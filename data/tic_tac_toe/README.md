# Tic-Tac-Toe

**Description**:

This database encodes the complete set of possible board configurations at the end of tic-tac-toe games, where "x" is assumed to have played first.  The target concept is "win for x" (i.e., true when "x" has one of 8 possible ways to create a "three-in-a-row").

---

## Table of Contents
- [Tic-Tac-Toe](#tic-tac-toe)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Tic-Tac-Toe Endgame](https://archive.ics.uci.edu/dataset/101/tic+tac+toe+endgame)

- **Domain**: Games

- **Format**: CSV

---

## Variables

| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***top-left-square*** | Feature | Value of the top-left square | Categorical | x, o, b |
| ***top-middle-square*** | Feature | Value of the top-middle square | Categorical | x, o, b |
| ***top-right-square*** | Feature | Value of the top-right square | Categorical | x, o, b |
| ***middle-left-square*** | Feature | Value of the middle-left square | Categorical | x, o, b |
| ***middle-middle-square*** | Feature | Value of the middle-middle square | Categorical | x, o, b |
| ***middle-right-square*** | Feature | Value of the middle-right square | Categorical | x, o, b |
| ***bottom-left-square*** | Feature | Value of the bottom-left square | Categorical | x, o, b |
| ***bottom-middle-square*** | Feature | Value of the bottom-middle square | Categorical | x, o, b |
| ***bottom-right-square*** | Feature | Value of the bottom-right square | Categorical | x, o, b |
| ***class*** | **Target** | Whether the configuration is a win for the player about to move or not | Categorical | positive, negative |

---

## Target Variable

- **Name**: *class*
- **Type**: Categorical
- **Values**:
  - positive = Win for the player about to move
  - negative = Not a win for the player about to move

---

## Dataset Details

- **Has missing values?**: no
- **Number of Instances**: 958 instances
- **Number of Features**: 9
- **Class Distribution**:
  - positive = 626 instances
  - negative = 332 instances

---

## File Structure

- `tic_tac_toe.csv`: Main dataset file.
- `README.md`: Documentation file (this file).
- `configuration.json`: Configuration file containing the instructions for DatasetPreprocessor.
- `results_images/`: A folder containing the charts of the metrics analyzed.
- `results_metrics.json`: The json file containing the results of the models for this dataset.

---

## Sample Data

An example of how the dataset is structured:

| top-left-square | top-middle-square | top-right-square | middle-left-square | middle-middle-square | middle-right-square | bottom-left-square | bottom-middle-square | bottom-right-square | class |
|---|---|---|---|---|---|---|---|---|---|
| b | b | b | o | b | o | x | x | x | positive |
| b | b | b | b | o | o | x | x | x | positive |
| x | x | o | x | x | o | o | b | o | negative |

---

## Performance Metrics

| Classifier | Accuracy | Balanced Accuracy | Micro F1 | Macro F1 | Training Time | Prediction Time | Total Time |
|  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |
| Random Forest | 97.2% | 96.6% | 97.2% | 96.9% | 0.031s | 0.002s | 0.033s |
| Extra Trees | 98.3% | 98.2% | 98.3% | 98.1% | 0.025s | 0.002s | 0.026s |
| XGBoost | 98.6% | 98.2% | 98.6% | 98.4% | 0.016s | 0.001s | 0.017s |
| AdaBoost | 76.7% | 69.5% | 76.7% | 70.9% | 0.037s | 0.003s | 0.041s |
| Gradient Boosting | 86.1% | 79.7% | 86.1% | 82.4% | 0.026s | 0.000s | 0.026s |
| SimilarityForest[cityblock] | 90.6% | 89.6% | 90.6% | 89.5% | 0.093s | 0.003s | 0.095s |
| SimilarityForest[cosine] | 92.7% | 91.9% | 92.7% | 91.8% | 0.022s | 0.003s | 0.025s |
| SimilarityForest[euclidean] | 87.2% | 86.2% | 87.2% | 85.7% | 0.023s | 0.003s | 0.026s |
| SimilarityForest[braycurtis] | 92.7% | 91.9% | 92.7% | 91.8% | 0.022s | 0.003s | 0.025s |
| SimilarityForest[canberra] | 90.6% | 89.6% | 90.6% | 89.5% | 0.023s | 0.003s | 0.026s |
| SimilarityForest[chebyshev] | 94.4% | 93.0% | 94.4% | 93.6% | 0.022s | 0.003s | 0.025s |
| SimilarityForest[correlation] | 89.6% | 88.3% | 89.6% | 88.3% | 0.022s | 0.003s | 0.025s |
| SimilarityForest[hamming] | 87.5% | 87.2% | 87.5% | 86.3% | 0.023s | 0.003s | 0.025s |

---

## Acknowledgments

Aha, D. (1991). Tic-Tac-Toe Endgame [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5688J.