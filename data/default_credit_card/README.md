# Default_credit_card

**Description**:

This research aimed at the case of customers' default payments in Taiwan and compares the predictive accuracy of probability of default among six data mining methods.

---

## Table of Contents
- [Default\_credit\_card](#default_credit_card)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Default of Credit Card Clients](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients)

- **Domain**: Business

- **Format**: CSV

---

## Variables

List the features (columns) in the dataset along with descriptions, data types, and possible values. Example:


| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***ID*** | ID | should be ignored | Integer | - |
| ***LIMIT_BAL*** | Feature | Amount of the given credit (NT dollar) | Integer | - |
| ***SEX*** | Feature | Gender (1 = male; 2 = female) | Integer | 1 - 2 |
| ***EDUCATION*** | Feature | Education (1 = graduate school; 2 = university; 3 = high school; 4 = others) | Integer | 1 - 4 |
| ***MARRIAGE*** | Feature | Marital status (1 = married; 2 = single; 3 = others) | Integer | 1 - 3 |
| ***AGE*** | Feature | Age (years) | Integer | - |
| ***PAY_0*** | Feature | repayment status in September, 2005 (-1 = pay duly; 1-8 = payment delay for 1-8 months; 9 = payment delay for 9+ months ) | Integer | -1 - 9 |
| ***PAY_2*** | Feature | repayment status in August, 2005 (-1 = pay duly; 1-8 = payment delay for 1-8 months; 9 = payment delay for 9+ months ) | Integer | -1 - 9 |
| ***PAY_3*** | Feature | repayment status in July, 2005 (-1 = pay duly; 1-8 = payment delay for 1-8 months; 9 = payment delay for 9+ months ) | Integer | -1 - 9 |
| ***PAY_4*** | Feature | repayment status in June, 2005 (-1 = pay duly; 1-8 = payment delay for 1-8 months; 9 = payment delay for 9+ months ) | Integer | -1 - 9 |
| ***PAY_5*** | Feature | repayment status in May, 2005 (-1 = pay duly; 1-8 = payment delay for 1-8 months; 9 = payment delay for 9+ months ) | Integer | -1 - 9 |
| ***PAY_6*** | Feature | repayment status in April, 2005 (-1 = pay duly; 1-8 = payment delay for 1-8 months; 9 = payment delay for 9+ months ) | Integer | -1 - 9 |
| ***BILL_AMT1*** | Feature | amount of bill statement in September, 2005 | Integer | - |
| ***BILL_AMT2*** | Feature | amount of bill statement in August, 2005 | Integer | - |
| ***BILL_AMT3*** | Feature | amount of bill statement in July, 2005 | Integer | - |
| ***BILL_AMT4*** | Feature | amount of bill statement in June, 2005 | Integer | - |
| ***BILL_AMT5*** | Feature | amount of bill statement in May, 2005 | Integer | - |
| ***BILL_AMT6*** | Feature | amount of bill statement in April, 2005 | Integer | - |
| ***PAY_AMT1*** | Feature | amount paid in September, 2005 | Integer | - |
| ***PAY_AMT2*** | Feature | amount paid in August, 2005 | Integer | - |
| ***PAY_AMT3*** | Feature | amount paid in July, 2005 | Integer | - |
| ***PAY_AMT4*** | Feature | amount paid in June, 2005 | Integer | - |
| ***PAY_AMT5*** | Feature | amount paid in May, 2005 | Integer | - |
| ***PAY_AMT6*** | Feature | amount paid in April, 2005 | Integer | - |
| ***default_payment_next_month*** | **Target** | default payment (Yes = 1, No = 0) | Categorical | 0 - 1 |

---

## Target Variable

- **Name**: *default_payment_next_month*
- **Type**: Categorical
- **Values**: Yes = 1, No = 0

---

## Dataset Details

- **Has missing values?**: no
- **Number of Instances**: 30000 instances
- **Number of Features**: 23
- **Class Distribution**:
  - Yes = 1 = 6636 instances
  - No = 0 = 23364 instances
---

## File Structure

- `default_credit_card.csv`: Main dataset file.
- `README.md`: Documentation file (this file).
- `configuration.json`: Configuration file containing the istructions for DatasetPreprocessor.
- `results_images/`: A folder containing the charts of the metrics analyzed.
- `results_metrics.json`: The json file containing the results of the models for this dataset.

---

## Sample Data

An example of how the dataset is structured:

| ID | LIMIT_BAL | SEX | EDUCATION | MARRIAGE | AGE | PAY_0 | PAY_2 | PAY_3 | PAY_4 | PAY_5 | PAY_6 | BILL_AMT1 | BILL_AMT2 | BILL_AMT3 | BILL_AMT4 | BILL_AMT5 | BILL_AMT6 | PAY_AMT1 | PAY_AMT2 | PAY_AMT3 | PAY_AMT4 | PAY_AMT5 | PAY_AMT6 | default_payment_next_month |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 20000 | 2 | 2 | 1 | 24 | 2 | 2 | -1 | -1 | -2 | -2 | 3913 | 3102 | 689 | 0 | 0 | 0 | 0 | 689 | 0 | 0 | 0 | 0 | 1 |
| 2 | 120000 | 2 | 2 | 2 | 26 | -1 | 2 | 0 | 0 | 0 | 2 | 2682 | 1725 | 2682 | 3272 | 3455 | 3261 | 0 | 1000 | 1000 | 1000 | 0 | 2000 | 1 |
| 3 | 90000 | 2 | 2 | 2 | 34 | 0 | 0 | 0 | 0 | 0 | 0 | 29239 | 14027 | 13559 | 14331 | 14948 | 15549 | 1518 | 1500 | 1000 | 1000 | 1000 | 5000 | 0 |

---

## Performance Metrics

| Classifier | Accuracy | Balanced Accuracy | Micro F1 | Macro F1 | Training Time | Prediction Time | Total Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Random Forest | 81.1% | 65.3% | 81.1% | 67.4% | 1.447s | 0.034s | 1.481s |
| Extra Trees | 80.6% | 64.7% | 80.6% | 66.7% | 0.489s | 0.049s | 0.538s |
| ***XGBoost*** | 82.1% | ***65.6%*** | 82.1% | ***68.2%*** | 0.048s | 0.002s | 0.049s |
| AdaBoost | 82.1% | 64.3% | 82.1% | 66.9% | 0.824s | 0.012s | 0.836s |
| ***Gradient Boosting*** | ***82.4%*** | 65.2% | ***82.4%*** | 67.9% | 2.100s | 0.004s | 2.105s |
| SimilarityForest[cityblock] | 71.6% | 60.1% | 71.6% | 59.9% | 0.265s | 0.028s | 0.293s |
| SimilarityForest[cosine] | 72.1% | 60.8% | 72.1% | 60.5% | 0.987s | 0.043s | 1.029s |
| SimilarityForest[euclidean] | 72.4% | 61.3% | 72.4% | 61.0% | 0.289s | 0.030s | 0.318s |
| SimilarityForest[braycurtis] | 72.1% | 60.4% | 72.1% | 60.2% | 1.031s | 0.052s | 1.084s |
| SimilarityForest[canberra] | 72.4% | 60.8% | 72.4% | 60.6% | 1.012s | 0.047s | 1.059s |
| SimilarityForest[chebyshev] | 71.6% | 61.0% | 71.6% | 60.5% | 0.243s | 0.036s | 0.279s |
| SimilarityForest[correlation] | 71.3% | 59.8% | 71.3% | 59.5% | 0.999s | 0.046s | 1.045s |
| SimilarityForest[hamming] | 72.1% | 60.4% | 72.1% | 60.2% | 1.059s | 0.045s | 1.104s |

---

## Acknowledgments

Yeh, I. (2009). Default of Credit Card Clients [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C55S3H.

