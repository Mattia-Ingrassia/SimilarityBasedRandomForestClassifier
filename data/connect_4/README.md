# Connect_4

**Description**:  

This database contains all legal 8-ply positions in the game of connect-4 in which neither player has won yet, and in which the next move is not forced.

x is the first player; o the second.

The outcome class is the game theoretical value for the first player.

---

## Table of Contents
- [Connect\_4](#connect_4)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Connect-4](https://archive.ics.uci.edu/dataset/26/connect+4)
  
- **Domain**: Games

- **Format**: CSV  

---

## Variables

List the features (columns) in the dataset along with descriptions, data types, and possible values. Example:


| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***a1*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***a2*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***a3*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***a4*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***a5*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***a6*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***b1*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***b2*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***b3*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***b4*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***b5*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***b6*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***c1*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***c2*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***c3*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***c4*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***c5*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***c6*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***d1*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***d2*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***d3*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***d4*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***d5*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***d6*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***e1*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***e2*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***e3*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***e4*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***e5*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***e6*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***f1*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***f2*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***f3*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***f4*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***f5*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***f6*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***g1*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***g2*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***g3*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***g4*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***g5*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***g6*** | Feature | b=blank, x=player1, o=player2 | Categorical | b, x, o |
| ***class*** | **Target** | Result of the match: win, loss, draw | Categorical | win, loss, draw |

---

## Target Variable

- **Name**:class.  
- **Type**: Categorical.  
- **Values**:
  - win = player 1 (x) win
  - draw = draw
  - loss = player 2 (o) win  

---

## Dataset Details

- **Has missing values?**: no 
- **Number of Instances**: 67557 instances 
- **Number of Features**: 42
- **Class Distribution**:
  - win: 44473 instances
  - draw: 6449 instances
  - loss: 16635 instances
 
---

## File Structure

- `connect_4.csv`: Main dataset file.  
- `README.md`: Documentation file (this file).  
- `configuration.json`: Configuration file containing the istructions for DatasetPreprocessor.  

---

## Sample Data

An example of how the dataset is structured:

| a1 | a2 | a3 | a4 | a5 | a6 | b1 | b2 | b3 | b4 | b5 | b6 | c1 | c2 | c3 | c4 | c5 | c6 | d1 | d2 | d3 | d4 | d5 | d6 | e1 | e2 | e3 | e4 | e5 | e6 | f1 | f2 | f3 | f4 | f5 | f6 | g1 | g2 | g3 | g4 | g5 | g6 | class |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| b | b | b | b | b | b | b | b | b | b | b | b | o | o | b | b | b | b | x | o | x | o | x | b | x | b | b | b | b | b | b | b | b | b | b | b | b | b | b | b | b | b | loss |
| b | b | b | b | b | b | b | b | b | b | b | b | o | b | b | b | b | b | x | o | x | o | x | b | x | o | b | b | b | b | b | b | b | b | b | b | b | b | b | b | b | b | draw |
| b | b | b | b | b | b | o | b | b | b | b | b | o | b | b | b | b | b | x | o | x | o | x | b | x | b | b | b | b | b | b | b | b | b | b | b | b | b | b | b | b | b | win |

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

Tromp, J. (1995). Connect-4 [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C59P43.


