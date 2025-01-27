import json
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np
import seaborn as sns

import pandas as pd

PATH_DATA = "data"
RESULTS_FOLDER = "results_images"
GENERAL_RESULT_FOLDER = "general_results_images"
RESULTS_FILE = "results_metrics.json"
IMAGE_COMPARISON_NAME = "comparison.png"
GENERAL_COMPARISON_MARKDOWN_FILE = "general_comparison.md"
NEED_MARKDOWN = True
TOTAL_DATASETS = 30
DATASET_INFO_CSV = "data/datasets_info.csv"


# Place the name of specific dataset for getting the results of only specified datasets
datasets = []

# return the list of datasets
def get_dataset_names(path_data: str) -> list:
    """
    Get the list of datasets in the data folder.

    Args: 
        path_data (str): The path to the data folder.
    
    Returns:
        datasets (list): The list of datasets in the data folder
    """

    if len(datasets) == 0:
        for name in os.listdir(path_data):
            if os.path.isdir(os.path.join(path_data, name)):
                datasets.append(name)
    return datasets

def load_results(file_path: str):
    """
    Load the results from a JSON file.

    Args:
        file_path (str): The path to the JSON file.
    
    Returns:
        results (dict): The dictionary containing the results.
    """

    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except json.JSONDecodeError:
        print(f"Error: {file_path} is not a valid JSON file.")
    return None

def create_chart(classifiers: list, metric: list, title: str, xlabel: str, ylabel: str, file_path: str, color_palette: str) -> None:
    """
    Create a bar chart comparing the metric of different classifiers.

    Args:
        classifiers (list): The list of classifiers.
        metric (list): The values of the metric compared.
        title (str): The title of the plot.
        xlabel (str): The x-axis label.
        ylabel (str): The y-axis label.
        file_path (str): The path to save the image.
        color_palette (str): The color palette to use for the bars.

    Returns:
        None
    """
    plt.figure(figsize=(12, 6))
    # Define the bar width and spacing
    bar_width = 0.6
    bar_spacing = 0.2
    bar_positions = np.arange(len(classifiers)) * (bar_width + bar_spacing)

    margin_ylim = 0.10
    min_y = np.min(metric)
    max_y = np.max(metric)
    
    # Add a margin to the min and max for preparing the graph limits
    min_ylim = max(0, min_y - margin_ylim)
    max_ylim = min(1, max_y + margin_ylim)

    bars = plt.bar(
        bar_positions,
        metric,
        width=bar_width,
        color=sns.color_palette(color_palette, len(classifiers)),
        edgecolor="black",
        linewidth=1.5
    )

    # Align the values to the top of the bars
    for bar in bars:
        width = bar.get_width()
        height = bar.get_height()
        x = bar.get_x()
        plt.text(
            x + width / 2,
            height + 0.001,
            f"{height:.3f}",
            ha="center",
            va="bottom",
            color="black"
        )

    # Prepare the legend and attach it outside the plot
    plt.legend(bars, classifiers, title="Classifiers", bbox_to_anchor=(1.05, 1), loc="upper left")

    # Removes the black ticks on the x axis
    plt.xticks([])
    
    # Add the title, labels and limits
    plt.title(title, fontsize=14, pad=20)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.ylim(min_ylim, max_ylim)
    plt.tight_layout()

    # Save the plot
    plt.savefig(file_path, dpi=300)
    plt.close()

def create_time_chart(classifiers: list, times: list, title: str, xlabel: str, ylabel: str, file_path: str, color_palette: str) -> None:
    """
    Create a bar chart comparing the times (in seconds) of different classifiers.

    Args:
        classifiers (list): The list of classifiers.
        times (list): The values of the times (in seconds) compared.
        title (str): The title of the plot.
        xlabel (str): The x-axis label.
        ylabel (str): The y-axis label.
        file_path (str): The path to save the image.
        color_palette (str): The color palette to use for the bars.

    Returns:
        None
    """

    plt.figure(figsize=(12, 6))
    # Define the bar width and spacing
    bar_width = 0.6
    bar_spacing = 0.2
    bar_positions = np.arange(len(classifiers)) * (bar_width + bar_spacing)

    margin_ylim = 0.10 * (max(times) - min(times)) if len(times) > 0 else 0
    min_y = min(times)
    max_y = max(times)

    # Add a margin to the min and max for preparing the graph limits
    min_ylim = max(0, min_y - margin_ylim)
    max_ylim = max_y + margin_ylim

    bars = plt.bar(
        bar_positions,
        times,
        width=bar_width,
        color=sns.color_palette(color_palette, len(classifiers)),
        edgecolor="black",
        linewidth=1.5
    )

    # Align the values to the top of the bars
    for bar in bars:
        width = bar.get_width()
        height = bar.get_height()
        x = bar.get_x()
        plt.text(
            x + width / 2,
            height + 0.00001,
            f"{height:.5f} s",  # Displaying time in seconds
            ha="center",
            va="bottom",
            color="black"
        )

    # Prepare the legend and attach it outside the plot
    plt.legend(bars, classifiers, title="Classifiers", bbox_to_anchor=(1.05, 1), loc="upper left")

    # Removes the black ticks on the x axis
    plt.xticks([])
    
    # Add the title, labels and limits
    plt.title(title, fontsize=14, pad=20)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.ylim(min_ylim, max_ylim)
    # Save the plot
    plt.tight_layout()
    plt.savefig(file_path, dpi=300)
    plt.close()

