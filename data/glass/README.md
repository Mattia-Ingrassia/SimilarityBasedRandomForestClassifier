# Glass

**Description**:

From USA Forensic Science Service; 6 types of glass; defined in terms of their oxide content (i.e. Na, Fe, K, etc)

---

## Table of Contents
- [Glass](#glass)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Glass Identification](https://archive.ics.uci.edu/dataset/42/glass+identification)

- **Domain**: Physics and Chemistry

- **Format**: CSV

---

## Variables

| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***Id*** | ID | ID column (should be ignored) | Integer | - |
| ***RI*** | Feature | refractive index | Continuous | - |
| ***Na*** | Feature | sodium | Continuous | - |
| ***Mg*** | Feature | magnesium | Continuous | - |
| ***Al*** | Feature | aluminum | Continuous | - |
| ***Si*** | Feature | silicon | Continuous | - |
| ***K*** | Feature | potassium | Continuous | - |
| ***Ca*** | Feature | calcium | Continuous | - |
| ***Ba*** | Feature | barium | Continuous | - |
| ***Fe*** | Feature | iron | Continuous | - |
| ***Type_of_glass*** | **Target** | a number representing a different type of glass | Continuous | 1 - 7 |

---

## Target Variable

- **Name**: Type_of_glass
- **Type**: Categorical
- **Values**: [1, 2, 3, 5, 6, 7]

---

## Dataset Details

- **Has missing values?**: no
- **Number of Instances**: 214 instances
- **Number of Features**: 9
- **Class Distribution**:
  - 1: 70 instances
  - 2: 76 instances
  - 3: 17 instances
  - 5: 13 instances
  - 6: 9 instances
  - 7: 29 instances

---

## File Structure

- `glass.csv`: Main dataset file.
- `README.md`: Documentation file (this file).
- `configuration.json`: Configuration file containing the istructions for DatasetPreprocessor.
- `results_images/`: A folder containing the charts of the metrics analyzed.
- `results_metrics.json`: The json file containing the results of the models for this dataset.

---

## Sample Data

An example of how the dataset is structured:

| Id | RI | Na | Mg | Al | Si | K | Ca | Ba | Fe | class |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 70 | 1.52300 | 13.31 | 3.58 | 0.82 | 71.99 | 0.12 | 10.17 | 0.00 | 0.03 | 1 |
| 71 | 1.51574 | 14.86 | 3.67 | 1.74 | 71.87 | 0.16 | 7.36 | 0.00 | 0.12 | 2 |
| 189 | 1.52247 | 14.86 | 2.20 | 2.06 | 70.26 | 0.76 | 9.76 | 0.00 | 0.00 | 7 |

---

## Performance Metrics

| Classifier | Accuracy | Balanced Accuracy | Micro F1 | Macro F1 | Training Time | Prediction Time | Total Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ***Random Forest*** | ***80.0%*** | ***80.8%*** | ***80.0%*** | 76.7% | 0.023s | 0.001s | 0.024s |
| Extra Trees | 76.9% | 67.4% | 76.9% | 68.7% | 0.018s | 0.001s | 0.020s |
| ***XGBoost*** | 78.5% | 79.8% | 78.5% | ***77.5%*** | 0.036s | 0.001s | 0.037s |
| AdaBoost | 49.2% | 37.0% | 49.2% | 35.2% | 0.033s | 0.003s | 0.035s |
| Gradient Boosting | 66.2% | 65.5% | 66.2% | 64.8% | 0.120s | 0.001s | 0.120s |
| SimilarityForest[cityblock] | 41.5% | 19.0% | 41.5% | 18.0% | 0.012s | 0.005s | 0.017s |
| SimilarityForest[cosine] | 60.0% | 61.6% | 60.0% | 56.5% | 0.023s | 0.003s | 0.025s |
| SimilarityForest[euclidean] | 63.1% | 52.2% | 63.1% | 48.1% | 0.023s | 0.002s | 0.025s |
| SimilarityForest[braycurtis] | 55.4% | 62.2% | 55.4% | 54.8% | 0.012s | 0.002s | 0.014s |
| SimilarityForest[canberra] | 60.0% | 47.0% | 60.0% | 46.3% | 0.012s | 0.002s | 0.014s |
| SimilarityForest[chebyshev] | 61.5% | 48.3% | 61.5% | 43.3% | 0.012s | 0.002s | 0.014s |
| SimilarityForest[correlation] | 60.0% | 61.6% | 60.0% | 56.5% | 0.012s | 0.002s | 0.014s |
| SimilarityForest[hamming] | 53.8% | 47.5% | 53.8% | 44.4% | 0.022s | 0.003s | 0.025s |

---

## Acknowledgments

German, B. (1987). Glass Identification [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5WW2P.

