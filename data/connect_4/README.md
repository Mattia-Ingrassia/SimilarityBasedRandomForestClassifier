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
- `results_images/`: A folder containing the charts of the metrics analyzed.
- `results_metrics.json`: The json file containing the results of the models for this dataset.

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

| Classifier | Accuracy | Balanced Accuracy | Micro F1 | Macro F1 | Training Time | Prediction Time | Total Time |
|---|---|---|---|---|---|---|---|
| Random Forest | 82.2% | 61.0% | 82.2% | 62.9% | 1.379s | 0.106s | 1.484s |
| ***Extra Trees*** | ***82.3%*** | ***62.4%*** | ***82.3%*** | ***64.3%*** | 1.913s | 0.120s | 2.033s |
| XGBoost | 80.1% | 55.4% | 80.1% | 55.0% | 0.210s | 0.007s | 0.217s |
| AdaBoost | 69.9% | 39.9% | 69.9% | 38.5% | 1.982s | 0.185s | 2.167s |
| Gradient Boosting | 71.9% | 42.1% | 71.9% | 41.4% | 11.422s | 0.048s | 11.471s |
| SimilarityForest[cityblock] | 74.0% | 58.0% | 74.0% | 58.0% | 2.891s | 0.271s | 3.162s |
| SimilarityForest[cosine] | 74.1% | 58.1% | 74.1% | 58.0% | 3.308s | 0.281s | 3.589s |
| SimilarityForest[euclidean] | 73.3% | 57.5% | 73.3% | 57.4% | 3.268s | 0.279s | 3.547s |
| SimilarityForest[braycurtis] | 74.1% | 58.1% | 74.1% | 58.0% | 3.001s | 0.279s | 3.280s |
| SimilarityForest[canberra] | 74.0% | 58.0% | 74.0% | 58.0% | 2.940s | 0.427s | 3.367s |
| SimilarityForest[chebyshev] | 74.2% | 58.2% | 74.2% | 58.2% | 2.386s | 0.234s | 2.620s |
| SimilarityForest[correlation] | 73.8% | 57.9% | 73.8% | 57.8% | 2.280s | 0.219s | 2.499s |
| SimilarityForest[hamming] | 73.6% | 57.8% | 73.6% | 57.7% | 2.231s | 0.225s | 2.456s |

---

## Acknowledgments

Tromp, J. (1995). Connect-4 [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C59P43.