def create_accuracy_plot_with_confidence_interval(dataframe: pd.DataFrame, metric: list, file_path: str, title: str, is_similarity_forest: bool = False) -> None:
    """
    Create a plot with the accuracy metric and confidence intervals for the different classifiers.
    
    Args:
        dataframe (pd.DataFrame): The DataFrame containing the results.
        metric (list): The metric to plot.
        file_path (str): The path to save the image.
        title (str): The title of the plot.
        is_similarity_forest (bool): Whether the comparison is for SimilarityForest models.
        
    Returns:
        None
    """
    # gets the mean and standard deviation of the metric for each classifier
    summary = dataframe.groupby("classifier").agg({metric: ["mean", "std"]})

    means = summary[metric]["mean"]
    stds = summary[metric]["std"]

    lower_bounds = means - stds
    upper_bounds = np.minimum(means + stds, 1)
    error_bars = [means - lower_bounds, upper_bounds - means]

    plt.figure(figsize=(12, 8))

    plt.errorbar(
        x= means,
        y= summary.index,
        xerr= error_bars,
        fmt="o",
        color="steelblue",
        ecolor="black",
        elinewidth=2,
        capsize=5,
        capthick=2,
    )

    plt.title(title)
    plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.xlabel(metric.replace("_", " ").title())
    plt.xlim(0, 1)
    plt.ylabel("Classifiers")
    plt.tight_layout()

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    if not is_similarity_forest:
        plot_path = os.path.join(file_path, f"{metric}_CI_plot.png")
    else:
        plot_path = os.path.join(file_path, f"similarities_{metric}_CI_plot.png")

    plt.savefig(plot_path, dpi=300)
    plt.close()

def create_accuracy_plot_with_confidence_interval_time(dataframe: pd.DataFrame, metric: list, file_path: str, title: str, is_similarity_forest: bool = False) -> None:
    """
    Create a plot with the accuracy metric and confidence intervals for the different classifiers.
    
    Args:
        dataframe (pd.DataFrame): The DataFrame containing the results.
        metric (list): The metric to plot.
        file_path (str): The path to save the image.
        title (str): The title of the plot.
        is_similarity_forest (bool): Whether the comparison is for SimilarityForest models.
        
    Returns:
        None
    """
    # gets the mean and standard deviation of the metric for each classifier
    summary = dataframe.groupby("classifier").agg({metric: ["mean", "std"]})
    means = summary[metric]["mean"]
    stds = summary[metric]["std"]

    lower_bounds = np.maximum(means - stds, 0)
    upper_bounds = means + stds
    error_bars = [means - lower_bounds, upper_bounds - means]

    plt.figure(figsize=(12, 8))

    plt.errorbar(
        x= means,
        y= summary.index,
        xerr= error_bars,
        fmt="o",
        color="steelblue",
        ecolor="black",
        elinewidth=2,
        capsize=5,
        capthick=2,
    )

    plt.title(title)
    plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.xlabel(metric.replace("_", " ").title() + " (in seconds)")
    plt.ylabel("Classifiers")
    plt.tight_layout()

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    if not is_similarity_forest:
        plot_path = os.path.join(file_path, f"{metric}_CI_plot.png")
    else:
        plot_path = os.path.join(file_path, f"similarities_{metric}_CI_plot.png")

    plt.savefig(plot_path, dpi=300)
    plt.close()



