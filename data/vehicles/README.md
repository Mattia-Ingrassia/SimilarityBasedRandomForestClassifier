# Vehicles

**Description**:  

This data was originally gathered at the TI in 1986-87 by JP Siebert. It was partially financed by Barr and Stroud Ltd. The original purpose was to find a method of distinguishing 3D objects within a 2D image by application of an ensemble of shape feature extractors to the 2D silhouettes of the objects. Measures of shape features extracted from example silhouettes of objects to be discriminated were used to generate a classification rule tree by means of computer induction.

This object recognition strategy was successfully used to discriminate between silhouettes of model cars, vans and buses viewed from constrained elevation but all angles of rotation.

---

## Table of Contents
- [Vehicles](#vehicles)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Statlog (Vehicle Silhouettes)](https://archive.ics.uci.edu/dataset/149/statlog+vehicle+silhouettes)
  
- **Domain**: Other

- **Format**: CSV  

---

## Variables

| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***COMPACTNESS*** | Feature | Measure of compactness of the vehicle | Integer | - |
| ***CIRCULARITY*** | Feature | Measure of circularity of the vehicle | Integer | - |
| ***DISTANCE_CIRCULARITY*** | Feature | Measure of distance circularity of the vehicle | Integer | - |
| ***RADIUS_RATIO*** | Feature | Ratio of the radius of the vehicle | Integer | - |
| ***PR.AXIS_ASPECT_RATIO*** | Feature | Aspect ratio of the principal axis | Integer | - |
| ***MAX.LENGTH_ASPECT_RATIO*** | Feature | Aspect ratio of the maximum length | Integer | - |
| ***SCATTER_RATIO*** | Feature | Scatter ratio of the vehicle | Integer | - |
| ***ELONGATEDNESS*** | Feature | Measure of elongatedness of the vehicle | Integer | - |
| ***PR.AXIS_RECTANGULARITY*** | Feature | Rectangularity of the principal axis | Integer | - |
| ***MAX.LENGTH_RECTANGULARITY*** | Feature | Rectangularity of the maximum length | Integer | - |
| ***SCALED_VARIANCE_MAJOR*** | Feature | Scaled variance of the major axis | Integer | - |
| ***SCALED_VARIANCE_MINOR*** | Feature | Scaled variance of the minor axis | Integer | - |
| ***SCALED_RADIUS_OF_GYRATION*** | Feature | Scaled radius of gyration | Integer | - |
| ***SKEWNESS_ABOUT_MAJOR*** | Feature | Skewness about the major axis | Integer | - |
| ***SKEWNESS_ABOUT_MINOR*** | Feature | Skewness about the minor axis | Integer | - |
| ***KURTOSIS_ABOUT_MAJOR*** | Feature | Kurtosis about the major axis | Integer | - |
| ***KURTOSIS_ABOUT_MINOR*** | Feature | Kurtosis about the minor axis | Integer | - |
| ***HOLLOWS_RATIO*** | Feature | Hollows ratio of the vehicle | Integer | - |
| ***class*** | **Target** | Type of vehicle | Categorical | bus, opel, saab, van |

---

## Target Variable

- **Name**: *class*  
- **Type**: Categorical
- **Values**:
  - bus
  - opel
  - saab
  - van

---

## Dataset Details

- **Has missing values?**: no
- **Number of Instances**: 846 instances 
- **Number of Features**: 18
- **Class Distribution**:
  - bus = 218 instances
  - opel = 212 instances
  - saab = 217 instances
  - van = 199 instances
 
---

## File Structure

- `vehicles.csv`: Main dataset file.  
- `README.md`: Documentation file (this file).  
- `configuration.json`: Configuration file containing the instructions for DatasetPreprocessor.  

---

## Sample Data

| COMPACTNESS | CIRCULARITY | DISTANCE_CIRCULARITY | RADIUS_RATIO | PR.AXIS_ASPECT_RATIO | MAX.LENGTH_ASPECT_RATIO | SCATTER_RATIO | ELONGATEDNESS | PR.AXIS_RECTANGULARITY | MAX.LENGTH_RECTANGULARITY | SCALED_VARIANCE_MAJOR | SCALED_VARIANCE_MINOR | SCALED_RADIUS_OF_GYRATION | SKEWNESS_ABOUT_MAJOR | SKEWNESS_ABOUT_MINOR | KURTOSIS_ABOUT_MAJOR | KURTOSIS_ABOUT_MINOR | HOLLOWS_RATIO | class |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 104 | 50 | 106 | 209 | 66 | 10 | 207 | 32 | 23 | 158 | 223 | 635 | 220 | 73 | 14 | 9 | 188 | 196 | saab |
| 93 | 41 | 82 | 159 | 63 | 9 | 144 | 46 | 19 | 143 | 160 | 309 | 127 | 63 | 6 | 10 | 199 | 207 | van |
| 85 | 44 | 70 | 205 | 103 | 52 | 149 | 45 | 19 | 144 | 241 | 325 | 188 | 127 | 9 | 11 | 180 | 183 | bus |

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

Mowforth, P. & Shepherd, B.  Statlog (Vehicle Silhouettes) [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5HG6N.