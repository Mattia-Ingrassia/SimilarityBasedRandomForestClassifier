# Ecoli

**Description**:

This data contains protein localization sites

---

## Table of Contents
- [Ecoli](#ecoli)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Ecoli](https://archive.ics.uci.edu/dataset/39/ecoli)

- **Domain**: Biology

- **Format**: CSV

---

## Variables

| Variable Name | Role | Description | Data Type | Range / Values |
| --- | --- | --- | --- | --- |
| ***Sequence*** | ID | Accession number for the SWISS-PROT database (should be ignored) | Categorical | - |
| ***mcg*** | Feature | McGeoch's method for signal sequence recognition | Continuous | - |
| ***gvh*** | Feature | von Heijne's method for signal sequence recognition | Continuous | - |
| ***lip*** | Feature | von Heijne's Signal Peptidase II consensus sequence score | Categorical | 0.48 / 1 |
| ***chg*** | Feature | Presence of charge on N-terminus of predicted lipoproteins | Categorical | 0.5 / 1 |
| ***aac*** | Feature | score of discriminant analysis of the amino acid content of outer membrane and periplasmic proteins | Continuous | - |
| ***alm1*** | Feature | score of the ALOM membrane spanning region prediction program | Continuous | - |
| ***alm2*** | Feature | score of ALOM program after excluding putative cleavable signal regions from the sequence | Continuous | - |
| ***class*** | **Target** | class labels | Categorical | cp, im, pp, imU, om, omL, imL, imS |

---

## Target Variable

- **Name**: *class*
- **Type**: Categorical
- **Values**: cp, im, pp, imU, om, omL, imL, imS

---

## Dataset Details

- **Has missing values?**: no
- **Number of Instances**: 336 instances
- **Number of Features**: 7
- **Class Distribution**:
  - cp: 143 instances
  - im: 77 instances
  - imS: 2 instances
  - imL: 2 instances
  - imU: 35 instances
  - om: 20 instances
  - omL: 5 instances
  - pp: 52 instances

---

## File Structure

- `ecoli.csv`: Main dataset file.
- `README.md`: Documentation file (this file).
- `configuration.json`: Configuration file containing the istructions for DatasetPreprocessor.
- `results_images/`: A folder containing the charts of the metrics analyzed.
- `results_metrics.json`: The json file containing the results of the models for this dataset.

---

## Sample Data

An example of how the dataset is structured:

| Sequence | mcg | gvh | lip | chg | aac | alm1 | alm2 | class |
|----------|-----|-----|-----|-----|-----|------|------|-------|
| CYOA_ECOLI | 0.70 | 0.39 | 1.00 | 0.50 | 0.51 | 0.82 | 0.84 | imL |
| ATKA_ECOLI | 0.72 | 0.42 | 0.48 | 0.50 | 0.65 | 0.77 | 0.79 | imU |
| SYK2_ECOLI | 0.17 | 0.39 | 0.48 | 0.50 | 0.53 | 0.30 | 0.39 | cp |

---

## Performance Metrics

| Classifier | Accuracy | Balanced Accuracy | Micro F1 | Macro F1 | Training Time | Prediction Time | Total Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ***Random Forest*** | ***88.1%*** | ***63.9%*** | ***88.1%*** | ***61.0%*** | 0.023s | 0.001s | 0.025s |
| Extra Trees | 86.1% | 62.5% | 86.1% | 59.0% | 0.018s | 0.001s | 0.019s |
| XGBoost | 84.2% | 62.3% | 84.2% | 58.3% | 0.045s | 0.001s | 0.046s |
| AdaBoost | 33.7% | 23.1% | 33.7% | 15.9% | 0.033s | 0.004s | 0.037s |
| Gradient Boosting | 85.1% | 61.6% | 85.1% | 59.1% | 0.142s | 0.001s | 0.143s |
| SimilarityForest[cityblock] | 74.3% | 50.7% | 74.3% | 49.8% | 0.049s | 0.005s | 0.054s |
| SimilarityForest[cosine] | 64.4% | 38.7% | 64.4% | 31.9% | 0.023s | 0.006s | 0.029s |
| SimilarityForest[euclidean] | 73.3% | 55.8% | 73.3% | 48.7% | 0.023s | 0.004s | 0.027s |
| SimilarityForest[braycurtis] | 65.3% | 39.2% | 65.3% | 32.8% | 0.022s | 0.005s | 0.027s |
| SimilarityForest[canberra] | 69.3% | 38.2% | 69.3% | 35.7% | 0.022s | 0.003s | 0.025s |
| SimilarityForest[chebyshev] | 70.3% | 46.0% | 70.3% | 43.1% | 0.022s | 0.002s | 0.024s |
| SimilarityForest[correlation] | 58.4% | 21.7% | 58.4% | 21.5% | 0.022s | 0.004s | 0.026s |
| SimilarityForest[hamming] | 58.4% | 23.0% | 58.4% | 23.2% | 0.022s | 0.004s | 0.026s |

---

## Acknowledgments

Nakai, K. (1996). Ecoli [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5388M.

