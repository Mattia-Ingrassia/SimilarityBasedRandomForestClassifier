# breast_cancer_wisconsin

**Description**:

Features are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass.
They describe characteristics of the cell nuclei present in the image.

---

## Table of Contents
- [breast\_cancer\_wisconsin](#breast_cancer_wisconsin)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Breast Cancer Wisconsin](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic)

- **Domain**: Health and Medicine

- **Format**: CSV

---

## Variables

List the features (columns) in the dataset along with descriptions, data types, and possible values. Example:


| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***id*** | ID | (should be ignored) | Categorical | - |
| ***diagnosis*** | **Target** | M = malignant, B = Benign | Categorical | M, B |
| ***radius1*** | Feature | mean of distances from center to points on the perimeter | Continuous | - |
| ***texture1*** | Feature | standard deviation of gray-scale values | Continuous | - |
| ***perimeter1*** | Feature | - | Continuous | - |
| ***area1*** | Feature | - | Continuous | - |
| ***smoothness1*** | Feature | local variation in radius lengths | Continuous | - |
| ***compactness1*** | Feature | perimeter^2 / area - 1.0 | Continuous | - |
| ***concavity1*** | Feature | severity of concave portions of the contour | Continuous | - |
| ***concave_points1*** | Feature | number of concave portions of the contour | Continuous | - |
| ***symmetry1*** | Feature | - | Continuous | - |
| ***fractal_dimension1*** | Feature | "coastline approximation" - 1 | Continuous | - |
| ***radius2*** | Feature | mean of distances from center to points on the perimeter | Continuous | - |
| ***texture2*** | Feature | standard deviation of gray-scale values | Continuous | - |
| ***perimeter2*** | Feature | - | Continuous | - |
| ***area2*** | Feature | - | Continuous | - |
| ***smoothness2*** | Feature | local variation in radius lengths | Continuous | - |
| ***compactness2*** | Feature | perimeter^2 / area - 1.0 | Continuous | - |
| ***concavity2*** | Feature | severity of concave portions of the contour | Continuous | - |
| ***concave_points2*** | Feature | number of concave portions of the contour | Continuous | - |
| ***symmetry2*** | Feature | - | Continuous | - |
| ***fractal_dimension2*** | Feature | "coastline approximation" - 1 | Continuous | - |
| ***radius3*** | Feature | mean of distances from center to points on the perimeter | Continuous | - |
| ***texture3*** | Feature | standard deviation of gray-scale values | Continuous | - |
| ***perimeter3*** | Feature | - | Continuous | - |
| ***area3*** | Feature | - | Continuous | - |
| ***smoothness3*** | Feature | local variation in radius lengths | Continuous | - |
| ***compactness3*** | Feature | perimeter^2 / area - 1.0 | Continuous | - |
| ***concavity3*** | Feature | severity of concave portions of the contour | Continuous | - |
| ***concave_points3*** | Feature | number of concave portions of the contour | Continuous | - |
| ***symmetry3*** | Feature | - | Continuous | - |
| ***fractal_dimension3*** | Feature | "coastline approximation" - 1 | Continuous | - |

---

## Target Variable

- **Name**: diagnosis
- **Type**: Categorical
- **Values**: B = Benign, M = Malignant

---

## Dataset Details

- **Has missing values?**: no
- **Number of Instances**: 569 instances
- **Number of Features**: 30
- **Class Distribution**:
  - M: 212
  - B: 357

---

## File Structure

- `breast_cancer_wisconsin.csv`: Main dataset file.
- `README.md`: Documentation file (this file).
- `configuration.json`: Configuration file containing the istructions for DatasetPreprocessor.
- `results_images/`: A folder containing the charts of the metrics analyzed.
- `results_metrics.json`: The json file containing the results of the models for this dataset.

---

## Sample Data

An example of how the dataset is structured:

| id | diagnosis | radius1 | texture1 | perimeter1 | area1 | smoothness1 | compactness1 | concavity1 | concave_points1 | symmetry1 | fractal_dimension1 | radius2 | texture2 | perimeter2 | area2 | smoothness2 | compactness2 | concavity2 | concave_points2 | symmetry2 | fractal_dimension2 | radius3 | texture3 | perimeter3 | area3 | smoothness3 | compactness3 | concavity3 | concave_points3 | symmetry3 | fractal_dimension3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 849014 | M | 19.81 | 22.15 | 130 | 1260 | 0.09831 | 0.1027 | 0.1479 | 0.09498 | 0.1582 | 0.05395 | 0.7582 | 1.017 | 5.865 | 112.4 | 0.006494 | 0.01893 | 0.03391 | 0.01521 | 0.01356 | 0.001997 | 27.32 | 30.88 | 186.8 | 2398 | 0.1512 | 0.315 | 0.5372 | 0.2388 | 0.2768 | 0.07615 |
| 8510426 | B | 13.54 | 14.36 | 87.46 | 566.3 | 0.09779 | 0.08129 | 0.06664 | 0.04781 | 0.1885 | 0.05766 | 0.2699 | 0.7886 | 2.058 | 23.56 | 0.008462 | 0.0146 | 0.02387 | 0.01315 | 0.0198 | 0.0023 | 15.11 | 19.26 | 99.7 | 711.2 | 0.144 | 0.1773 | 0.239 | 0.1288 | 0.2977 | 0.07259 |
| 8510653 | B | 13.08 | 15.71 | 85.63 | 520 | 0.1075 | 0.127 | 0.04568 | 0.0311 | 0.1967 | 0.06811 | 0.1852 | 0.7477 | 1.383 | 14.67 | 0.004097 | 0.01898 | 0.01698 | 0.00649 | 0.01678 | 0.002425 | 14.5 | 20.49 | 96.09 | 630.5 | 0.1312 | 0.2776 | 0.189 | 0.07283 | 0.3184 | 0.08183 |

---

## Performance Metrics

| Classifier | Accuracy | Balanced Accuracy | Micro F1 | Macro F1 | Training Time | Prediction Time | Total Time |
|---|---|---|---|---|---|---|---|
| ***Random Forest*** | ***98.2%*** | ***98.3%*** | ***98.2%*** | ***98.1%*** | 0.038s | 0.001s | 0.039s |
| ***Extra Trees*** | ***98.2%*** | ***98.3%*** | ***98.2%*** | ***98.1%*** | 0.019s | 0.002s | 0.021s |
| XGBoost | 97.1% | 96.7% | 97.1% | 96.8% | 0.022s | 0.001s | 0.023s |
| AdaBoost | 97.1% | 96.4% | 97.1% | 96.8% | 0.076s | 0.003s | 0.079s |
| Gradient Boosting | 95.3% | 94.3% | 95.3% | 94.9% | 0.112s | 0.000s | 0.113s |
| SimilarityForest[cityblock] | 91.8% | 90.2% | 91.8% | 91.0% | 0.023s | 0.003s | 0.025s |
| SimilarityForest[cosine] | 95.9% | 95.8% | 95.9% | 95.6% | 0.023s | 0.003s | 0.025s |
| SimilarityForest[euclidean] | 94.2% | 93.1% | 94.2% | 93.6% | 0.022s | 0.002s | 0.025s |
| SimilarityForest[braycurtis] | 93.0% | 93.1% | 93.0% | 92.6% | 0.024s | 0.003s | 0.026s |
| SimilarityForest[canberra] | 94.7% | 94.5% | 94.7% | 94.4% | 0.022s | 0.003s | 0.025s |
| SimilarityForest[chebyshev] | 95.3% | 96.0% | 95.3% | 95.1% | 0.022s | 0.002s | 0.025s |
| SimilarityForest[correlation] | 95.9% | 95.8% | 95.9% | 95.6% | 0.022s | 0.003s | 0.025s |
| SimilarityForest[hamming] | 90.6% | 89.9% | 90.6% | 89.9% | 0.023s | 0.003s | 0.025s |

---

## Acknowledgments

Wolberg, W., Mangasarian, O., Street, N., & Street, W. (1993). Breast Cancer Wisconsin (Diagnostic) [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5DW2B.