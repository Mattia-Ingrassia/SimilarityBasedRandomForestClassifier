# Tic-Tac-Toe

**Description**:  

This database encodes the complete set of possible board configurations at the end of tic-tac-toe games, where "x" is assumed to have played first.  The target concept is "win for x" (i.e., true when "x" has one of 8 possible ways to create a "three-in-a-row").  

---

## Table of Contents
- [Tic-Tac-Toe](#tic-tac-toe)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Tic-Tac-Toe Endgame](https://archive.ics.uci.edu/dataset/101/tic+tac+toe+endgame)
  
- **Domain**: Games

- **Format**: CSV  

---

## Variables

| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***top-left-square*** | Feature | Value of the top-left square | Categorical | x, o, b |
| ***top-middle-square*** | Feature | Value of the top-middle square | Categorical | x, o, b |
| ***top-right-square*** | Feature | Value of the top-right square | Categorical | x, o, b |
| ***middle-left-square*** | Feature | Value of the middle-left square | Categorical | x, o, b |
| ***middle-middle-square*** | Feature | Value of the middle-middle square | Categorical | x, o, b |
| ***middle-right-square*** | Feature | Value of the middle-right square | Categorical | x, o, b |
| ***bottom-left-square*** | Feature | Value of the bottom-left square | Categorical | x, o, b |
| ***bottom-middle-square*** | Feature | Value of the bottom-middle square | Categorical | x, o, b |
| ***bottom-right-square*** | Feature | Value of the bottom-right square | Categorical | x, o, b |
| ***class*** | **Target** | Whether the configuration is a win for the player about to move or not | Categorical | positive, negative |

---

## Target Variable

- **Name**: *class*  
- **Type**: Categorical
- **Values**:
  - positive = Win for the player about to move
  - negative = Not a win for the player about to move

---

## Dataset Details

- **Has missing values?**: no
- **Number of Instances**: 958 instances 
- **Number of Features**: 9
- **Class Distribution**:
  - positive = 626 instances
  - negative = 332 instances
 
---

## File Structure

- `tic_tac_toe.csv`: Main dataset file.  
- `README.md`: Documentation file (this file).  
- `configuration.json`: Configuration file containing the instructions for DatasetPreprocessor.  

---

## Sample Data

| top-left-square | top-middle-square | top-right-square | middle-left-square | middle-middle-square | middle-right-square | bottom-left-square | bottom-middle-square | bottom-right-square | class |
|---|---|---|---|---|---|---|---|---|---|
| b | b | b | o | b | o | x | x | x | positive |
| b | b | b | b | o | o | x | x | x | positive |
| x | x | o | x | x | o | o | b | o | negative |

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

Aha, D. (1991). Tic-Tac-Toe Endgame [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5688J.