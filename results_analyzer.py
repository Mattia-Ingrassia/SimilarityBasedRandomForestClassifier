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
METRICS = ["accuracy", "balanced_accuracy", "macro_f1", "micro_f1"]
TOTAL_DATASETS = 30

# Place the name of specific dataset for getting the results of only specified datasets
datasets = []

# return the list of datasets
def get_datasets(path_data: str) -> list:
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

def process_results(results: list) -> tuple:
    """
    Process the results to separate SimilarityForest models from other models.

    Args:
        results (list): The list of results.
    
    Returns:
        similarity_models (list): The list of SimilarityForest models.
        other_models (list): The list of other models.
    """

    similarity_models = []
    other_models = []

    for result in results:
        if "SimilarityBasedForest" in result["classifier"]:
            result["classifier"] = result["classifier"].replace("SimilarityBasedForest-", "SimilarityForest")
            similarity_models.append(result)
        else:
            other_models.append(result)

    return similarity_models, other_models

def prepare_dataframe(results: list) -> pd.DataFrame:
    """
    Prepare a DataFrame from the results: Normalizing the json data, dropping unnecessary columns 
    and renaming columns.

    Args:
        results (list): The list of results.

    Returns:
        dataframe (pd.DataFrame): The DataFrame containing the results.
    """
    
    if not results:
        return pd.DataFrame()
    dataframe = pd.json_normalize(results)
    dataframe.columns = dataframe.columns.str.replace("metrics.", "", regex=False)
    dataframe = dataframe.drop(columns=["random_state", "test_size", "n_estimators"])
    return dataframe


def save_markdown(dataframe: pd.DataFrame, file_path: str) -> None:
    """
    Save the DataFrame as a markdown file.

    Args:
        dataframe (pd.DataFrame): The DataFrame to be saved.
        file_path (str): The path to the markdown file.

    Returns:
        None
    """
    
    try:
        # Replace underscores with spaces and capitalize the first letter of each word (micro_f1 -> Micro F1)
        dataframe.columns = dataframe.columns.str.replace("_", " ").str.title()

        # Format the columns: metrics as percentages and time columns as seconds
        percentage_columns = ["Accuracy", "Balanced Accuracy", "Micro F1", "Macro F1"]
        for col in percentage_columns:
            if col in dataframe.columns:
                dataframe[col] = dataframe[col].map(lambda x: f"{x * 100:.1f}%")
            else :
                print(f"Column {col} not found in the dataframe")
    
        time_columns = ["Training Time", "Prediction Time", "Total Time"]        
        for col in time_columns:
            if col in dataframe.columns:
                dataframe[col] = dataframe[col].map(lambda x: f"{x:.3f}s")
            else:
                print(f"Column {col} not found in the dataframe")
        
        dataframe.to_markdown(file_path, index=False, tablefmt="github", floatfmt=".3f")
        print(f"Markdown file saved at {file_path}")
    except Exception as e:
        print(f"Error during the creation of markdown file: {e}")

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
    plt.title(title, fontsize=14)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.ylim(min_ylim, max_ylim)
    plt.tight_layout()

    # Save the plot
    plt.savefig(file_path, dpi=300)
    plt.close()

def generate_comparison_charts(dataframe: pd.DataFrame, comparison_path: str, title: str, color_palette: str, is_similarity_forest: bool = False) -> None:
    """
    Generate comparison charts for the different metrics.

    Args:
        dataframe (pd.DataFrame): The DataFrame containing the results.
        comparison_path (str): The path to save the images.
        title (str): The title of the plot.
        color_palette (str): The color palette to use for the bars.
        is_similarity_forest (bool): Whether the comparison is for SimilarityForest models.

    Returns:
        None
    """
    
    metric_map = {
        "accuracy" : "Accuracy",
        "balanced_accuracy" : "Balanced Accuracy",
        "macro_f1" : "Macro F1",
        "micro_f1" : "Micro F1"
    }

    # Create a chart for each metric analyzed
    for metric, metric_name in metric_map.items():
        file_path = ""
        if not is_similarity_forest:
            file_path = os.path.join(comparison_path, f"{metric}_{IMAGE_COMPARISON_NAME}")
        else:
            file_path = os.path.join(comparison_path, f"similarities_{metric}_{IMAGE_COMPARISON_NAME}")
        create_chart(
            classifiers=dataframe["classifier"],
            metric=dataframe[metric],
            title=f"{metric_name} {title}",
            xlabel="Classifiers",
            ylabel=metric_name,
            file_path=file_path,
            color_palette=color_palette
        )


