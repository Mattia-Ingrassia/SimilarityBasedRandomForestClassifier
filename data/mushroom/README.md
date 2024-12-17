# Mushroom

**Description**:

This data set includes descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms in the Agaricus and Lepiota Family (pp. 500-525).

Each species is identified as definitely edible, definitely poisonous, or of unknown edibility and not recommended.

This latter class was combined with the poisonous one.

The Guide clearly states that there is no simple rule for determining the edibility of a mushroom.


---

## Table of Contents
- [Mushroom](#mushroom)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Mushroom](https://archive.ics.uci.edu/dataset/73/mushroom)

- **Domain**: Biology

- **Format**: CSV

---

## Variables

| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***class*** | **Target** | Edibility of the mushroom | Categorical | edible=e, poisonous=p |
| ***cap-shape*** | Feature | Shape of the cap | Categorical | bell=b, conical=c, convex=x, flat=f, knobbed=k, sunken=s |
| ***cap-surface*** | Feature | Surface of the cap | Categorical | fibrous=f, grooves=g, scaly=y, smooth=s |
| ***cap-color*** | Feature | Color of the cap | Categorical | brown=n, buff=b, cinnamon=c, gray=g, green=r, pink=p, purple=u, red=e, white=w, yellow=y |
| ***bruises*** | Feature | Whether the mushroom bruises | Categorical | bruises=t, no=f |
| ***odor*** | Feature | Odor of the mushroom | Categorical | almond=a, anise=l, creosote=c, fishy=y, foul=f, musty=m, none=n, pungent=p, spicy=s |
| ***gill-attachment*** | Feature | Gill attachment to the cap | Categorical | attached=a, descending=d, free=f, notched=n |
| ***gill-spacing*** | Feature | Spacing of the gills | Categorical | close=c, crowded=w, distant=d |
| ***gill-size*** | Feature | Size of the gills | Categorical | broad=b, narrow=n |
| ***gill-color*** | Feature | Color of the gills | Categorical | black=k, brown=n, buff=b, chocolate=h, gray=g, green=r, orange=o, pink=p, purple=u, red=e, white=w, yellow=y |
| ***stalk-shape*** | Feature | Shape of the stalk | Categorical | enlarging=e, tapering=t |
| ***stalk-root*** | Feature | Root of the stalk | Categorical | bulbous=b, club=c, cup=u, equal=e, rhizomorphs=z, rooted=r, missing=? |
| ***stalk-surface-above-ring*** | Feature | Surface of the stalk above the ring | Categorical | {fibrous=f, scaly=y, silky=k, smooth=s} |
| ***stalk-surface-below-ring*** | Feature | Surface of the stalk below the ring | Categorical | fibrous=f, scaly=y, silky=k, smooth=s |
| ***stalk-color-above-ring*** | Feature | Color of the stalk above the ring | Categorical | brown=n, buff=b, cinnamon=c, gray=g, orange=o, pink=p, red=e, white=w, yellow=y |
| ***stalk-color-below-ring*** | Feature | Color of the stalk below the ring | Categorical | brown=n, buff=b, cinnamon=c, gray=g, orange=o, pink=p, red=e, white=w, yellow=y |
| ***veil-type*** | Feature | Type of veil | Categorical | partial=p, universal=u |
| ***veil-color*** | Feature | Color of the veil | Categorical | brown=n, orange=o, white=w, yellow=y |
| ***ring-number*** | Feature | Number of rings | Categorical | none=n, one=o, two=t |
| ***ring-type*** | Feature | Type of ring | Categorical | cobwebby=c, evanescent=e, flaring=f, large=l, none=n, pendant=p, sheathing=s, zone=z |
| ***spore-print-color*** | Feature | Color of the spore print | Categorical | black=k, brown=n, buff=b, chocolate=h, green=r, orange=o, purple=u, white=w, yellow=y |
| ***population*** | Feature | Population size | Categorical | abundant=a, clustered=c, numerous=n, scattered=s, several=v, solitary=y |
| ***habitat*** | Feature | Habitat of the mushroom | Categorical | grasses=g, leaves=l, meadows=m, paths=p, urban=u, waste=w, woods=d |

---

## Target Variable

- **Name**: *class*
- **Type**: Categorical
- **Values**:
  - e for edible
  - p for poisonous

---

## Dataset Details

- **Has missing values?**: Yes - marked with "?" (only in stalk-root)
- **Number of Instances**:
  - with missing values: 8124 instances
  - without missing values: 5644 instances
- **Number of Features**: 22
- **Class Distribution**:
  - with missing values: p (poisonus): 3916 instances, e (edible): 4208
  - without missing values: p (poisonus): 2156 instances, e (edible): 3488 instances

---

## File Structure

- `mushroom.csv`: Main dataset file.
- `README.md`: Documentation file (this file).
- `configuration.json`: Configuration file containing the instructions for DatasetPreprocessor.
- `results_images/`: A folder containing the charts of the metrics analyzed.
- `results_metrics.json`: The json file containing the results of the models for this dataset.

---

## Sample Data

An example of how the dataset is structured:

| ***class*** | cap-shape | cap-surface | cap-color | bruises | odor | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | stalk-root | stalk-surface-above-ring | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ***p*** | x | s | n | t | p | f | c | n | k | e | e | s | s | w | w | p | w | o | p | k | s | u |
| ***e*** | x | s | y | t | a | f | c | b | k | e | c | s | s | w | w | p | w | o | p | n | n | g |
| ***e*** | b | s | w | t | l | f | c | b | n | e | c | s | s | w | w | p | w | o | p | n | n | m |

---

## Performance Metrics

| Classifier | Accuracy | Balanced Accuracy | Micro F1 | Macro F1 | Training Time | Prediction Time | Total Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Random Forest | 100.0% | 100.0% | 100.0% | 100.0% | 0.041s | 0.003s | 0.044s |
| Extra Trees | 100.0% | 100.0% | 100.0% | 100.0% | 0.039s | 0.003s | 0.042s |
| XGBoost | 100.0% | 100.0% | 100.0% | 100.0% | 0.023s | 0.001s | 0.024s |
| AdaBoost | 99.8% | 99.8% | 99.8% | 99.8% | 0.125s | 0.008s | 0.133s |
| Gradient Boosting | 100.0% | 100.0% | 100.0% | 100.0% | 0.154s | 0.001s | 0.155s |
| SimilarityForest[cityblock] | 100.0% | 100.0% | 100.0% | 100.0% | 0.161s | 0.010s | 0.171s |
| SimilarityForest[cosine] | 100.0% | 100.0% | 100.0% | 100.0% | 0.157s | 0.008s | 0.166s |
| SimilarityForest[euclidean] | 100.0% | 100.0% | 100.0% | 100.0% | 0.159s | 0.008s | 0.166s |
| SimilarityForest[braycurtis] | 100.0% | 100.0% | 100.0% | 100.0% | 0.155s | 0.011s | 0.166s |
| SimilarityForest[canberra] | 100.0% | 100.0% | 100.0% | 100.0% | 0.157s | 0.011s | 0.168s |
| SimilarityForest[chebyshev] | 100.0% | 100.0% | 100.0% | 100.0% | 0.147s | 0.009s | 0.156s |
| SimilarityForest[correlation] | 100.0% | 100.0% | 100.0% | 100.0% | 0.178s | 0.009s | 0.187s |
| SimilarityForest[hamming] | 100.0% | 100.0% | 100.0% | 100.0% | 0.179s | 0.010s | 0.189s |

---

## Acknowledgments

Mushroom [Dataset]. (1981). UCI Machine Learning Repository. https://doi.org/10.24432/C5959T.
