# Yeast

**Description**:

This dataset contains information about various properties of yeast cells. The goal is to classify the localization sites of proteins within the cell based on their attributes.

---

## Table of Contents
- [Yeast](#yeast)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Yeast](https://archive.ics.uci.edu/dataset/110/yeast)

- **Domain**: Biology

- **Format**: CSV

---

## Variables

| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***Sequence_Name*** | ID | Accession number for the SWISS-PROT database (should be ignored) | Categorical | - |
| ***mcg*** | Feature | McGeoch's method for signal sequence recognition | Continuous | - |
| ***gvh*** | Feature | von Heijne's method for signal sequence recognition | Continuous | - |
| ***alm*** | Feature | Score of the ALOM membrane spanning region prediction program | Continuous | - |
| ***mit*** | Feature | Score of discriminant analysis of the amino acid content of the N-terminal region, excluding the signal sequence | Continuous | - |
| ***erl*** | Feature | Presence of "HDEL" substring (thought to act as a signal for retention in the endoplasmic reticulum lumen) | Continuous | - |
| ***pox*** | Feature | Score of peroxisomal targeting signal in the C-terminal | Continuous | - |
| ***vac*** | Feature | Score of discriminant analysis of the amino acid content of vacuolar proteins | Continuous | - |
| ***nuc*** | Feature | Score of discriminant analysis of nuclear localization signals of nuclear proteins | Continuous | - |
| ***localization_site*** | **Target** | Localization site of the protein | Categorical | CYT, NUC, MIT, ME3, ME2, ME1, EXC, VAC, POX, ERL |

---

## Target Variable

- **Name**: *localization_site*
- **Type**: Categorical
- **Values**:
  - CYT = Cytoplasm
  - NUC = Nucleus
  - MIT = Mitochondrion
  - ME3 = Membrane protein, no N-terminal signal
  - ME2 = Membrane protein, uncleaved signal
  - ME1 = Membrane protein, cleaved signal
  - EXC = Extracellular
  - VAC = Vacuole
  - POX = Peroxisome
  - ERL = Endoplasmic reticulum lumen

---

## Dataset Details

- **Has missing values?**: no
- **Number of Instances**: 1484 instances
- **Number of Features**: 8
- **Class Distribution**:
  - CYT = 463 instances
  - NUC = 429 instances
  - MIT = 244 instances
  - ME3 = 163 instances
  - ME2 = 51 instances
  - ME1 = 44 instances
  - EXC = 35 instances
  - VAC = 30 instances
  - POX = 20 instances
  - ERL = 5 instances

---

## File Structure

- `yeast.csv`: Main dataset file.
- `README.md`: Documentation file (this file).
- `configuration.json`: Configuration file containing the instructions for DatasetPreprocessor.
- `results_images/`: A folder containing the charts of the metrics analyzed.
- `results_metrics.json`: The json file containing the results of the models for this dataset.

---

## Sample Data

An example of how the dataset is structured:

| Sequence_Name | mcg  | gvh  | alm  | mit  | erl | pox  | vac  | nuc  | localization_site |
|---|---|---|---|---|---|---|---|---|---|
| AAR2_YEAST | 0.58 | 0.44 | 0.57 | 0.13 | 0.50 | 0.00 | 0.54 | 0.22 | NUC |
| AATM_YEAST | 0.42 | 0.44 | 0.48 | 0.54 | 0.50 | 0.00 | 0.48 | 0.22 | MIT |
| AATC_YEAST | 0.51 | 0.40 | 0.56 | 0.17 | 0.50 | 0.50 | 0.49 | 0.22 | CYT |

---

## Performance Metrics

| Classifier | Accuracy | Balanced Accuracy | Micro F1 | Macro F1 | Training Time | Prediction Time | Total Time |
|  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |
| Random Forest | 60.1% | 52.6% | 60.1% | 53.4% | 0.043s | 0.002s | 0.046s |
| Extra Trees | 59.4% | 52.5% | 59.4% | 47.7% | 0.035s | 0.003s | 0.037s |
| XGBoost | 58.5% | 52.4% | 58.5% | 47.5% | 0.101s | 0.001s | 0.102s |
| AdaBoost | 47.5% | 27.1% | 47.5% | 21.8% | 0.040s | 0.004s | 0.044s |
| Gradient Boosting | 58.5% | 46.1% | 58.5% | 42.4% | 0.327s | 0.002s | 0.330s |
| SimilarityForest[cityblock] | 46.9% | 38.4% | 46.9% | 38.4% | 0.023s | 0.004s | 0.026s |
| SimilarityForest[cosine] | 48.9% | 39.2% | 48.9% | 35.6% | 0.023s | 0.004s | 0.027s |
| SimilarityForest[euclidean] | 50.9% | 38.7% | 50.9% | 35.1% | 0.022s | 0.003s | 0.025s |
| SimilarityForest[braycurtis] | 45.7% | 39.5% | 45.7% | 38.3% | 0.022s | 0.003s | 0.025s |
| SimilarityForest[canberra] | 47.5% | 41.5% | 47.5% | 42.3% | 0.023s | 0.004s | 0.027s |
| SimilarityForest[chebyshev] | 46.2% | 37.3% | 46.2% | 32.5% | 0.063s | 0.007s | 0.071s |
| SimilarityForest[correlation] | 48.0% | 44.6% | 48.0% | 44.5% | 0.022s | 0.004s | 0.026s |
| SimilarityForest[hamming] | 46.9% | 42.6% | 46.9% | 42.7% | 0.023s | 0.003s | 0.026s |

---

## Acknowledgments

Nakai, K. (1991). Yeast [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5KG68.