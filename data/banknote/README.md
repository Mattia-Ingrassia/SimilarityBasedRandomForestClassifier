# Banknote

**Description**:

Data were extracted from images that were taken from genuine and forged banknote-like specimens.  For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.  

---

## Table of Contents
- [Banknote](#banknote)
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
 
---

## File Structure

- `banknote.csv`: Main dataset file.  
- `README.md`: Documentation file (this file).  
- `configuration.json`: Configuration file containing the istructions for DatasetPreprocessor.  

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

TODO

(Optional) Include baseline metrics from using simple models, such as accuracy, precision, recall, etc. Example:

| Model         | Accuracy | Precision | Recall | F1 Score |
|---------------|----------|-----------|--------|----------|
| Logistic Reg. | 85%      | 83%       | 82%    | 82.5%    |
| Random Forest | 90%      | 88%       | 87%    | 87.5%    |

---

## Acknowledgments

Lohweg, V. (2012). Banknote Authentication [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C55P57.

