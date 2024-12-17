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
- `results_images/`: A folder containing the charts of the metrics analyzed.
- `results_metrics.json`: The json file containing the results of the models for this dataset.

---

## Sample Data

An example of how the dataset is structured:

| COMPACTNESS | CIRCULARITY | DISTANCE_CIRCULARITY | RADIUS_RATIO | PR.AXIS_ASPECT_RATIO | MAX.LENGTH_ASPECT_RATIO | SCATTER_RATIO | ELONGATEDNESS | PR.AXIS_RECTANGULARITY | MAX.LENGTH_RECTANGULARITY | SCALED_VARIANCE_MAJOR | SCALED_VARIANCE_MINOR | SCALED_RADIUS_OF_GYRATION | SKEWNESS_ABOUT_MAJOR | SKEWNESS_ABOUT_MINOR | KURTOSIS_ABOUT_MAJOR | KURTOSIS_ABOUT_MINOR | HOLLOWS_RATIO | class |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 104 | 50 | 106 | 209 | 66 | 10 | 207 | 32 | 23 | 158 | 223 | 635 | 220 | 73 | 14 | 9 | 188 | 196 | saab |
| 93 | 41 | 82 | 159 | 63 | 9 | 144 | 46 | 19 | 143 | 160 | 309 | 127 | 63 | 6 | 10 | 199 | 207 | van |
| 85 | 44 | 70 | 205 | 103 | 52 | 149 | 45 | 19 | 144 | 241 | 325 | 188 | 127 | 9 | 11 | 180 | 183 | bus |

---

## Performance Metrics

| Classifier | Accuracy | Balanced Accuracy | Micro F1 | Macro F1 | Training Time | Prediction Time | Total Time |
|  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |
| Random Forest | 74.0% | 76.1% | 74.0% | 74.3% | 0.039s | 0.001s | 0.040s |
| Extra Trees | 72.8% | 75.0% | 72.8% | 73.4% | 0.026s | 0.002s | 0.028s |
| XGBoost | 76.0% | 77.7% | 76.0% | 76.9% | 0.040s | 0.001s | 0.041s |
| AdaBoost | 62.6% | 65.5% | 62.6% | 61.1% | 0.045s | 0.003s | 0.048s |
| Gradient Boosting | 73.6% | 75.7% | 73.6% | 73.5% | 0.190s | 0.001s | 0.192s |
| SimilarityForest[cityblock] | 65.7% | 66.8% | 65.7% | 66.5% | 0.023s | 0.003s | 0.025s |
| SimilarityForest[cosine] | 70.1% | 71.4% | 70.1% | 71.5% | 0.022s | 0.003s | 0.025s |
| SimilarityForest[euclidean] | 70.5% | 71.6% | 70.5% | 70.7% | 0.023s | 0.003s | 0.025s |
| SimilarityForest[braycurtis] | 69.3% | 70.4% | 69.3% | 70.1% | 0.024s | 0.003s | 0.027s |
| SimilarityForest[canberra] | 67.7% | 69.0% | 67.7% | 68.3% | 0.022s | 0.003s | 0.025s |
| SimilarityForest[chebyshev] | 65.0% | 66.1% | 65.0% | 65.6% | 0.048s | 0.003s | 0.050s |
| SimilarityForest[correlation] | 73.2% | 74.4% | 73.2% | 73.9% | 0.022s | 0.003s | 0.025s |
| SimilarityForest[hamming] | 66.9% | 67.9% | 66.9% | 68.2% | 0.023s | 0.003s | 0.026s |

---

## Acknowledgments

Mowforth, P. & Shepherd, B.  Statlog (Vehicle Silhouettes) [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5HG6N.