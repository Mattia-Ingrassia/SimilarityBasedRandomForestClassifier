import json
import os

from sklearn.metrics import accuracy_score, balanced_accuracy_score, f1_score
from sklearn.ensemble import AdaBoostClassifier, ExtraTreesClassifier, GradientBoostingClassifier, RandomForestClassifier
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

from DatasetPreprocessor import DatasetPreprocessor
from SimilarityBasedRandomForestClassifier import SimilarityBasedRandomForestClassifier


# Run settings
RANDOM_STATE = 23
N_ESTIMATORS = 10
MAX_DEPTH = 4
DISTANCE_METRIC = "euclidean"
LEARNING_RATE = 1.0
TEST_SIZE = 0.3
PATH_DATA = "data"
PATH_CONFIG = os.path.join(PATH_DATA, "datasets_config.json")
PATH_RESULTS = "results_metrics.json"

# False if the preprocessing has already been done (if it has
# been already done, the files X.npy and Y.npy already exists), 
# True otherwise
FROM_SCRATCH = True

# For running only explicit datasets, add the name of them
# inside this variable.
datasets = []
models = []

# if no datasets where specified, load all the datasets
if len(datasets) == 0:
    for name in os.listdir(PATH_DATA):
        if os.path.isdir(os.path.join(PATH_DATA, name)):
            datasets.append(name)

# function for loading the datasets configuration.
# returns a json object containing all the datasets configuration.
def load_config(config_path):
    try:
        with open(config_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Configuration file {config_path} not found.")
    except json.JSONDecodeError:
        print(f"Error: Configuration file {config_path} is not a valid json file")
    return None

# function for initializing the classifiers with the specified parameters.  
# returns a dictionary {classifier_name : classifier} containing all the classifiers.
def init_classifiers() -> dict:
    classifiers = {
        "Edited Variant of Random Forest": SimilarityBasedRandomForestClassifier(
            n_estimators=N_ESTIMATORS,
            max_depth=MAX_DEPTH,
            random_state=RANDOM_STATE,
            distance_metric=DISTANCE_METRIC
        ),
        "Random Forest": RandomForestClassifier(
            n_estimators=N_ESTIMATORS,
            random_state=RANDOM_STATE,
            min_samples_leaf=1,
            max_features=None
        ),
        "Extra Trees": ExtraTreesClassifier(
            n_estimators=N_ESTIMATORS,
            random_state=RANDOM_STATE,
            min_samples_leaf=1,
            max_features=None
        ),
        "AdaBoost": AdaBoostClassifier(
            n_estimators=N_ESTIMATORS,
            learning_rate=LEARNING_RATE,
            algorithm="SAMME",
            random_state=RANDOM_STATE
        ),
        "Gradient Boosting": GradientBoostingClassifier(
            n_estimators=N_ESTIMATORS,
            learning_rate=LEARNING_RATE,
            random_state=RANDOM_STATE
        ),
        "XGBoost": XGBClassifier(
            n_estimators=N_ESTIMATORS,
            learning_rate=LEARNING_RATE,
            random_state=RANDOM_STATE
        ),
    }
    return classifiers



# Prepare the dataset following the configuration
# specified in the dataset_config.
# Returns the splitted dataset (X_train, X_test, y_train, y_test)
def prepare_dataset(dataset_config: dict, dataset_name: str) -> list:
    columns = dataset_config.get("columns")
    target_column = dataset_config.get("target_column")
    needs_y_encoding = dataset_config.get("needs_y_encoding")
    categorical_features = dataset_config.get("categorical_features")
    na_values = dataset_config.get("na_values")
    ignored_columns = dataset_config.get("ignored_columns")

    dataset_preprocessor = DatasetPreprocessor(
        dataset_name=dataset_name,
        columns=columns,
        target_column=target_column,
        needs_y_encoding=needs_y_encoding,
        categorical_features=categorical_features,
        ignored_columns=ignored_columns,
        na_values=na_values
    )
    X, y = dataset_preprocessor.load_dataset(from_scratch=FROM_SCRATCH)
    return train_test_split(X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE)

# Evaluate the classifier using the specified dataset.
# Returns a dictionary containing the metrics.
def evaluate_classifier(classifier, X_train, X_test, y_train, y_test) -> dict:
    classifier.fit(X_train, y_train)
    predictions = classifier.predict(X_test)
    return {
        "accuracy": accuracy_score(y_test, predictions),
        "balanced_accuracy": balanced_accuracy_score(y_test, predictions),
        "micro_f1": f1_score(y_test, predictions, average='micro'),
        "macro_f1": f1_score(y_test, predictions, average='macro')
    }

def print_metrics(classifier_name: str, metrics: dict):
    print(f"{classifier_name}:")
    print(f"  Accuracy: {metrics['accuracy']:.5f}")
    print(f"  Balanced Accuracy: {metrics['balanced_accuracy']:.5f}")
    print(f"  Micro F1: {metrics['micro_f1']:.5f}")
    print(f"  Macro F1: {metrics['macro_f1']:.5f}")
    print("-" * 60)

def save_metrics_to_json(dataset_name: str, classifier_name: str, metrics: dict, path_results: str = PATH_RESULTS):
    result_entry = {
        "dataset": dataset_name,
        "classifier": classifier_name,
        "metrics": metrics
    }

    if os.path.exists(path_results):
        with open(path_results, 'r') as file:
            results = json.load(file)
    else:
        results = []

    results.append(result_entry)
    with open(path_results, 'w') as file:
        json.dump(results, file, indent=4)
        print(f"Metrics saved for {classifier_name} on dataset {dataset_name}.")


def main():
    datasets_config = load_config(PATH_CONFIG)
    if datasets_config is not None:
        # Initialize the results file
        with open(PATH_RESULTS, 'w') as file:
            json.dump([], file, indent=4)
            print(f"Results file {PATH_RESULTS} has been created.")

        for dataset_name in datasets:
            dataset_config = datasets_config.get(dataset_name)
            if dataset_config is not None:
                print(f"Processing Dataset: {dataset_name}")
                X_train, X_test, y_train, y_test = prepare_dataset(dataset_config, dataset_name)
                classifiers = init_classifiers()
                for classifier_name, classifier in classifiers.items():
                    metrics = evaluate_classifier(classifier, X_train, X_test, y_train, y_test)
                    print_metrics(classifier_name, metrics)
                    save_metrics_to_json(dataset_name, classifier_name, metrics)
            else:
                print(f"Configuration not found for dataset: {dataset_name}")

if __name__ == "__main__":
    main()


