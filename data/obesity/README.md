# Obesity

**Description**:

This dataset include data for the estimation of obesity levels in individuals from the countries of Mexico, Peru and Colombia, based on their eating habits and physical condition.

---

## Table of Contents
- [Obesity](#obesity)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Estimation of Obesity Levels Based On Eating Habits and Physical Condition](https://archive.ics.uci.edu/dataset/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition)

- **Domain**: Health and Medicine

- **Format**: CSV

---

## Variables

| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***Gender*** | Feature | Gender of the individual | Categorical | Male, Female |
| ***Age*** | Feature | Age of the individual | Integer | - |
| ***Height*** | Feature | Height of the individual | Continuous | - |
| ***Weight*** | Feature | Weight of the individual | Continuous | - |
| ***family_history_with_overweight*** | Feature | Family history of overweight | Categorical | yes, no |
| ***FAVC*** | Feature | Frequent consumption of high caloric food | Categorical | yes, no |
| ***FCVC*** | Feature | Frequency of consumption of vegetables (never, sometimes, always) | Integer | {1, 2, 3}        |
| ***NCP*** | Feature | Number of main meals (Between 1 and 2, Three, More than three) | Integer | {1, 2, 3} |
| ***CAEC*** | Feature | Consumption of food between meals | Categorical | no, Sometimes, Frequently, Always |
| ***SMOKE*** | Feature | Smoking habit | Categorical | yes, no |
| ***CH2O*** | Feature | Daily water intake (less than a liter, Between 1 and 2 L, More than 2 L) | Integer | 1, 2, 3 |
| ***SCC*** | Feature | Calorie consumption monitoring | Categorical | yes, no |
| ***FAF*** | Feature | Physical activity frequency (I do not have, 1 or 2 days, 2 or 4 days, 4 or 5 days) | Integer | {0, 1, 2, 3} |
| ***TUE*** | Feature | Time using technology devices (0–2 hours, 3–5 hours, More than 5 hours) | Integer | 0, 1, 2 |
| ***CALC*** | Feature | Consumption of alcohol | Categorical | no, Sometimes, Frequently, Always |
| ***MTRANS*** | Feature | Transportation used | Categorical | Automobile, Motorbike, Bike, Public_Transportation, Walking |
| ***NObeyesdad*** | **Target** | Obesity level | Categorical | Insufficient_Weight, Normal_Weight, Overweight_Level_I, Overweight_Level_II, Obesity_Type_I, Obesity_Type_II, Obesity_Type_III |

---

## Target Variable

- **Name**: *NObeyesdad*
- **Type**: Categorical
- **Values**:
  - Insufficient_Weight
  - Normal_Weight
  - Overweight_Level_I
  - Overweight_Level_II
  - Obesity_Type_I
  - Obesity_Type_II
  - Obesity_Type_III

---

## Dataset Details

- **Has missing values?**: no
- **Number of Instances**: 2111 instances
- **Number of Features**: 16
- **Class Distribution**:
  - Insufficient_Weight = 272 instances
  - Normal_Weight = 287 instances
  - Overweight_Level_I = 290 instances
  - Overweight_Level_II = 290 instances
  - Obesity_Type_I = 351 instances
  - Obesity_Type_II = 297 instances
  - Obesity_Type_III = 324 instances

---

## File Structure

- `obesity.csv`: Main dataset file.
- `README.md`: Documentation file (this file).
- `configuration.json`: Configuration file containing the instructions for DatasetPreprocessor.
- `results_images/`: A folder containing the charts of the metrics analyzed.
- `results_metrics.json`: The json file containing the results of the models for this datase

---

## Sample Data

An example of how the dataset is structured:

| Gender | Age | Height | Weight | family_history_with_overweight | FAVC | FCVC | NCP | CAEC | SMOKE | CH2O | SCC | FAF | TUE | CALC | MTRANS | ***NObeyesdad*** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Male | 23 | 1.8 | 77 | yes | no | 2 | 3 | Sometimes | no | 2 | no | 2 | 1 | Frequently | Public_Transportation | *Normal_Weight* |
| Male | 27 | 1.8 | 87 | no | no | 3 | 3 | Sometimes | no | 2 | no | 2 | 0 | Frequently | Walking | *Overweight_Level_I* |
| Male | 22 | 1.78 | 89.8 | no | no | 2 | 1 | Sometimes | no | 2 | no | 0 | 0 | Sometimes | Public_Transportation | *Overweight_Level_II* |

---

## Performance Metrics

| Classifier | Accuracy | Balanced Accuracy | Micro F1 | Macro F1 | Training Time | Prediction Time | Total Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Random Forest | 92.0% | 91.8% | 92.0% | 92.0% | 0.055s | 0.002s | 0.058s |
| Extra Trees | 89.3% | 89.4% | 89.3% | 89.4% | 0.040s | 0.003s | 0.044s |
| ***XGBoost*** | ***97.2%*** | ***97.2%*** | ***97.2%*** | ***97.3%*** | 0.083s | 0.001s | 0.085s |
| AdaBoost | 48.4% | 51.6% | 48.4% | 43.9% | 0.073s | 0.004s | 0.077s |
| Gradient Boosting | 93.4% | 93.6% | 93.4% | 93.5% | 0.688s | 0.003s | 0.691s |
| SimilarityForest[cityblock] | 91.6% | 91.9% | 91.6% | 91.6% | 0.099s | 0.004s | 0.103s |
| SimilarityForest[cosine] | 87.1% | 87.0% | 87.1% | 87.1% | 0.033s | 0.004s | 0.037s |
| SimilarityForest[euclidean] | 87.9% | 88.3% | 87.9% | 88.0% | 0.022s | 0.004s | 0.026s |
| SimilarityForest[braycurtis] | 90.7% | 91.1% | 90.7% | 90.7% | 0.033s | 0.004s | 0.036s |
| SimilarityForest[canberra] | 90.2% | 90.5% | 90.2% | 90.3% | 0.033s | 0.004s | 0.037s |
| SimilarityForest[chebyshev] | 89.3% | 89.6% | 89.3% | 89.3% | 0.023s | 0.004s | 0.026s |
| SimilarityForest[correlation] | 87.4% | 87.4% | 87.4% | 87.5% | 0.033s | 0.003s | 0.036s |
| SimilarityForest[hamming] | 94.5% | 94.7% | 94.5% | 94.6% | 0.033s | 0.003s | 0.036s |

---

## Acknowledgments

Estimation of Obesity Levels Based On Eating Habits and Physical Condition [Dataset]. (2019). UCI Machine Learning Repository. https://doi.org/10.24432/C5H31Z.
