# Rice

**Description**:  

A total of 3810 rice grain's images were taken for the two species, processed and feature inferences were made. 7 morphological features were obtained for each grain of rice.

---

## Table of Contents
- [Rice](#rice)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Rice](https://archive.ics.uci.edu/dataset/545/rice+cammeo+and+osmancik)
  
- **Domain**: Biology

- **Format**: CSV  

---

## Variables

| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***Area*** | Feature | Returns the number of pixels within the boundaries of the rice grain | Integer | - |
| ***Perimeter*** | Feature | Calculates the circumference by calculating the distance between pixels around the boundaries of the rice grain | Continuous | - |
| ***Major_Axis_Length*** | Feature | The longest line that can be drawn on the rice grain, i.e. the main axis distance, gives | Continuous | - |
| ***Minor_Axis_Length*** | Feature | The shortest line that can be drawn on the rice grain, i.e. the small axis distance, gives | Continuous | - |
| ***Eccentricity*** | Feature | It measures how round the ellipse, which has the same moments as the rice grain, is | Continuous | - |
| ***Convex_Area*** | Feature | Returns the pixel count of the smallest convex shell of the region formed by the rice grain | Integer | - |
| ***Extent*** | Feature | Returns the ratio of the region formed by the rice grain to the bounding box | Continuous | - |
| ***Class*** | **Target** | The variety of the rice grain | Categorical | Cammeo, Osmancik |

---

## Target Variable

- **Name**: *Class*  
- **Type**: Categorical
- **Values**:
  - Cammeo
  - Osmanick

---

## Dataset Details

- **Has missing values?**: no
- **Number of Instances**: 3810 instances 
- **Number of Features**: 7
- **Class Distribution**:
  - Osmanick = 2180 instances
  - Cammeo = 1630 instances
 
---

## File Structure

- `rice.csv`: Main dataset file.  
- `README.md`: Documentation file (this file).  
- `configuration.json`: Configuration file containing the instructions for DatasetPreprocessor.  

---

## Sample Data

| Area | Perimeter | Major_Axis_Length | Minor_Axis_Length | Eccentricity | Convex_Area | Extent | **Class** |
|---|---|---|---|---|---|---|---|
| 13939.0 | 484.39300537109375 | 207.02627563476562 | 86.22347259521484 | 0.9091423153877258 | 14233.0 | 0.6424686312675476 | *Cammeo* |
| 12488.0 | 469.8280029296875 | 200.74375915527344 | 80.0468521118164 | 0.917059063911438 | 12932.0 | 0.7446630597114563 | *Cammeo* |
| 13447.0 | 455.64801025390625 | 183.95758056640625 | 94.45813751220703 | 0.8581028580665588 | 13867.0 | 0.6259076595306396 | *Osmancik* |

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

Rice (Cammeo and Osmancik) [Dataset]. (2019). UCI Machine Learning Repository. https://doi.org/10.24432/C5MW4Z.