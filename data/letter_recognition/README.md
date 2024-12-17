# Letter Recognition

**Description**:

The objective is to identify each of a large number of black-and-white rectangular pixel displays as one of the 26 capital letters in the English alphabet. The character images were based on 20 different fonts and each letter within these 20 fonts was randomly distorted to produce a file of 20,000 unique stimuli. Each stimulus was converted into 16 primitive numerical attributes (statistical moments and edge counts) which were then scaled to fit into a range of integer values from 0 through 15. We typically train on the first 16000 items and then use the resulting model to predict the letter category for the remaining 4000. See the article cited below for more details.

---

## Table of Contents
- [Letter Recognition](#letter-recognition)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Letter Recognition](https://archive.ics.uci.edu/dataset/59/letter+recognition)

- **Domain**: Computer Science

- **Format**: CSV

---

## Variables

| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***letter*** | **Target** | The letter represented by the instance | Categorical | A-Z |
| ***x-box*** | Feature | Horizontal position of box | Integer | - |
| ***y-box*** | Feature | Vertical position of box | Integer | - |
| ***width*** | Feature | Width of box | Integer | - |
| ***height*** | Feature | Height of box | Integer | - |
| ***onpix*** | Feature | Total number of on pixels | Integer | - |
| ***x-bar*** | Feature | Mean x of on pixels in box | Integer | - |
| ***y-bar*** | Feature | Mean y of on pixels in box | Integer | - |
| ***x2bar*** | Feature | Mean x variance | Integer | - |
| ***y2bar*** | Feature | Mean y variance | Integer | - |
| ***xybar*** | Feature | Mean x y correlation | Integer | - |
| ***x2ybr*** | Feature | Mean of x * x * y | Integer | - |
| ***xy2br*** | Feature | Mean of x * y * y | Integer | - |
| ***x-ege*** | Feature | Mean edge count left to right | Integer | - |
| ***xegvy*** | Feature | Correlation of x-ege with y | Integer | - |
| ***y-ege*** | Feature | Mean edge count bottom to top | Integer | - |
| ***yegvx*** | Feature | Correlation of y-ege with x | Integer | - |

---

## Target Variable

- **Name**: *letter*
- **Type**: Categorical
- **Values**:
  - A-Z (26 capital letters)

---

## Dataset Details

- **Has missing values?**: no
- **Number of Instances**: 20000 instances
- **Number of Features**: 16
- **Class Distribution**:
  - A: 789 instances
  - B: 766 instances
  - C: 736 instances
  - D: 805 instances
  - E: 768 instances
  - F: 775 instances
  - G: 773 instances
  - H: 734 instances
  - I: 755 instances
  - J: 747 instances
  - K: 739 instances
  - L: 761 instances
  - M: 792 instances
  - N: 783 instances
  - O: 753 instances
  - P: 803 instances
  - Q: 783 instances
  - R: 758 instances
  - S: 748 instances
  - T: 796 instances
  - U: 813 instances
  - V: 764 instances
  - W: 752 instances
  - X: 787 instances
  - Y: 786 instances
  - Z: 734 instances

---

## File Structure

- `letter_recognition.csv`: Main dataset file.
- `README.md`: Documentation file (this file).
- `configuration.json`: Configuration file containing the instructions for DatasetPreprocessor.
- `results_images/`: A folder containing the charts of the metrics analyzed.
- `results_metrics.json`: The json file containing the results of the models for this dataset.

---

## Sample Data

An example of how the dataset is structured:

| **lettr** | x-box | y-box | width | height | onpix | x-bar | y-bar | x2bar | y2bar | xybar | x2ybr | xy2br | x-ege | xegvy | y-ege | yegvx |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **T** | 2 | 8 | 3 | 5 | 1 | 8 | 13 | 0 | 6 | 6 | 10 | 8 | 0 | 8 | 0 | 8 |
| **I** | 5 | 12 | 3 | 7 | 2 | 10 | 5 | 5 | 4 | 13 | 3 | 9 | 2 | 8 | 4 | 10 |
| **D** | 4 | 11 | 6 | 8 | 6 | 10 | 6 | 2 | 6 | 10 | 3 | 7 | 3 | 7 | 3 | 9 |

---

## Performance Metrics

| Classifier | Accuracy | Balanced Accuracy | Micro F1 | Macro F1 | Training Time | Prediction Time | Total Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Random Forest | 94.9% | 95.0% | 94.9% | 95.0% | 0.366s | 0.030s | 0.396s |
| ***Extra Trees*** | ***96.0%*** | ***96.1%*** | ***96.0%*** | ***96.1%*** | 0.282s | 0.034s | 0.316s |
| XGBoost | 93.5% | 93.6% | 93.5% | 93.6% | 0.373s | 0.007s | 0.381s |
| AdaBoost | 16.5% | 16.8% | 16.5% | 11.6% | 0.203s | 0.037s | 0.240s |
| Gradient Boosting | 81.8% | 81.9% | 81.8% | 82.2% | 9.922s | 0.052s | 9.974s |
| SimilarityForest[cityblock] | 84.2% | 84.3% | 84.2% | 84.3% | 0.349s | 0.044s | 0.393s |
| SimilarityForest[cosine] | 83.3% | 83.4% | 83.3% | 83.4% | 0.282s | 0.048s | 0.330s |
| SimilarityForest[euclidean] | 84.1% | 84.1% | 84.1% | 84.2% | 0.258s | 0.051s | 0.309s |
| SimilarityForest[braycurtis] | 84.8% | 84.9% | 84.8% | 84.9% | 0.281s | 0.046s | 0.327s |
| SimilarityForest[canberra] | 84.3% | 84.4% | 84.3% | 84.4% | 0.296s | 0.044s | 0.340s |
| SimilarityForest[chebyshev] | 83.9% | 84.0% | 83.9% | 84.0% | 0.270s | 0.045s | 0.315s |
| SimilarityForest[correlation] | 83.3% | 83.4% | 83.3% | 83.4% | 0.273s | 0.050s | 0.323s |
| SimilarityForest[hamming] | 83.4% | 83.5% | 83.4% | 83.5% | 0.273s | 0.043s | 0.316s |

---

## Acknowledgments

Slate, D. (1991). Letter Recognition [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5ZP40.

Frey, P. W., & Slate, D. J. (1991). Letter recognition using Holland-style adaptive classifiers. Machine Learning, 6(2), 161-182.