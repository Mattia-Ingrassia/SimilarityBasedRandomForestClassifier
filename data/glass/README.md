# Glass

**Description**:  

From USA Forensic Science Service; 6 types of glass; defined in terms of their oxide content (i.e. Na, Fe, K, etc)

---

## Table of Contents
- [Glass](#glass)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Glass Identification](https://archive.ics.uci.edu/dataset/42/glass+identification)
  
- **Domain**: Physics and Chemistry

- **Format**: CSV  

---

## Variables

| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***Id*** | ID | ID column (should be ignored) | Integer | - |
| ***RI*** | Feature | refractive index | Continuous | - |
| ***Na*** | Feature | sodium | Continuous | - |
| ***Mg*** | Feature | magnesium | Continuous | - |
| ***Al*** | Feature | aluminum | Continuous | - |
| ***Si*** | Feature | silicon | Continuous | - |
| ***K*** | Feature | potassium | Continuous | - |
| ***Ca*** | Feature | calcium | Continuous | - |
| ***Ba*** | Feature | barium | Continuous | - |
| ***Fe*** | Feature | iron | Continuous | - |
| ***Type_of_glass*** | **Target** | a number representing a different type of glass | Continuous | 1 - 7 |

---

## Target Variable

- **Name**: Type_of_glass  
- **Type**: Categorical
- **Values**: [1, 2, 3, 5, 6, 7]

---

## Dataset Details

- **Has missing values?**: no
- **Number of Instances**: 214 instances 
- **Number of Features**: 9
- **Class Distribution**:
  - 1: 70 instances
  - 2: 76 instances
  - 3: 17 instances
  - 5: 13 instances
  - 6: 9 instances
  - 7: 29 instances

---

## File Structure

- `glass.csv`: Main dataset file.  
- `README.md`: Documentation file (this file).  
- `configuration.json`: Configuration file containing the istructions for DatasetPreprocessor.  

---

## Sample Data

| Id | RI | Na | Mg | Al | Si | K | Ca | Ba | Fe | class | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| 70 | 1.52300 | 13.31 | 3.58 | 0.82 | 71.99 | 0.12 | 10.17 | 0.00 | 0.03 | 1 | 
| 71 | 1.51574 | 14.86 | 3.67 | 1.74 | 71.87 | 0.16 | 7.36 | 0.00 | 0.12 | 2 | 
| 189 | 1.52247 | 14.86 | 2.20 | 2.06 | 70.26 | 0.76 | 9.76 | 0.00 | 0.00 | 7 | 

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

German, B. (1987). Glass Identification [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5WW2P.