def process_dataset(dataset_name: str, path_data: str) -> None:
    """
    Process the results for a specific dataset.

    Args:
        dataset_name (str): The name of the dataset.
        path_data (str): The path to the data folder.

    Returns:
        None
    """

    dataset_path = os.path.join(path_data, dataset_name)
    dataset_results_path = os.path.join(dataset_path, RESULTS_FILE)
    results = load_results(dataset_results_path)

    if results is None:
        print(f"No results found for {dataset_name}")
        return
    
    similarity_results, other_results = process_results(results)

    df_similarity_forests = prepare_dataframe(similarity_results)
    df_others = prepare_dataframe(other_results)

    if NEED_MARKDOWN:
        print("Creating markdown files")
        dataframe_complete = pd.concat([df_others, df_similarity_forests], ignore_index=True)
        if "dataset" in dataframe_complete.columns:
            dataframe_complete = dataframe_complete.drop(columns=["dataset"])
        save_markdown(dataframe_complete, os.path.join(dataset_path, GENERAL_COMPARISON_MARKDOWN_FILE))

    images_path = os.path.join(dataset_path, RESULTS_FOLDER)
    
    if not os.path.exists(images_path):
        os.makedirs(images_path)
   
    if not df_others.empty and not df_similarity_forests.empty:
        best_similarity_models = pd.DataFrame()

        # Collect the best SimilarityForest models across all metrics
        for metric in METRICS:
            best_model = df_similarity_forests.sort_values(by=metric, ascending=False).iloc[[0]]
            best_similarity_models = pd.concat([best_similarity_models, best_model], ignore_index=True)

        # Remove duplicate models based on the "classifier" column
        best_similarity_models = best_similarity_models.drop_duplicates(subset="classifier")

        # Append the unique best SimilarityForest models to df_others
        df_others = pd.concat([df_others, best_similarity_models], ignore_index=True)

        generate_comparison_charts(df_others, images_path, "comparison with state-of-the-art ensemble models and SimilarityForest", "plasma")

    if not df_similarity_forests.empty:
        generate_comparison_charts(df_similarity_forests, images_path, "comparison with different similarity metrics", "mako", is_similarity_forest=True)


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

    plt.figure(figsize=(12, 8))

    plt.errorbar(
        x= means,
        y= summary.index,
        xerr= stds,
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

def get_aggregated_results(datasets: list) -> None:
    """
    Get the aggregated results for all datasets.
    
    Args:
        datasets (list): The list of datasets.
        
    Returns:
        None
    """

    aggregated_similarity_results = []
    aggregated_other_results = []
    
    for dataset_name in datasets:
        dataset_results_path = os.path.join(PATH_DATA, dataset_name, RESULTS_FILE)
        results = load_results(dataset_results_path)

        if results is not None:
            similarity_results, other_results = process_results(results)
            aggregated_similarity_results.extend(similarity_results)
            aggregated_other_results.extend(other_results)
        else:
            print(f"No results found for {dataset_name}")

    if len(aggregated_similarity_results) > 0:
        df_aggregated_similarity = pd.json_normalize(aggregated_similarity_results)
        df_aggregated_similarity.columns = df_aggregated_similarity.columns.str.replace("metrics.", "", regex=False)
 
        similarity_average = (
            df_aggregated_similarity
            .groupby("classifier")[[metric for metric in METRICS]]
            .mean()
            .reset_index()
        )

        best_similarity_models = {}

        for metric in METRICS:
            best_model = (
                similarity_average
                .sort_values(by=metric, ascending=False)
                .iloc[[0]]
            )
            best_similarity_models[metric] = best_model
            create_accuracy_plot_with_confidence_interval(
                df_aggregated_similarity,
                metric,
                GENERAL_RESULT_FOLDER,
                f"Comparison of SimilarityForest Models ({metric.replace("_", " ").title()})",
                is_similarity_forest=True
            )

    else:
        print("No SimilarityForest models found in the datasets")
    
    

    if len(aggregated_other_results) > 0 and len(best_similarity_models) > 0:
        df_aggregated_other = pd.json_normalize(aggregated_other_results)
        df_aggregated_other.columns = df_aggregated_other.columns.str.replace("metrics.", "", regex=False)

        for metric, df_best_model in best_similarity_models.items():
            
            df_to_be_added = df_aggregated_similarity[df_aggregated_similarity["classifier"].isin(df_best_model["classifier"])]

            new_other_df = pd.concat([df_aggregated_other, df_to_be_added], ignore_index=True)

            create_accuracy_plot_with_confidence_interval(
                new_other_df,
                metric,
                GENERAL_RESULT_FOLDER,
                f"Best SimilarityForest vs State-of-the-Art Models ({metric.replace("_", " ").title()})"
            )

def main():
    datasets = get_datasets(PATH_DATA)

    if not datasets:
        print(f"No datasets found in {PATH_DATA}")
        return

    for dataset_name in datasets:
        process_dataset(dataset_name, PATH_DATA)


    if len(datasets) == TOTAL_DATASETS:
        get_aggregated_results(datasets)



if __name__ == "__main__":
    main()