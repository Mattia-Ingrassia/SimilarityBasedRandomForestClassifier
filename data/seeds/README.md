# Seeds

**Description**:  

Measurements of geometrical properties of kernels belonging to three different varieties of wheat. A soft X-ray technique and GRAINS package were used to construct all seven, real-valued attributes.

---

## Table of Contents
- [Seeds](#seeds)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Seeds](https://archive.ics.uci.edu/dataset/236/seeds)
  
- **Domain**: Biology

- **Format**: CSV  

---

## Variables

| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***Area*** | Feature | The area of the kernel | Continuous | - |
| ***Perimeter*** | Feature | The perimeter of the kernel | Continuous | - |
| ***Compactness*** | Feature | The compactness of the kernel | Continuous | - |
| ***Length_of_kernel*** | Feature | The length of the kernel | Continuous | - |
| ***Width_of_kernel*** | Feature | The width of the kernel | Continuous | - |
| ***Asymmetry_coefficient*** | Feature | The asymmetry coefficient of the kernel | Continuous | - |
| ***Length_of_kernel_groove*** | Feature | The length of the kernel groove | Continuous | - |
| ***Class*** | **Target** | The variety of the wheat kernel | Categorical | Kama, Rosa, Canadian |

---

## Target Variable

- **Name**: *Class*  
- **Type**: Categorical
- **Values**:
  - 1 = Kama
  - 2 = Rosa
  - 3 = Canadian

---

## Dataset Details

- **Has missing values?**: no
- **Number of Instances**: 210 instances 
- **Number of Features**: 7
- **Class Distribution**:
  - 1 = Kama = 70 instances
  - 2 = Rosa = 70 instances
  - 3 = Canadian = 70 instances
 
---

## File Structure

- `seeds.csv`: Main dataset file.  
- `README.md`: Documentation file (this file).  
- `configuration.json`: Configuration file containing the instructions for DatasetPreprocessor.  

---

## Sample Data

| Area | Perimeter | Compactness | Length of kernel | Width of kernel | Asymmetry coefficient | Length of kernel groove | Class |
|---|---|---|---|---|---|---|---|
| 12.73 | 13.75 | 0.8458 | 5.412 | 2.882 | 3.533 | 5.067 | 1 |
| 17.63 | 15.98 | 0.8673 | 6.191 | 3.561 | 4.076 | 6.06 | 2 |
| 11.23 | 12.82 | 0.8594 | 5.089 | 2.821 | 7.524 | 4.957 | 3 |

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

Charytanowicz, M., Niewczas, J., Kulczycki, P., Kowalski, P., & Lukasik, S. (2010). Seeds [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5H30K.
