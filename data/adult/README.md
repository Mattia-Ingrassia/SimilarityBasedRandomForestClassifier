# Adult

**Description**:

Predict whether annual income of an individual exceeds $50K/yr based on census data. Also known as "Census Income" dataset.

---

## Table of Contents
- [Adult](#adult)
  - [Table of Contents](#table-of-contents)
  - [Dataset Overview](#dataset-overview)
  - [Variables](#variables)
  - [Target Variable](#target-variable)
  - [Dataset Details](#dataset-details)
  - [File Structure](#file-structure)
  - [Sample Data](#sample-data)
  - [Performance Metrics (results)](#performance-metrics-results)
  - [Acknowledgments](#acknowledgments)

---

## Dataset Overview

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Adult](https://archive.ics.uci.edu/dataset/2/adult).

- **Domain**: Social Science

- **Format**: CSV

---

## Variables

| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***age*** | Feature | Age of the individual | Integer | 17-90 |
| ***workclass*** | Feature | Work class of the individual | Categorical | Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked. |
| ***fnlwgt*** | Feature | Sample weight | Integer | - |
| ***education*** | Feature | Education level | Categorical | Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool. |
| ***education-num*** | Feature | Education level | Integer | - |
| ***marital-status*** | Feature | Marital status | Categorical | Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse. |
| ***occupation*** | Feature | Occupation of the individual | Categorical | Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces. |
| ***relationship*** | Feature | Relationship status | Categorical |Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.|
| ***race*** | Feature | Race of the individual | Categorical | White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black. |
| ***sex*** | Feature | Sex of the individual | Categorical | Male, Female |
| ***capital-gain*** | Feature | Capital gain | Integer | - |
| ***capital-loss*** | Feature | Capital loss | Integer | - |
| ***hours-per-week*** | Feature | Hours per week | Integer | - |
| ***native-country*** | Feature | Native country | Categorical | United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands. |
| ***income*** | **Target** | Target split between two classes | Categorical | >50k or <=50k |

---

## Target Variable

- **Name**: income
- **Type**: Categorical
- **Values**: { >50k, <=50k}

---

## Dataset Details

- **Has missing values?**: yes - marked with "?"
- **Number of Instances**:
  - with missing values: 48842 instances
  - without missing values: 45222 instances
- **Number of Features**: 14
- **Class Distribution**:
  - with missing values: <=50K: 37155, >50K: 11687
  - without missing values: <=50K: 34014, >50K: 11208

---

## File Structure

- `adult.csv`: Main dataset file.
- `README.md`: Documentation file (this file).
- `configuration.json`: Configuration file containing the istructions for DatasetPreprocessor.
- `results_images/`: A folder containing the charts of the metrics analyzed.
- `results_metric.json`: The json file containing the results of the models for this dataset.

---

## Sample Data

An example of how the dataset is structured:

| age | workclass | fnlwgt | education | education-num | marital-status | occupation | relationship | race | sex | capital-gain | capital-loss | hours-per-week | native-country | ***income*** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | State-gov | 77516 | Bachelors | 13 | Never-married | Adm-clerical | Not-in-family | White | Male | 2174 | 0 | 40 | United-States | <=50K |
| 52 | Self-emp-not-inc | 209642 | HS-grad | 9 | Married-civ-spouse | Exec-managerial | Husband | White | Male | 0 | 0 | 45 | United-States | >50K |
| 38 | Private | 215646 | HS-grad | 9 | Divorced | Handlers-cleaners | Not-in-family | White | Male | 0 | 0 | 40 | United-States | <=50K |


---

## Performance Metrics (results)


| Classifier | Accuracy | Balanced Accuracy | Micro F1 | Macro F1 | Training Time | Prediction Time | Total Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Random Forest | 84.3% | 76.4% | 84.3% | 77.7% | 0.914s | 0.062s | 0.976s |
| Extra Trees | 82.7% | 75.0% | 82.7% | 75.9% | 1.076s | 0.085s | 1.162s |
| ***XGBoost*** | ***86.9%*** | ***78.6%*** | ***86.9%*** | ***80.8%*** | 0.095s | 0.005s | 0.100s |
| AdaBoost | 84.6% | 73.9% | 84.6% | 76.6% | 1.216s | 0.077s | 1.293s |
| Gradient Boosting | 84.9% | 73.5% | 84.9% | 76.5% | 2.133s | 0.009s | 2.142s |
| SimilarityForest[cityblock] | 80.0% | 73.3% | 80.0% | 73.2% | 4.528s | 0.125s | 4.653s |
| SimilarityForest[cosine] | 80.4% | 73.8% | 80.4% | 73.7% | 1.602s | 0.162s | 1.764s |
| SimilarityForest[euclidean] | 78.4% | 71.6% | 78.4% | 71.3% | 1.804s | 0.116s | 1.920s |
| SimilarityForest[braycurtis] | 80.6% | 74.1% | 80.6% | 74.0% | 1.439s | 0.142s | 1.582s |
| SimilarityForest[canberra] | 80.4% | 73.8% | 80.4% | 73.7% | 1.630s | 0.146s | 1.775s |
| SimilarityForest[chebyshev] | 79.4% | 73.3% | 79.4% | 72.8% | 1.603s | 0.128s | 1.731s |
| SimilarityForest[correlation] | 80.8% | 74.2% | 80.8% | 74.2% | 1.460s | 0.135s | 1.595s |
| SimilarityForest[hamming] | 81.6% | 75.1% | 81.6% | 75.2% | 1.391s | 0.132s | 1.523s |

---

## Acknowledgments

This dataset was extracted from the 1994 U.S. Census Bureau database by Barry Becker and made available for research purposes. The original extraction and cleaning process is detailed in Ron Kohavi's paper: *Scaling Up the Accuracy of Naive-Bayes Classifiers: A Decision-Tree Hybrid*.

Becker, B. & Kohavi, R. (1996). Adult [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5XW20.
