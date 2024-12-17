# Shuttle

**Description**:

This dataset contains information about the shuttle's flight data. The goal is to classify the different states of the shuttle based on various features.
The shuttle dataset contains 9 attributes all of which are numerical. Approximately 80% of the data belongs to class 1


---

## Table of Contents
- [Shuttle](#shuttle)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Statlog (Shuttle)](https://archive.ics.uci.edu/dataset/148/statlog+shuttle)

- **Domain**: Physics and Chemistry

- **Format**: CSV

---

## Variables

| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***f1*** | Feature | Feature 1 | Continuous | - |
| ***f2*** | Feature | Feature 2 | Continuous | - |
| ***f3*** | Feature | Feature 3 | Continuous | - |
| ***f4*** | Feature | Feature 4 | Continuous | - |
| ***f5*** | Feature | Feature 5 | Continuous | - |
| ***f6*** | Feature | Feature 6 | Continuous | - |
| ***f7*** | Feature | Feature 7 | Continuous | - |
| ***f8*** | Feature | Feature 8 | Continuous | - |
| ***f9*** | Feature | Feature 9 | Continuous | - |
| ***class*** | **Target** | Shuttle state | Categorical | 1, 2, 3, 4, 5, 6, 7 |

---

## Target Variable

- **Name**: *class*
- **Type**: Categorical
- **Values**:
  - 1 = Rad Flow
  - 2 = Fpv Close
  - 3 = Fpv Open
  - 4 = High
  - 5 = Bypass
  - 6 = Bpv Close
  - 7 = Bpv Open

---

## Dataset Details

- **Has missing values?**: no
- **Number of Instances**: 58000 instances
- **Number of Features**: 9
- **Class Distribution**:
  - 1 = Rad Flow = 45586 instances
  - 2 = Fpv Close = 50 instances
  - 3 = Fpv Open = 171 instances
  - 4 = High = 8903 instances
  - 5 = Bypass = 3267 instances
  - 6 = Bpv Close = 10 instances
  - 7 = Bpv Open = 13 instances

---

## File Structure

- `shuttle.csv`: Main dataset file.
- `README.md`: Documentation file (this file).
- `configuration.json`: Configuration file containing the instructions for DatasetPreprocessor.
- `results_images/`: A folder containing the charts of the metrics analyzed.
- `results_metrics.json`: The json file containing the results of the models for this dataset.

---

## Sample Data

An example of how the dataset is structured:

| f1 | f2 | f3 | f4 | f5 | f6 | f7 | f8 | f9 | class |
|----|----|----|----|----|----|----|----|----|-------|
| 55 | 0 | 96 | 0 | 46 | 23 | 41 | 50 | 8 | **4** |
| 42 | 0 | 81 | -2 | 42 | -4 | 39 | 39 | 0 | **1** |
| 79 | 0 | 83 | 0 | -40 | 3 | 4 | 125 | 120 | **5** |

---

## Performance Metrics

| Classifier | Accuracy | Balanced Accuracy | Micro F1 | Macro F1 | Training Time | Prediction Time | Total Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Random Forest | 100.0% | 85.2% | 100.0% | 89.4% | 0.384s | 0.018s | 0.401s |
| Extra Trees | 100.0% | 98.7% | 100.0% | 99.2% | 0.249s | 0.031s | 0.280s |
| XGBoost | 100.0% | 99.5% | 100.0% | 99.7% | 0.111s | 0.004s | 0.115s |
| AdaBoost | 99.4% | 42.7% | 99.4% | 42.7% | 0.397s | 0.021s | 0.418s |
| Gradient Boosting | 99.9% | 98.9% | 99.9% | 99.3% | 5.207s | 0.032s | 5.239s |
| SimilarityForest[cityblock] | 99.9% | 68.8% | 99.9% | 68.5% | 0.340s | 0.040s | 0.380s |
| SimilarityForest[cosine] | 99.9% | 85.1% | 99.9% | 83.6% | 0.290s | 0.032s | 0.322s |
| SimilarityForest[euclidean] | 99.9% | 68.8% | 99.9% | 67.9% | 0.333s | 0.041s | 0.374s |
| SimilarityForest[braycurtis] | 99.9% | 98.4% | 99.9% | 97.1% | 0.365s | 0.034s | 0.399s |
| SimilarityForest[canberra] | 100.0% | 99.2% | 100.0% | 99.5% | 0.321s | 0.034s | 0.354s |
| SimilarityForest[chebyshev] | 99.9% | 66.8% | 99.9% | 67.9% | 0.281s | 0.042s | 0.323s |
| SimilarityForest[correlation] | 100.0% | 89.9% | 100.0% | 91.6% | 0.406s | 0.034s | 0.440s |
| SimilarityForest[hamming] | 99.9% | 88.4% | 99.9% | 89.4% | 0.282s | 0.031s | 0.313s |

---

## Acknowledgments

Statlog (Shuttle) [Dataset].  UCI Machine Learning Repository. https://doi.org/10.24432/C5WS31.