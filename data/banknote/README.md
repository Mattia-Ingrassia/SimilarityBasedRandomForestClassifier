# Banknote

**Description**:

Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.

---

## Table of Contents
- [Banknote](#banknote)
  - [Table of Contents](#table-of-contents)
  - [Dataset Overview](#dataset-overview)
  - [Variables](#variables)
  - [Target Variable](#target-variable)
  - [Dataset Details](#dataset-details)
  - [s](#s)
  - [File Structure](#file-structure)
  - [Sample Data](#sample-data)
  - [Performance Metrics](#performance-metrics)
  - [Acknowledgments](#acknowledgments)

---

## Dataset Overview

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Banknote Authentication](https://archive.ics.uci.edu/dataset/267/banknote+authentication).

- **Domain**: Computer science

- **Format**: CSV

---

## Variables

| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***variance*** | Feature | variance of Wavelet Transformed image | Continuous | - |
| ***skewness*** | Feature | skewness of Wavelet Transformed image | Continuous | - |
| ***curtosis*** | Feature | curtosis of Wavelet Transformed image | Continuous | - |
| ***entropy*** | Feature | entropy of image | Continuous | - |
| ***class*** | **Target** | is the banknote genuine (0) or not (1) | Binary | 0, 1 |


---

## Target Variable

- **Name**: class
- **Type**: Binary
- **Values**: 0 if the banknote is genuine, 1 otherwise

---

## Dataset Details

- **Has missing values?**: no
- **Number of Instances**: 1372 instances
- **Number of Features**: 4
- **Class Distribution**:
  - (0) : 762 instances
  - (1) : 610 instances
s
---

## File Structure

- `banknote.csv`: Main dataset file.
- `README.md`: Documentation file (this file).
- `configuration.json`: Configuration file containing the istructions for DatasetPreprocessor.
- `results_images/`: A folder containing the charts of the metrics analyzed.
- `results_metrics.json`: The json file containing the results of the models for this dataset.

---

## Sample Data

An example of how the dataset is structured:

| variance | skewness | curtosis | entropy | class |
| --- | --- | --- | --- | --- |
|3.2414 | 0.40971 | 1.4015 | 1.1952 | 0|
|2.2504 | 3.5757 | 0.35273 | 0.2836 | 0|
|-1.3971 | 3.3191 | -1.3927 | -1.9948 | 1|


---

## Performance Metrics

| Classifier | Accuracy | Balanced Accuracy | Micro F1 | Macro F1 | Training Time | Prediction Time | Total Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ***Random Forest*** | ***99.3%*** | ***99.3%*** | ***99.3%*** | ***99.3%*** | 0.040s | 0.001s | 0.041s |
| Extra Trees | 98.5% | 98.7% | 98.5% | 98.5% | 0.020s | 0.002s | 0.022s |
| XGBoost | 99.0% | 99.0% | 99.0% | 99.0% | 0.014s | 0.001s | 0.015s |
| AdaBoost | 97.1% | 97.3% | 97.1% | 97.1% | 0.050s | 0.003s | 0.053s |
| Gradient Boosting | 97.8% | 97.9% | 97.8% | 97.8% | 0.063s | 0.001s | 0.064s |
| SimilarityForest[cityblock] | 98.1% | 98.1% | 98.1% | 98.0% | 0.097s | 0.003s | 0.100s |
| SimilarityForest[cosine] | 97.1% | 97.2% | 97.1% | 97.1% | 0.022s | 0.003s | 0.025s |
| SimilarityForest[euclidean] | 98.5% | 98.5% | 98.5% | 98.5% | 0.022s | 0.003s | 0.025s |
| SimilarityForest[braycurtis] | 98.5% | 98.5% | 98.5% | 98.5% | 0.023s | 0.003s | 0.026s |
| SimilarityForest[canberra] | 98.5% | 98.6% | 98.5% | 98.5% | 0.022s | 0.003s | 0.025s |
| SimilarityForest[chebyshev] | 98.5% | 98.7% | 98.5% | 98.5% | 0.022s | 0.003s | 0.025s |
| SimilarityForest[correlation] | 97.1% | 97.2% | 97.1% | 97.1% | 0.023s | 0.003s | 0.025s |
| SimilarityForest[hamming] | 97.3% | 97.3% | 97.3% | 97.3% | 0.022s | 0.004s | 0.027s |

---

## Acknowledgments

Lohweg, V. (2012). Banknote Authentication [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C55P57.

