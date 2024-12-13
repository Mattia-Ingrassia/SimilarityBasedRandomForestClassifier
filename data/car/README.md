# Car

**Description**:  

Derived from simple hierarchical decision model, this car evaluation database may be useful for testing constructive induction and structure discovery methods.

---

## Table of Contents
- [Car](#car)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Car Evaluation](https://archive.ics.uci.edu/dataset/19/car+evaluation)
  
- **Domain**: Other

- **Format**: CSV  

---

## Variables

| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***buying*** | Feature | Buying price | Categorical | vhigh, high, med, low |
| ***maint*** | Feature | Price of the maintenance | Categorical | vhigh, high, med, low |
| ***doors***| Feature | Number of doors | Categorical | 2, 3, 4, 5more |
| ***persons*** | Feature | Capacity in terms of persons to carry | Categorical | 2, 4, more |
| ***lug_boot*** | Feature | The size of luggage boot | Categorical | small, med, big |
| ***safety*** | Feature | Estimated safety of the car | Categorical | low, med, high |
| ***class***| **Target** | Evaluation Level (unacc = unacceptable, acc = acceptable, good = good, vgood = very good) | Categorical | unacc, acc, good, vgood |

---

## Target Variable

- **Name**: *class*
- **Type**: Categorical 
- **Values**: 
  - unacc = unacceptable
  - acc = acceptable
  - good = good
  - vgood = very good  

---

## Dataset Details

- **Has missing values?**: no
- **Number of Instances**: 1728 instances 
- **Number of Features**: 6
- **Class Distribution**:
  - unacc = 1210 instances
  - acc = 384 instances
  - good = 69 instances
  - vgood = 65 instances
---

## File Structure

- `car.csv`: Main dataset file.  
- `README.md`: Documentation file (this file).  
- `configuration.json`: Configuration file containing the istructions for DatasetPreprocessor.  

---

## Sample Data

An example of how the dataset is structured:

| buying | maint | doors | persons | lug_boot | safety | class |
| --- | --- | --- | --- | --- | --- | --- | 
| low | med | 5more | more | big | med | good |
| low | med | 5more | more | big | high | vgood |
| low | low | 2 | 2 | small | low | unacc |

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

Bohanec, M. (1988). Car Evaluation [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5JP48.

