# Heart_failure

**Description**:

This dataset contains the medical records of 299 patients who had heart failure, collected during their follow-up period, where each patient profile has 13 clinical features.

---

## Table of Contents
- [Heart\_failure](#heart_failure)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Heart Failure Clinical Records](https://archive.ics.uci.edu/dataset/519/heart+failure+clinical+records)

- **Domain**: Health and Medicine

- **Format**: CSV

---

## Variables

List the features (columns) in the dataset along with descriptions, data types, and possible values. Example:


| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***age*** | Feature | age of the patient | Integer | - |
| ***anaemia*** | Feature | decrease of red blood cells or hemoglobin | Binary | - |
| ***creatinine_phosphokinase*** | Feature | level of the CPK enzyme in the blood | Integer | - |
| ***diabetes*** | Feature | if the patient has diabetes | Binary | - |
| ***ejection_fraction*** | Feature | percentage of blood leaving the heart at each contraction | Integer | - |
| ***high_blood_pressure*** | Feature | if the patient has hypertension | Binary | - |
| ***platelets*** | Feature | platelets in the blood | Continuous | - |
| ***serum_creatinine*** | Feature | level of serum creatinine in the blood | Continuous | - |
| ***serum_sodium*** | Feature | level of serum sodium in the blood | Integer | - |
| ***sex*** | Feature | woman or man | Binary | - |
| ***smoking*** | Feature | if the patient smokes or not | Binary | - |
| ***time*** | Feature | follow-up period | Integer | - |
| ***death_event*** | **Target** | if the patient died during the follow-up period | Binary | - |

---

## Target Variable

- **Name**: *death_event*
- **Type**: Binary
- **Values**:
  - 0 if the patient survived in the follow-up period
  - 1 if the patient died in the follow-up period
---

## Dataset Details

- **Has missing values?**: no
- **Number of Instances**: 299 instances
- **Number of Features**: 12
- **Class Distribution**:
  - 0 if the patient survived = 203 instances
  - 1 if the patient died = 96 instances

---

## File Structure

- `heart_failure.csv`: Main dataset file.
- `README.md`: Documentation file (this file).
- `configuration.json`: Configuration file containing the istructions for DatasetPreprocessor.

---

## Sample Data

An example of how the dataset is structured:

| age | anaemia | creatinine_phosphokinase | diabetes | ejection_fraction | high_blood_pressure | platelets | serum_creatinine | serum_sodium | sex | smoking | time | death_event |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 70 | 0 | 571 | 1 | 45 | 1 | 185000 | 1.2 | 139 | 1 | 1 | 33 | 1 |
| 72 | 0 | 127 | 1 | 50 | 1 | 218000 | 1 | 134 | 1 | 0 | 33 | 0 |
| 60 | 1 | 588 | 1 | 60 | 0 | 194000 | 1.1 | 142 | 0 | 0 | 33 | 1 |

---

## Performance Metrics

| Classifier | Accuracy | Balanced Accuracy | Micro F1 | Macro F1 | Training Time | Prediction Time | Total Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Random Forest | 81.1% | 76.9% | 81.1% | 78.2% | 0.023s | 0.001s | 0.024s |
| ***Extra Trees*** | ***83.3%*** | ***80.1%*** | ***83.3%*** | ***81.1%*** | 0.018s | 0.001s | 0.019s |
| XGBoost | 80.0% | 75.4% | 80.0% | 76.7% | 0.015s | 0.001s | 0.016s |
| AdaBoost | 76.7% | 72.1% | 76.7% | 73.0% | 0.033s | 0.003s | 0.036s |
| Gradient Boosting | 77.8% | 73.0% | 77.8% | 74.1% | 0.023s | 0.000s | 0.023s |
| SimilarityForest[cityblock] | 72.2% | 67.9% | 72.2% | 68.5% | 0.012s | 0.002s | 0.014s |
| SimilarityForest[cosine] | 77.8% | 72.3% | 77.8% | 73.5% | 0.022s | 0.003s | 0.025s |
| SimilarityForest[euclidean] | 65.6% | 56.5% | 65.6% | 55.4% | 0.035s | 0.005s | 0.040s |
| SimilarityForest[braycurtis] | 72.2% | 70.0% | 72.2% | 69.9% | 0.025s | 0.002s | 0.027s |
| SimilarityForest[canberra] | 73.3% | 70.9% | 73.3% | 70.9% | 0.012s | 0.002s | 0.015s |
| SimilarityForest[chebyshev] | 65.6% | 56.5% | 65.6% | 55.4% | 0.012s | 0.002s | 0.014s |
| SimilarityForest[correlation] | 77.8% | 72.3% | 77.8% | 73.5% | 0.022s | 0.002s | 0.025s |
| SimilarityForest[hamming] | 74.4% | 73.2% | 74.4% | 72.7% | 0.022s | 0.002s | 0.025s |

---

## Acknowledgments

Heart Failure Clinical Records [Dataset]. (2020). UCI Machine Learning Repository. https://doi.org/10.24432/C5Z89R.

Chicco, D., Jurman, G. Machine learning can predict survival of patients with heart failure from serum creatinine and ejection fraction alone. BMC Med Inform Decis Mak 20, 16 (2020). https://doi.org/10.1186/s12911-020-1023-5

