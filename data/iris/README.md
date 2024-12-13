# Iris

**Description**:  

This is one of the earliest datasets used in the literature on classification methods and widely used in statistics and machine learning.  The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant.  One class is linearly separable from the other 2; the latter are not linearly separable from each other.

---

## Table of Contents
- [Iris](#iris)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Iris](https://archive.ics.uci.edu/dataset/53/iris)
  
- **Domain**: Biology

- **Format**: CSV  

---

## Variables

| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***sepal_length*** | Feature | Length of the sepal | Continuous | - |
| ***sepal_width*** | Feature | Width of the sepal | Continuous | - |
| ***petal_length*** | Feature | Length of the petal | Continuous | - |
| ***petal_width*** | Feature | Width of the petal | Continuous | - |
| ***class*** | **Target** | Species of the iris flower | Categorical | Iris-setosa, Iris-versicolor, Iris-virginica |

---

## Target Variable

- **Name**: *class*  
- **Type**: Categorical
- **Values**:
  - Iris-setosa
  - Iris-versicolor
  - Iris-virginica

---

## Dataset Details

- **Has missing values?**: no
- **Number of Instances**: 150 instances 
- **Number of Features**: 4
- **Class Distribution**:
  - Iris-setosa = 50 instances
  - Iris-versicolor = 50 instances
  - Iris-virginica = 50 instances
 
---

## File Structure

- `iris.csv`: Main dataset file.  
- `README.md`: Documentation file (this file).  
- `configuration.json`: Configuration file containing the instructions for DatasetPreprocessor.  

---

## Sample Data

An example of how the dataset is structured:

| sepal_length | sepal_width | petal_length | petal_width | **class** |
|---|---|---|---|---|
| 5.0 | 3.3 | 1.4 | 0.2 | Iris-setosa |
| 7.0 | 3.2 | 4.7 | 1.4 | Iris-versicolor |
| 6.5 | 3.0 | 5.5 | 1.8 | Iris-virginica |


---

## Performance Metrics

TODO

(Optional) Include baseline metrics from using simple models, such as accuracy, precision, recall, etc. Example:

| Model         | Accuracy | Precision | Recall | F1 Score |
|---------------|----------|-----------|--------|----------|
| Logistic Reg. | 95%      | 94%       | 94%    | 94.5%    |
| Random Forest | 97%      | 96%       | 96%    | 96.5%    |

---

## Acknowledgments

Fisher, R. (1936). Iris [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C56C76.

Fisher, R. A. (1936). The use of multiple measurements in taxonomic problems. Annals of Eugenics, 7(2), 179-188.