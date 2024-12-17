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
- `results_images/`: A folder containing the charts of the metrics analyzed.
- `results_metrics.json`: The json file containing the results of the models for this dataset.

---

## Sample Data

An example of how the dataset is structured:

| Area | Perimeter | Major_Axis_Length | Minor_Axis_Length | Eccentricity | Convex_Area | Extent | **Class** |
|---|---|---|---|---|---|---|---|
| 13939.0 | 484.39300537109375 | 207.02627563476562 | 86.22347259521484 | 0.9091423153877258 | 14233.0 | 0.6424686312675476 | *Cammeo* |
| 12488.0 | 469.8280029296875 | 200.74375915527344 | 80.0468521118164 | 0.917059063911438 | 12932.0 | 0.7446630597114563 | *Cammeo* |
| 13447.0 | 455.64801025390625 | 183.95758056640625 | 94.45813751220703 | 0.8581028580665588 | 13867.0 | 0.6259076595306396 | *Osmancik* |

---

## Performance Metrics

| Classifier | Accuracy | Balanced Accuracy | Micro F1 | Macro F1 | Training Time | Prediction Time | Total Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Random Forest | 92.1% | 91.5% | 92.1% | 91.9% | 0.101s | 0.003s | 0.104s |
| Extra Trees | 91.4% | 90.8% | 91.4% | 91.1% | 0.037s | 0.004s | 0.040s |
| ***XGBoost*** | ***92.2%*** | ***91.6%*** | ***92.2%*** | ***92.0%*** | 0.019s | 0.001s | 0.020s |
| ***AdaBoost*** | 92.1% | ***91.6%*** | 92.1% | 91.9% | 0.106s | 0.003s | 0.109s |
| Gradient Boosting | 91.9% | 91.3% | 91.9% | 91.6% | 0.190s | 0.001s | 0.191s |
| SimilarityForest[cityblock] | 87.9% | 87.7% | 87.9% | 87.7% | 0.100s | 0.004s | 0.104s |
| SimilarityForest[cosine] | 88.7% | 88.2% | 88.7% | 88.4% | 0.044s | 0.004s | 0.048s |
| SimilarityForest[euclidean] | 87.0% | 86.4% | 87.0% | 86.6% | 0.034s | 0.004s | 0.038s |
| SimilarityForest[braycurtis] | 88.3% | 87.6% | 88.3% | 87.9% | 0.038s | 0.004s | 0.042s |
| SimilarityForest[canberra] | 88.5% | 87.8% | 88.5% | 88.1% | 0.043s | 0.004s | 0.047s |
| SimilarityForest[chebyshev] | 88.1% | 87.9% | 88.1% | 87.8% | 0.034s | 0.004s | 0.037s |
| SimilarityForest[correlation] | 88.7% | 88.2% | 88.7% | 88.4% | 0.045s | 0.004s | 0.049s |
| SimilarityForest[hamming] | 89.2% | 88.8% | 89.2% | 88.9% | 0.042s | 0.004s | 0.046s |

---

## Acknowledgments

Rice (Cammeo and Osmancik) [Dataset]. (2019). UCI Machine Learning Repository. https://doi.org/10.24432/C5MW4Z.