def main():
    dataset_names = get_dataset_names(PATH_DATA)

    if not dataset_names:
        print(f"No datasets found in {PATH_DATA}")
        return
    


    loaded_datasets = list()
    for dataset_name in dataset_names:
        dataset_path = os.path.join(PATH_DATA, dataset_name)
        dataset_results_path = os.path.join(dataset_path, RESULTS_FILE)
        loaded_dataset = load_results(dataset_results_path)
        if loaded_dataset is None:
            print(f"No results found for {dataset_name}")
            continue
        
        loaded_datasets.extend(loaded_dataset)

    general_dataframes = pd.json_normalize(loaded_datasets)
    general_dataframes.columns = general_dataframes.columns.str.replace("metrics.", "", regex=False)
    general_dataframes = general_dataframes.drop(columns=["random_state", "test_size", "n_estimators"])

    datasets_info = pd.read_csv(DATASET_INFO_CSV)
    columns_to_merge = ["dataset","classes_range","features_range","istances_range","balance_class"]
    general_dataframes = general_dataframes.merge(datasets_info[columns_to_merge], on="dataset", how="left")

    new_cols = ["classes_range","features_range","istances_range","balance_class"]
    existing_cols = [c for c in general_dataframes.columns if c not in new_cols]
    general_dataframes = general_dataframes[existing_cols + new_cols]


    for index, row in general_dataframes.iterrows():
        if "classifier" in row and "SimilarityBasedForest" in row['classifier']:
            general_dataframes.at[index, "classifier"] = general_dataframes.at[index, "classifier"].replace("SimilarityBasedForest-", "SimilarityForest")
    
    df_similarity = general_dataframes[general_dataframes["classifier"].str.contains("SimilarityForest")]
    df_others = general_dataframes[general_dataframes["classifier"].str.contains("SimilarityForest") == False]

    metric_map = {
        "accuracy": "Accuracy",
        "balanced_accuracy": "Balanced Accuracy",
        "macro_f1": "Macro F1",
        "micro_f1": "Micro F1",
        "training_time" : "Training time",
        "prediction_time" : "Prediction time",
        "total_time" : "Total time"
    }

    list_of_groups = list()

    df_balanced = general_dataframes[general_dataframes['balance_class'] == 'balanced'].reset_index(drop=True)
    df_unbalanced = general_dataframes[general_dataframes['balance_class'] == 'unbalanced'].reset_index(drop=True)
    df_very_unbalanced = general_dataframes[general_dataframes['balance_class'] == 'very unbalanced'].reset_index(drop=True)

    df_features_1_8 = general_dataframes[general_dataframes['features_range'] == '1-8'].reset_index(drop=True)
    df_features_9_19 = general_dataframes[general_dataframes['features_range'] == '9-19'].reset_index(drop=True)
    df_features_20_plus = general_dataframes[general_dataframes['features_range'] == '20+'].reset_index(drop=True)
    
    df_istances_1_999 = general_dataframes[general_dataframes['istances_range'] == '1-999'].reset_index(drop=True)
    df_istances_1000_9999 = general_dataframes[general_dataframes['istances_range'] == '1000-9999'].reset_index(drop=True)
    df_istances_10000_plus = general_dataframes[general_dataframes['istances_range'] == '10000+'].reset_index(drop=True)

    df_classes_2 = general_dataframes[general_dataframes['classes_range'] == '2'].reset_index(drop=True)
    df_classes_3_4 = general_dataframes[general_dataframes['classes_range'] == '3-4'].reset_index(drop=True)
    df_classes_5_plus = general_dataframes[general_dataframes['classes_range'] == '5+'].reset_index(drop=True)


    list_of_groups.append(("Balanced", df_balanced))
    list_of_groups.append(("Unbalanced", df_unbalanced))
    list_of_groups.append(("Very Unbalanced", df_very_unbalanced))
    list_of_groups.append(("Features 1-8", df_features_1_8))
    list_of_groups.append(("Features 9-19", df_features_9_19))
    list_of_groups.append(("Features 20+", df_features_20_plus))
    list_of_groups.append(("Istances 1-999", df_istances_1_999))
    list_of_groups.append(("Istances 1000-9999", df_istances_1000_9999))
    list_of_groups.append(("Istances 10000+", df_istances_10000_plus))
    list_of_groups.append(("Classes 2", df_classes_2))
    list_of_groups.append(("Classes 3-4", df_classes_3_4))
    list_of_groups.append(("Classes 5+", df_classes_5_plus))
    list_of_groups.append(("General", general_dataframes))

    for category, df in list_of_groups:
        print(category)
        df_filtered_similarity = df[df["classifier"].str.contains("SimilarityForest")]
        df_filtered_others = df[df["classifier"].str.contains("SimilarityForest") == False]

        similarity_average = (
            df_filtered_similarity
            .groupby("classifier")[[metric for metric in metric_map.keys()]]
            .mean()
            .reset_index()
        )

        best_similarity_models = {}

        category_path = os.path.join(GENERAL_RESULT_FOLDER, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

        for metric, metric_name in metric_map.items():

            if "time" in metric:
                best_model = (
                    similarity_average
                    .sort_values(by=metric, ascending=True)
                    .iloc[[0]]
                )

            else:
                best_model = (
                    similarity_average
                    .sort_values(by=metric, ascending=False)
                    .iloc[[0]]
                )

            best_similarity_models[metric] = best_model

            if "time" in metric:
                create_accuracy_plot_with_confidence_interval_time(
                    df_filtered_similarity,
                    metric,
                    category_path,
                    f"Comparison of SimilarityForest Models ({metric.replace("_", " ").title()}) - {category}",
                    is_similarity_forest=True
                )
            else:
                create_accuracy_plot_with_confidence_interval(
                    df_filtered_similarity,
                    metric,
                    category_path,
                    f"Comparison of SimilarityForest Models ({metric.replace("_", " ").title()}) - {category}",
                    is_similarity_forest=True
                )


        for metric, df_best_model in best_similarity_models.items():
            
            df_to_be_added = df_filtered_similarity[df_filtered_similarity["classifier"].isin(df_best_model["classifier"])]

            new_other_df = pd.concat([df_filtered_others, df_to_be_added], ignore_index=True)

            if "time" in metric:
                create_accuracy_plot_with_confidence_interval_time(
                    new_other_df,
                    metric,
                    category_path,
                    f"Best SimilarityForest vs State-of-the-Art Models ({metric.replace("_", " ").title()}) - {category}"
                )
            else:
                create_accuracy_plot_with_confidence_interval(
                    new_other_df,
                    metric,
                    category_path,
                    f"Best SimilarityForest vs State-of-the-Art Models ({metric.replace("_", " ").title()}) - {category}"
                )

    for metric, metric_name in metric_map.items():
        for dataset_name in dataset_names:
            dataset_path = os.path.join(PATH_DATA, dataset_name)
            images_path = os.path.join(dataset_path, RESULTS_FOLDER)
          
            if not os.path.exists(images_path):
                os.makedirs(images_path)
            
            df_dataset = df_similarity[df_similarity["dataset"] == dataset_name]

            df_similarity_metric = df_dataset.groupby("classifier")[metric].mean().reset_index()
            
            similarities_images_path = os.path.join(images_path, "similarities")
            if not os.path.exists(similarities_images_path):
                os.makedirs(similarities_images_path)
            
            if "time" in metric:
                create_time_chart(
                    classifiers=df_similarity_metric['classifier'].tolist(),
                    times=df_similarity_metric[metric].tolist(),
                    title=f"{dataset_name.title()} - SimilarityForests Comparison ({metric_name})",
                    xlabel="Similarity Models",
                    ylabel=metric_name,
                    file_path=os.path.join(similarities_images_path, f"similarity_forests_comparison_{metric}.png"),
                    color_palette="mako"
                )

                best_value = df_similarity_metric[metric].min()
            else:
                create_chart(
                    classifiers=df_similarity_metric['classifier'].tolist(),
                    metric=df_similarity_metric[metric].tolist(),
                    title=f"{dataset_name.title()} - SimilarityForests Comparison ({metric_name})",
                    xlabel="Similarity Models",
                    ylabel=metric_name,
                    file_path=os.path.join(similarities_images_path, f"similarity_forests_comparison_{metric}.png"),
                    color_palette="mako"
                )

                best_value = df_similarity_metric[metric].max()
            
            best_similarity_models = df_similarity_metric[df_similarity_metric[metric] == best_value]
            best_similarity_models = best_similarity_models.drop_duplicates(subset="classifier")

            df_dataset_general = df_others[df_others["dataset"] == dataset_name]
            df_dataset_general = pd.concat([df_dataset_general, best_similarity_models], ignore_index=True)

            sota_images_path = os.path.join(images_path, "sota comparison")
            if not os.path.exists(sota_images_path):
                os.makedirs(sota_images_path)
            
            if "time" in metric:
                create_time_chart(
                    classifiers=df_dataset_general['classifier'].tolist(),
                    times=df_dataset_general[metric].tolist(),
                    title=f"{dataset_name.title()} - SOTA vs. Best SimilarityForest ({metric_name})",
                    xlabel="Classifiers",
                    ylabel=metric_name,
                    file_path=os.path.join(sota_images_path, f"sota_vs_similarityforest_{metric}.png"),
                    color_palette="mako"
                )
            else:
                create_chart(
                    classifiers=df_dataset_general['classifier'].tolist(),
                    metric=df_dataset_general[metric].tolist(),
                    title=f"{dataset_name.title()} - SOTA vs. Best SimilarityForest ({metric_name})",
                    xlabel="Classifiers",
                    ylabel=metric_name,
                    file_path=os.path.join(sota_images_path, f"sota_vs_similarityforest_{metric}.png"),
                    color_palette="mako"
                )



if __name__ == "__main__":
    main()