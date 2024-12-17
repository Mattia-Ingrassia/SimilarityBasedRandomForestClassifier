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
- `results_images/`: A folder containing the charts of the metrics analyzed.
- `results_metrics.json`: The json file containing the results of the models for this dataset.

---

## Sample Data

An example of how the dataset is structured:

| Area | Perimeter | Compactness | Length of kernel | Width of kernel | Asymmetry coefficient | Length of kernel groove | Class |
|---|---|---|---|---|---|---|---|
| 12.73 | 13.75 | 0.8458 | 5.412 | 2.882 | 3.533 | 5.067 | 1 |
| 17.63 | 15.98 | 0.8673 | 6.191 | 3.561 | 4.076 | 6.06 | 2 |
| 11.23 | 12.82 | 0.8594 | 5.089 | 2.821 | 7.524 | 4.957 | 3 |

---

## Performance Metrics

| Classifier | Accuracy | Balanced Accuracy | Micro F1 | Macro F1 | Training Time | Prediction Time | Total Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Random Forest | 93.7% | 93.3% | 93.7% | 93.2% | 0.023s | 0.001s | 0.024s |
| Extra Trees | 93.7% | 93.3% | 93.7% | 93.2% | 0.016s | 0.001s | 0.017s |
| ***XGBoost*** | ***95.2%*** | ***95.2%*** | ***95.2%*** | ***94.9%*** | 0.021s | 0.001s | 0.022s |
| AdaBoost | 93.7% | 93.3% | 93.7% | 93.2% | 0.035s | 0.003s | 0.038s |
| ***Gradient Boosting*** | ***95.2%*** | ***95.2%*** | ***95.2%*** | ***94.9%*** | 0.062s | 0.001s | 0.063s |
| SimilarityForest[cityblock] | 92.1% | 91.7% | 92.1% | 91.4% | 0.023s | 0.003s | 0.025s |
| SimilarityForest[cosine] | 92.1% | 91.3% | 92.1% | 91.4% | 0.023s | 0.002s | 0.025s |
| SimilarityForest[euclidean] | 92.1% | 91.7% | 92.1% | 91.4% | 0.012s | 0.002s | 0.014s |
| SimilarityForest[braycurtis] | 90.5% | 90.1% | 90.5% | 90.0% | 0.012s | 0.002s | 0.014s |
| SimilarityForest[canberra] | 90.5% | 90.1% | 90.5% | 90.0% | 0.012s | 0.002s | 0.014s |
| ***SimilarityForest[chebyshev]*** | ***95.2%*** | ***95.2%*** | 95.2% | 94.9% | 0.023s | 0.002s | 0.025s |
| SimilarityForest[correlation] | 92.1% | 91.3% | 92.1% | 91.4% | 0.023s | 0.002s | 0.025s |
| ***SimilarityForest[hamming]*** | ***95.2%*** | ***95.2%*** | ***95.2%*** | ***94.9%*** | 0.024s | 0.002s | 0.026s |



---

## Acknowledgments

Charytanowicz, M., Niewczas, J., Kulczycki, P., Kowalski, P., & Lukasik, S. (2010). Seeds [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5H30K.
