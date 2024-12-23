# Poker Hand

**Description**:

Each record is an example of a hand consisting of five playing cards drawn from a standard deck of 52. Each card is described using two attributes (suit and rank), for a total of 10 predictive attributes. There is one Class attribute that describes the "Poker Hand". The order of cards is important, which is why there are 480 possible Royal Flush hands as compared to 4 (one for each suit)

---

## Table of Contents
- [Poker Hand](#poker-hand)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Poker Hand](https://archive.ics.uci.edu/dataset/158/poker+hand)

- **Domain**: Games

- **Format**: CSV

---

## Variables

| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***S1*** | Feature | Suit of card 1 | Categorical | 1=Hearts, 2=Spades, 3=Diamonds, 4=Clubs |
| ***C1*** | Feature | Rank of card 1 | Integer | 1-13 (1=Ace, 11=Jack, 12=Queen, 13=King) |
| ***S2*** | Feature | Suit of card 2 | Categorical | 1=Hearts, 2=Spades, 3=Diamonds, 4=Clubs |
| ***C2*** | Feature | Rank of card 2 | Integer | 1-13 (1=Ace, 11=Jack, 12=Queen, 13=King) |
| ***S3*** | Feature | Suit of card 3 | Categorical | 1=Hearts, 2=Spades, 3=Diamonds, 4=Clubs |
| ***C3*** | Feature | Rank of card 3 | Integer | 1-13 (1=Ace, 11=Jack, 12=Queen, 13=King) |
| ***S4*** | Feature | Suit of card 4 | Categorical | 1=Hearts, 2=Spades, 3=Diamonds, 4=Clubs |
| ***C4*** | Feature | Rank of card 4 | Integer | 1-13 (1=Ace, 11=Jack, 12=Queen, 13=King) |
| ***S5*** | Feature | Suit of card 5 | Categorical | 1=Hearts, 2=Spades, 3=Diamonds, 4=Clubs |
| ***C5*** | Feature | Rank of card 5 | Integer | 1-13 (1=Ace, 11=Jack, 12=Queen, 13=King) |
| ***hand*** | **Target** | Poker hand | Categorical | 0=Nothing, 1=One pair, 2=Two pairs, 3=Three of a kind, 4=Straight, 5=Flush, 6=Full house, 7=Four of a kind, 8=Straight flush, 9=Royal flush |

---

## Target Variable

- **Name**: *hand*
- **Type**: Categorical
- **Values**:
  - 0 = Nothing
  - 1 = One pair
  - 2 = Two pairs
  - 3 = Three of a kind
  - 4 = Straight
  - 5 = Flush
  - 6 = Full house
  - 7 = Four of a kind
  - 8 = Straight flush
  - 9 = Royal flush

---

## Dataset Details

- **Has missing values?**: no
- **Number of Instances**: 1025010 instances
- **Number of Features**: 10
- **Class Distribution**:
  - 0 = Nothing = 513702 instances
  - 1 = One pair = 433097 instances
  - 2 = Two pairs = 48828 instances
  - 3 = Three of a kind = 21634 instances
  - 4 = Straight = 3978 instances
  - 5 = Flush = 2050 instances
  - 6 = Full house = 1460 instances
  - 7 = Four of a kind = 236 instances
  - 8 = Straight flush = 17 instances
  - 9 = Royal flush = 8 instances

---

## File Structure

- `poker_hand.csv`: Main dataset file.
- `README.md`: Documentation file (this file).
- `configuration.json`: Configuration file containing the instructions for DatasetPreprocessor.
- `results_images/`: A folder containing the charts of the metrics analyzed.
- `results_metrics.json`: The json file containing the results of the models for this dataset.

---

## Sample Data

An example of how the dataset is structured:

| S1 | C1 | S2 | C2 | S3 | C3 | S4 | C4 | S5 | C5 | hand |
|----|----|----|----|----|----|----|----|----|----|------|
| 3 | 10 | 4 | 10 | 3 | 1 | 1 | 1 | 2 | 12 | 2 |
| 3 | 7 | 4 | 5 | 3 | 12 | 3 | 5 | 3 | 4 | 1 |
| 1 | 13 | 1 | 6 | 1 | 4 | 2 | 12 | 4 | 8 | 0 |

---

## Performance Metrics

| Classifier | Accuracy | Balanced Accuracy | Micro F1 | Macro F1 | Training Time | Prediction Time | Total Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ***Random Forest*** | ***73.3%*** | 17.9% | ***73.3%*** | 19.2% | 23.629s | 3.150s | 26.779s |
| Extra Trees | 71.4% | 19.5% | 71.4% | 21.7% | 22.184s | 3.761s | 25.945s |
| XGBoost | 66.1% | 17.3% | 66.1% | 19.0% | 2.552s | 0.088s | 2.639s |
| AdaBoost | 44.2% | 10.0% | 44.2% | 8.7% | 8.034s | 0.824s | 8.858s |
| Gradient Boosting | 57.3% | 14.8% | 57.3% | 15.6% | 179.922s | 1.245s | 181.167s |
| SimilarityForest[cityblock] | 62.8% | 24.4% | 62.8% | 23.7% | 12.637s | 3.102s | 15.739s |
| SimilarityForest[cosine] | 62.2% | 23.8% | 62.2% | 23.0% | 12.496s | 3.187s | 15.684s |
| SimilarityForest[euclidean] | 63.3% | 24.3% | 63.3% | 23.5% | 12.297s | 3.218s | 15.515s |
| SimilarityForest[braycurtis] | 62.1% | 24.3% | 62.1% | 23.3% | 12.737s | 3.305s | 16.042s |
| SimilarityForest[canberra] | 62.6% | 24.7% | 62.6% | 23.9% | 13.060s | 3.333s | 16.392s |
| SimilarityForest[chebyshev] | 64.0% | 24.7% | 64.0% | 23.9% | 14.285s | 3.380s | 17.665s |
| ***SimilarityForest[correlation]*** | 62.1% | ***25.6%*** | 62.1% | ***24.6%*** | 12.506s | 3.269s | 15.775s |
| SimilarityForest[hamming] | 61.9% | 25.5% | 61.9% | 24.8% | 14.699s | 3.351s | 18.050s |

---

## Acknowledgments

Cattral, R. & Oppacher, F. (2002). Poker Hand [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5KW38.