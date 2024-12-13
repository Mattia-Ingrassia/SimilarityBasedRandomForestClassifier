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

TODO

(Optional) Include baseline metrics from using simple models, such as accuracy, precision, recall, etc. Example:

| Model         | Accuracy | Precision | Recall | F1 Score |
|---------------|----------|-----------|--------|----------|
| Logistic Reg. | 85%      | 83%       | 82%    | 82.5%    |
| Random Forest | 90%      | 88%       | 87%    | 87.5%    |

---

## Acknowledgments

Statlog (Shuttle) [Dataset].  UCI Machine Learning Repository. https://doi.org/10.24432/C5WS31.