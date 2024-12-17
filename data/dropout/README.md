# Dropout

**Description**:

A dataset created from a higher education institution (acquired from several disjoint databases) related to students enrolled in different undergraduate degrees, such as agronomy, design, education, nursing, journalism, management, social service, and technologies. The dataset includes information known at the time of student enrollment (academic path, demographics, and social-economic factors) and the students' academic performance at the end of the first and second semesters. The data is used to build classification models to predict students' dropout and academic sucess. The problem is formulated as a three category classification task, in which there is a strong imbalance towards one of the classes.

---

## Table of Contents
- [Dropout](#dropout)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Predict Students' Dropout and Academic Success](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)

- **Domain**: Social Science

- **Format**: CSV

---

## Variables


| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***Marital status*** | Feature | 1=single, 2=married, 3=widowed, 4=divorced, 5=facto union, 6=legally separated | Categorical | 1-6 |
| ***Application mode*** | Feature | For more information check the dataset's website | Categorical | - |
| ***Application order*** | Feature | For more information check the dataset's website | Categorical | - |
| ***Course*** | Feature | For more information check the dataset's website | Categorical | - |
| ***Daytime/evening attendance*** | Feature | 0 = evening, 1 = daytime | Binary | 0 / 1 |
| ***Previous qualification*** | Feature | For more information check the dataset's website | Categorical | - |
| ***Previous qualification (grade)*** | Feature | For more information check the dataset's website | Categorical | - |
| ***Nationality*** | Feature | For more information check the dataset's website | Categorical | - |
| ***Mother's qualification*** | Feature | For more information check the dataset's website | Categorical | - |
| ***Father's qualification*** | Feature | - | Categorical | - |
| ***Mother's occupation*** | Feature | For more information check the dataset's website | Categorical | - |
| ***Father's occupation*** | Feature | For more information check the dataset's website | Categorical | - |
| ***Admission grade*** | Feature | Admission grade | Continuous | 0 - 200 |
| ***Displaced*** | Feature | 1 = yes, 0 = no | Binary | 0 / 1 |
| ***Educational special needs*** | Feature | 1 = yes, 0 = no | Binary | 0 / 1 |
| ***Debtor*** | Feature | 1 = yes, 0 = no | Binary | 0 / 1 |
| ***Tuition fees up to date*** | Feature | 1 = yes, 0 = no | Binary | 0 / 1 |
| ***Gender*** | Feature | 1 = Male, 0 = Female | Binary | 0 / 1 |
| ***Scholarship holder*** | Feature | 1 = yes, 0 = no | Binary | 0 / 1 |
| ***Age at enrollment*** | Feature | Age | Integer | - |
| ***International*** | Feature | 1 = yes, 0 = no | Categorical | 0 / 1 |
| ***Curricular units 1st sem (credited)*** | Feature | Number of curricular units credited in the 1st semester | Integer | - |
| ***Curricular units 1st sem (enrolled)*** | Feature | Number of curricular units enrolled in the 1st semester | Integer | - |
| ***Curricular units 1st sem (evaluations)*** | Feature | Number of evaluations to curricular units in the 1st semester | Integer | - |
| ***Curricular units 1st sem (approved)*** | Feature | Number of curricular units approved in the 1st semester | Integer | - |
| ***Curricular units 1st sem (grade)*** | Feature | Grade average in the 1st semester | Integer | 0 - 20 |
| ***Curricular units 1st sem (without evaluations)*** | Feature | Number of curricular units without evalutions in the 1st semester | Integer | - |
| ***Curricular units 2nd sem (credited)*** | Feature | Number of curricular units credited in the 2nd semester | Integer | - |
| ***Curricular units 2nd sem (enrolled)*** | Feature | Number of curricular units enrolled in the 2nd semester | Integer | - |
| ***Curricular units 2nd sem (evaluations)*** | Feature | Number of evaluations to curricular units in the 2nd semester | Integer | - |
| ***Curricular units 2nd sem (approved)*** | Feature | Number of curricular units approved in the 2nd semester | Integer | - |
| ***Curricular units 2nd sem (grade)*** | Feature | Grade average in the 2nd semester | Integer | 0 - 20 |
| ***Curricular units 2nd sem (without evaluations)*** | Feature | Number of curricular units without evalutions in the 2nd semester | Integer | - |
| ***Unemployment rate*** | Feature | Unemployment rate (%) | Continuous | - |
| ***Inflation rate*** | Feature | Inflation rate (%) | Continuous | - |
| ***GDP*** | Feature | - | Continuous | - |
| ***Target*** | **Target** | Three category classification (dropout, enrolled, and graduate) at the end of the normal duration of the course | Categorical | dropout, enrolled, graduate |

---

## Target Variable

- **Name**: Target.
- **Type**: Categorical
- **Values**:
  - dropout
  - enrolled
  - graduate

---

## Dataset Details

- **Has missing values?**: no
- **Number of Instances**: 4424 instances
- **Number of Features**: 36
- **Class Distribution**:
  - Dropout: 1421 instances
  - Graduate: 2209 instances
  - Enrolled: 794 instances


---

## File Structure

- `dropout.csv`: Main dataset file.
- `README.md`: Documentation file (this file).
- `configuration.json`: Configuration file containing the istructions for DatasetPreprocessor.
- `results_images/`: A folder containing the charts of the metrics analyzed.
- `results_metrics.json`: The json file containing the results of the models for this dataset.


---

## Sample Data

An example of how the dataset is structured:

| Marital status | Application mode | Application order | Course | Daytime/evening attendance | Previous qualification | Previous qualification (grade) | Nationality | Mother's qualification | Father's qualification | Mother's occupation | Father's occupation | Admission grade | Displaced | Educational special needs | Debtor | Tuition fees up to date | Gender | Scholarship holder | Age at enrollment | International | Curricular units 1st sem (credited) | Curricular units 1st sem (enrolled) | Curricular units 1st sem (evaluations) | Curricular units 1st sem (approved) | Curricular units 1st sem (grade) | Curricular units 1st sem (without evaluations) | Curricular units 2nd sem (credited) | Curricular units 2nd sem (enrolled) | Curricular units 2nd sem (evaluations) | Curricular units 2nd sem (approved) | Curricular units 2nd sem (grade) | Curricular units 2nd sem (without evaluations) | Unemployment rate | Inflation rate | GDP | Target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 9085 | 1 | 1 | 149.0 | 1 | 38 | 37 | 5 | 5 | 137.1 | 1 | 0 | 0 | 1 | 0 | 1 | 18 | 0 | 0 | 5 | 7 | 4 | 13.25 | 0 | 0 | 5 | 5 | 5 | 12.0 | 0 | 10.8 | 1.4 | 1.74 | Graduate |
| 1 | 1 | 1 | 9773 | 1 | 1 | 127.0 | 1 | 19 | 37 | 9 | 3 | 120.7 | 1 | 0 | 0 | 1 | 0 | 0 | 20 | 0 | 0 | 6 | 6 | 5 | 13.2 | 0 | 0 | 6 | 7 | 0 | 0.0 | 0 | 15.5 | 2.8 | -4.06 | Dropout |
| 1 | 18 | 1 | 9238 | 1 | 1 | 137.0 | 1 | 19 | 38 | 5 | 8 | 137.4 | 1 | 0 | 0 | 1 | 0 | 0 | 18 | 0 | 0 | 6 | 10 | 1 | 12.0 | 0 | 0 | 6 | 14 | 2 | 11.0 | 0 | 10.8 | 1.4 | 1.74 | Enrolled |

---

## Performance Metrics

| Classifier | Accuracy | Balanced Accuracy | Micro F1 | Macro F1 | Training Time | Prediction Time | Total Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Random Forest | 76.2% | 66.9% | 76.2% | 67.6% | 0.126s | 0.005s | 0.131s |
| Extra Trees | 77.3% | 67.8% | 77.3% | 68.6% | 0.092s | 0.006s | 0.098s |
| ***XGBoost*** | ***77.6%*** | ***69.6%*** | ***77.6%*** | ***70.4%*** | 0.067s | 0.001s | 0.069s |
| AdaBoost | 72.4% | 61.0% | 72.4% | 60.3% | 0.103s | 0.004s | 0.107s |
| Gradient Boosting | 76.5% | 66.5% | 76.5% | 67.4% | 0.545s | 0.003s | 0.547s |
| SimilarityForest[cityblock] | 66.6% | 60.0% | 66.6% | 59.8% | 0.150s | 0.007s | 0.157s |
| SimilarityForest[cosine] | 66.1% | 59.8% | 66.1% | 59.3% | 0.078s | 0.006s | 0.084s |
| SimilarityForest[euclidean] | 65.1% | 57.3% | 65.1% | 57.3% | 0.070s | 0.006s | 0.076s |
| SimilarityForest[braycurtis] | 67.6% | 60.2% | 67.6% | 60.1% | 0.081s | 0.007s | 0.088s |
| SimilarityForest[canberra] | 65.1% | 58.8% | 65.1% | 58.4% | 0.088s | 0.007s | 0.095s |
| SimilarityForest[chebyshev] | 66.1% | 59.2% | 66.1% | 58.7% | 0.069s | 0.007s | 0.076s |
| SimilarityForest[correlation] | 66.6% | 59.6% | 66.6% | 59.2% | 0.077s | 0.007s | 0.084s |
| SimilarityForest[hamming] | 66.9% | 61.3% | 66.9% | 60.8% | 0.080s | 0.008s | 0.088s |

---

## Acknowledgments

Realinho, V., Vieira Martins, M., Machado, J., & Baptista, L. (2021). Predict Students' Dropout and Academic Success [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5MC89.


