# Wine

**Description**:

These data are the results of a chemical analysis of wines grown in the same region in Italy but derived from three different cultivars. The analysis determined the quantities of 13 constituents found in each of the three types of wines.

---

## Table of Contents
- [Wine](#wine)
  - [Table of Contents](#table-of-contents)
  - [Dataset Overview](#dataset-overview)
  - [Variables](#variables)
  - [Target Variable](#target-variable)
  - [Dataset Details](#dataset-details)
  - [File Structure](#file-structure)
  - [Sample Data](#sample-data)
  - [Performance Metrics](#performance-metrics)
  - [Acknowledgments](#acknowledgments)

---

## Dataset Overview

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Wine](https://archive.ics.uci.edu/dataset/109/wine)

- **Domain**: Physics and Chemistry

- **Format**: CSV

---

## Variables

| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***Class*** | **Target** | Type of wine | Categorical | 1, 2, 3 |
| ***Alcohol*** | Feature | Alcohol content of the wine | Continuous | - |
| ***Malic acid*** | Feature | Malic acid content of the wine | Continuous | - |
| ***Ash*** | Feature | Ash content of the wine | Continuous | - |
| ***Alcalinity_of_ash*** | Feature | Alcalinity of ash in the wine | Continuous | - |
| ***Magnesium*** | Feature | Magnesium content of the wine | Integer | - |
| ***Total_phenols*** | Feature | Total phenol content of the wine | Continuous | - |
| ***Flavanoids*** | Feature | Flavanoid content of the wine | Continuous | - |
| ***Nonflavanoid phenols*** | Feature | Nonflavanoid phenol content of the wine | Continuous | - |
| ***Proanthocyanins*** | Feature | Proanthocyanin content of the wine | Continuous | - |
| ***Color_intensity*** | Feature | Color intensity of the wine | Continuous | - |
| ***Hue*** | Feature | Hue of the wine | Continuous | - |
| ***OD280/OD315_of_diluted wines*** | Feature | OD280/OD315 ratio of the wine | Continuous | - |
| ***Proline*** | Feature | Proline content of the wine | Integer | - |

---

## Target Variable

- **Name**: *Class*
- **Type**: Categorical
- **Values**:
  - 1 = Class 1
  - 2 = Class 2
  - 3 = Class 3

---

## Dataset Details

- **Has missing values?**: no
- **Number of Instances**: 178 instances
- **Number of Features**: 13
- **Class Distribution**:
  - Class 1 = 59 instances
  - Class 2 = 71 instances
  - Class 3 = 48 instances

---

## File Structure

- `wine.csv`: Main dataset file.
- `README.md`: Documentation file (this file).
- `configuration.json`: Configuration file containing the instructions for DatasetPreprocessor.
- `results_images/`: A folder containing the charts of the metrics analyzed.
- `results_metrics.json`: The json file containing the results of the models for this dataset.

---

## Sample Data

An example of how the dataset is structured:

| Alcohol | Malic acid | Ash | Alcalinity of ash | Magnesium | Total phenols | Flavanoids | Nonflavanoid phenols | Proanthocyanins | Color intensity | Hue | OD280/OD315 of diluted wines | Proline | Class |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 13.72 | 1.43 | 2.5 | 16.7 | 108 | 3.4 | 3.67 | .19 | 2.04 | 6.8 | .89 | 2.87 | 1285 |
| 2 | 12.37 | .94 | 1.36 | 10.6 | 88 | 1.98 | .57 | .28 | .42 | 1.95 | 1.05 | 1.82 | 520 |
| 3 | 14.16 | 2.51 | 2.48 | 20 | 91 | 1.68 | .7 | .44 | 1.24 | 9.7 | .62 | 1.71 | 660 |


---

## Performance Metrics

| Classifier | Accuracy | Balanced Accuracy | Micro F1 | Macro F1 | Training Time | Prediction Time | Total Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Random Forest | 98.1% | 98.1% | 98.1% | 98.3% | 0.021s | 0.001s | 0.022s |
| Extra Trees | 100.0% | 100.0% | 100.0% | 100.0% | 0.016s | 0.001s | 0.017s |
| XGBoost | 98.1% | 98.1% | 98.1% | 98.3% | 0.017s | 0.001s | 0.018s |
| AdaBoost | 100.0% | 100.0% | 100.0% | 100.0% | 0.033s | 0.003s | 0.036s |
| Gradient Boosting | 100.0% | 100.0% | 100.0% | 100.0% | 0.069s | 0.001s | 0.070s |
| SimilarityForest[cityblock] | 94.4% | 95.2% | 94.4% | 95.1% | 0.092s | 0.002s | 0.095s |
| SimilarityForest[cosine] | 85.2% | 83.1% | 85.2% | 84.4% | 0.012s | 0.003s | 0.015s |
| SimilarityForest[euclidean] | 94.4% | 93.7% | 94.4% | 94.7% | 0.012s | 0.002s | 0.014s |
| SimilarityForest[braycurtis] | 88.9% | 87.6% | 88.9% | 87.9% | 0.022s | 0.002s | 0.025s |
| SimilarityForest[canberra] | 96.3% | 96.0% | 96.3% | 96.0% | 0.022s | 0.003s | 0.025s |
| SimilarityForest[chebyshev] | 94.4% | 95.7% | 94.4% | 94.4% | 0.012s | 0.002s | 0.014s |
| SimilarityForest[correlation] | 85.2% | 83.1% | 85.2% | 84.4% | 0.022s | 0.002s | 0.024s |
| SimilarityForest[hamming] | 94.4% | 94.1% | 94.4% | 94.7% | 0.023s | 0.003s | 0.026s |

---

## Acknowledgments

Aeberhard, S. & Forina, M. (1992). Wine [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5PC7J.
