import json
import os
from time import time

from sklearn.metrics import accuracy_score, balanced_accuracy_score, f1_score
from sklearn.ensemble import AdaBoostClassifier, ExtraTreesClassifier, GradientBoostingClassifier, RandomForestClassifier
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

from DatasetPreprocessor import DatasetPreprocessor
from classifier.SimilarityBasedRandomForestClassifier import SimilarityBasedRandomForestClassifier

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

PATH_RUN_CONFIGURATION = "run_configuration.json"
PATH_DATA = "data"
RESULTS_FILE_NAME = "results_metrics.json"

# False if the preprocessing has already been done (if it has
# been already done, the files X.npy and Y.npy already exists), 
# True otherwise
FROM_SCRATCH = True

# those values are loaded from PATH_RUN_CONFIGURATION file
NUMBER_OF_ESTIMATORS = []
TEST_SIZES = []
RANDOM_STATES = []
DISTANCE_METRICS = []

# For running only explicit datasets, add the name of them
# inside this variable.
datasets = []

# function for loading the datasets configuration.
# returns a json object containing all the datasets configuration.
def load_config(dataset_name: str):
    configuration_path = os.path.join(PATH_DATA, dataset_name, "configuration.json")
    try:
        with open(configuration_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Configuration file {configuration_path} not found.")
    except json.JSONDecodeError:
        print(f"Error: Configuration file {configuration_path} is not a valid json file")
    return None

# function for initializing the classifiers with the specified parameters.  
# returns a dictionary {classifier_name : classifier} containing all the classifiers.
def init_classifiers(random_state: int, number_of_estimators: int) -> dict:
    classifiers = {
        "Random Forest": RandomForestClassifier(
            n_estimators=number_of_estimators,
            random_state=random_state,
            min_samples_leaf=1,
            max_features='sqrt'
        ),
        "Extra Trees": ExtraTreesClassifier(
            n_estimators=number_of_estimators,
            random_state=random_state,
            min_samples_leaf=1,
            max_features='sqrt'
        ),
        "XGBoost": XGBClassifier(
            n_estimators=number_of_estimators,
            random_state=random_state
        ),
        "AdaBoost": AdaBoostClassifier(
            n_estimators=number_of_estimators,
            random_state=random_state,
            algorithm="SAMME",
            learning_rate=1.0
        ),
        "Gradient Boosting": GradientBoostingClassifier(
            n_estimators=number_of_estimators,
            random_state=random_state,
            learning_rate=0.1
        ),
    }

    for metric in DISTANCE_METRICS:
        classifiers.update(
            {
                f"SimilarityBasedForest-[{metric}]" : 
                SimilarityBasedRandomForestClassifier(
                    n_estimators=number_of_estimators,
                    random_state=random_state,
                    distance_metric=metric,
                    n_jobs=-1
                )
            }
        )            
    return classifiers



# Prepare the dataset following the configuration
# specified in the dataset_config.
# Returns the splitted dataset (X_train, X_test, y_train, y_test)
def prepare_dataset(dataset_configuration: dict, dataset_name: str, test_size: float, random_state: int) -> list:
    dataset_preprocessor = DatasetPreprocessor(
        dataset_name= dataset_name,
        columns= dataset_configuration.get("columns"),
        target_column= dataset_configuration.get("target_column"),
        input_data_path= os.path.join(PATH_DATA, dataset_name),
        output_data_path= PATH_DATA,
        needs_y_encoding= dataset_configuration.get("needs_y_encoding"),
        categorical_features= dataset_configuration.get("categorical_features"),
        ignored_columns= dataset_configuration.get("ignored_columns"),
        na_values= dataset_configuration.get("na_values")
    )
    X, y = dataset_preprocessor.load_dataset(from_scratch=FROM_SCRATCH)
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

# Evaluate the classifier using the specified dataset.
# Returns a dictionary containing the metrics.
def evaluate_classifier(classifier, X_train, X_test, y_train, y_test) -> dict:
    start_time = time()
    classifier.fit(X_train, y_train)
    training_time = time() - start_time

    start_time = time()
    predictions = classifier.predict(X_test)
    prediction_time = time() - start_time
    total_time = training_time + prediction_time
    return {
        "accuracy": accuracy_score(y_test, predictions),
        "balanced_accuracy": balanced_accuracy_score(y_test, predictions),
        "micro_f1": f1_score(y_test, predictions, average='micro'),
        "macro_f1": f1_score(y_test, predictions, average='macro'),
        "training_time": training_time,
        "prediction_time": prediction_time,
        "total_time": total_time
    }

def print_metrics(classifier_name: str, metrics: dict):
    print(f"{classifier_name}:")
    print(f"  Accuracy: {metrics['accuracy']:.5f}")
    print(f"  Balanced Accuracy: {metrics['balanced_accuracy']:.5f}")
    print(f"  Micro F1: {metrics['micro_f1']:.5f}")
    print(f"  Macro F1: {metrics['macro_f1']:.5f}")
    print(f"  Training Time: {metrics['training_time']:.5f} seconds")
    print(f"  Prediction Time: {metrics['prediction_time']:.5f} seconds")
    print(f"  Total Time: {metrics['total_time']:.5f} seconds")
    print("-" * 50)

def save_metrics_to_json(dataset_name: str, classifier_name: str, random_state: int, test_size: float, number_of_estimators: int, metrics: dict):
    result_entry = {
        "dataset": dataset_name,
        "classifier": classifier_name,
        "random_state": random_state,
        "test_size": test_size,
        "n_estimators": number_of_estimators,
        "metrics": metrics
    }

    dataset_results_path = os.path.join(PATH_DATA, dataset_name, RESULTS_FILE_NAME)

    if os.path.exists(dataset_results_path):
        with open(dataset_results_path, 'r') as file:
            results = json.load(file)
    else:
        results = []

    results.append(result_entry)

    with open(dataset_results_path, 'w') as file:
        json.dump(results, file, indent=4)
        #print(f"Metrics saved for {classifier_name} on dataset {dataset_name} in {dataset_results_path}.")

def load_datasets() -> list:
    # if no datasets where specified, load all the datasets
    if len(datasets) == 0:
        for name in os.listdir(PATH_DATA):
            if os.path.isdir(os.path.join(PATH_DATA, name)):
                datasets.append(name)
    return datasets

def load_run_configuration():
    global NUMBER_OF_ESTIMATORS, TEST_SIZES, RANDOM_STATES, DISTANCE_METRICS
    
    try:
        with open(PATH_RUN_CONFIGURATION, 'r') as file:
            run_configuration = json.load(file)
            if run_configuration is not None:
                NUMBER_OF_ESTIMATORS = run_configuration.get("number_of_estimators")
                TEST_SIZES = run_configuration.get("test_sizes")
                RANDOM_STATES = run_configuration.get("random_states")
                DISTANCE_METRICS = run_configuration.get("distance_metrics")
    except FileNotFoundError:
        print(f"Error: Configuration file {PATH_RUN_CONFIGURATION} not found.")
    except json.JSONDecodeError:
        print(f"Error: Configuration file {PATH_RUN_CONFIGURATION} is not a valid json file")

def main():
    global datasets
    
    datasets = load_datasets()
    load_run_configuration()

    total_iterations = len(TEST_SIZES) * len(RANDOM_STATES) * len(NUMBER_OF_ESTIMATORS) * (len(DISTANCE_METRICS) + 5)
    for dataset_name in datasets:
        dataset_configuration = load_config(dataset_name)
        
        dataset_results_path = os.path.join(PATH_DATA, dataset_name, RESULTS_FILE_NAME)
        with open(dataset_results_path, 'w') as file:
            json.dump([], file, indent=4)
        print(f"Results file {RESULTS_FILE_NAME} for dataset {dataset_name} has been created.")
        
        progress_tracker = 0
        if dataset_configuration is not None:
            print(f"Processing Dataset: {dataset_name}")
            for test_size in TEST_SIZES:
                for random_state in RANDOM_STATES:
                    X_train, X_test, y_train, y_test = prepare_dataset(dataset_configuration, dataset_name, test_size, random_state)
                    for number_of_estimators in NUMBER_OF_ESTIMATORS:
                        classifiers = init_classifiers(random_state, number_of_estimators)
                        for classifier_name, classifier in classifiers.items():
                            metrics = evaluate_classifier(classifier, X_train, X_test, y_train, y_test)
                            # print_metrics(classifier_name, metrics)
                            save_metrics_to_json(dataset_name, classifier_name, random_state, test_size, number_of_estimators, metrics)
                            progress_tracker += 1
                            print(f"{dataset_name} - progress: {progress_tracker}/{total_iterations}")
        else:
            print(f"Configuration not found for dataset: {dataset_name}")
        print(f"Dataset: {dataset_name} processed.")            

if __name__ == "__main__":
    main()


