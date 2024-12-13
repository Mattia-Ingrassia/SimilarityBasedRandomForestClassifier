# Ecoli

**Description**:  

This data contains protein localization sites

---

## Table of Contents
- [Ecoli](#ecoli)
  - [Table of Contents](#table-of-contents)
  - [Dataset Overview](#dataset-overview)
  - [Variables](#variables)
  - [Variables](#variables-1)
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

---

## Sample Data

| Sequence | mcg | gvh | lip | chg | aac | alm1 | alm2 | class |
|----------|-----|-----|-----|-----|-----|------|------|-------|
| CYOA_ECOLI | 0.70 | 0.39 | 1.00 | 0.50 | 0.51 | 0.82 | 0.84 | imL |
| ATKA_ECOLI | 0.72 | 0.42 | 0.48 | 0.50 | 0.65 | 0.77 | 0.79 | imU |
| SYK2_ECOLI | 0.17 | 0.39 | 0.48 | 0.50 | 0.53 | 0.30 | 0.39 | cp |


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

Nakai, K. (1996). Ecoli [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5388M.

