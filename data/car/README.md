# Car

**Description**:

Derived from simple hierarchical decision model, this car evaluation database may be useful for testing constructive induction and structure discovery methods.

---

## Table of Contents
- [Car](#car)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Car Evaluation](https://archive.ics.uci.edu/dataset/19/car+evaluation)

- **Domain**: Other

- **Format**: CSV

---

## Variables

| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***buying*** | Feature | Buying price | Categorical | vhigh, high, med, low |
| ***maint*** | Feature | Price of the maintenance | Categorical | vhigh, high, med, low |
| ***doors***| Feature | Number of doors | Categorical | 2, 3, 4, 5more |
| ***persons*** | Feature | Capacity in terms of persons to carry | Categorical | 2, 4, more |
| ***lug_boot*** | Feature | The size of luggage boot | Categorical | small, med, big |
| ***safety*** | Feature | Estimated safety of the car | Categorical | low, med, high |
| ***class***| **Target** | Evaluation Level (unacc = unacceptable, acc = acceptable, good = good, vgood = very good) | Categorical | unacc, acc, good, vgood |

---

## Target Variable

- **Name**: *class*
- **Type**: Categorical
- **Values**:
  - unacc = unacceptable
  - acc = acceptable
  - good = good
  - vgood = very good

---

## Dataset Details

- **Has missing values?**: no
- **Number of Instances**: 1728 instances
- **Number of Features**: 6
- **Class Distribution**:
  - unacc = 1210 instances
  - acc = 384 instances
  - good = 69 instances
  - vgood = 65 instances

---

## File Structure

- `car.csv`: Main dataset file.
- `README.md`: Documentation file (this file).
- `configuration.json`: Configuration file containing the istructions for DatasetPreprocessor.
- `results_images/`: A folder containing the charts of the metrics analyzed.
- `results_metrics.json`: The json file containing the results of the models for this dataset.

---

## Sample Data

An example of how the dataset is structured:

| buying | maint | doors | persons | lug_boot | safety | class |
| --- | --- | --- | --- | --- | --- | --- |
| low | med | 5more | more | big | med | good |
| low | med | 5more | more | big | high | vgood |
| low | low | 2 | 2 | small | low | unacc |

---

## Performance Metrics

| Classifier | Accuracy | Balanced Accuracy | Micro F1 | Macro F1 | Training Time | Prediction Time | Total Time |
|---|---|---|---|---|---|---|---|
| Random Forest | 93.1% | 77.4% | 93.1% | 80.6% | 0.031s | 0.002s | 0.033s |
| Extra Trees | 94.6% | 82.8% | 94.6% | 85.5% | 0.027s | 0.002s | 0.029s |
| XGBoost | 95.4% | 84.0% | 95.4% | 85.4% | 0.052s | 0.001s | 0.053s |
| AdaBoost | 82.1% | 45.8% | 82.1% | 40.4% | 0.046s | 0.004s | 0.050s |
| Gradient Boosting | 88.1% | 56.7% | 88.1% | 57.9% | 0.127s | 0.002s | 0.129s |
| SimilarityForest[cityblock] | 93.8% | 86.4% | 93.8% | 87.9% | 0.098s | 0.003s | 0.101s |
| ***SimilarityForest[cosine]*** | ***96.3%*** | ***88.5%*** | ***96.3%*** | ***89.0%*** | 0.023s | 0.004s | 0.027s |
| SimilarityForest[euclidean] | 94.0% | 83.5% | 94.0% | 84.8% | 0.022s | 0.003s | 0.025s |
| ***SimilarityForest[braycurtis]*** | ***96.3%*** | ***88.5%*** | ***96.3%*** | ***89.0%*** | 0.023s | 0.003s | 0.026s |
| SimilarityForest[canberra] | 93.8% | 86.4% | 93.8% | 87.9% | 0.023s | 0.004s | 0.026s |
| SimilarityForest[chebyshev] | 95.8% | 85.4% | 95.8% | 87.2% | 0.022s | 0.004s | 0.026s |
| SimilarityForest[correlation] | 94.8% | 86.1% | 94.8% | 87.2% | 0.023s | 0.003s | 0.026s |
| SimilarityForest[hamming] | 94.4% | 84.6% | 94.4% | 87.1% | 0.023s | 0.003s | 0.027s |

---

## Acknowledgments

Bohanec, M. (1988). Car Evaluation [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5JP48.

