# Seismic Bumps

**Description**:

The data describe the problem of high energy (higher than 10^4 J) seismic bumps forecasting in a coal mine. Data come from two of longwalls located in a Polish coal mine.

---

## Table of Contents
- [Seismic Bumps](#seismic-bumps)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Seismic Bumps](https://archive.ics.uci.edu/dataset/266/seismic+bumps)

- **Domain**: Other

- **Format**: CSV

---

## Variables

| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***seismic*** | Feature | Seismic activity level (a = lack of hazard, b = low hazard, c = high hazard, d = danger state) | Categorical | a, b, c, d |
| ***seismoacoustic*** | Feature | Seismoacoustic activity level | Categorical | a, b, c, d |
| ***shift*** | Feature | Shift during which the measurement was taken | Categorical | W, N |
| ***genergy*** | Feature | Energy of the seismic event | Continuous | - |
| ***gpuls*** | Feature | Number of pulses in the seismic event | Continuous | - |
| ***gdenergy*** | Feature | Energy of the seismic event divided by the duration | Continuous | - |
| ***gdpuls*** | Feature | Number of pulses divided by the duration | Continuous | - |
| ***ghazard*** | Feature | Hazard level of the seismic event | Categorical | a, b, c, d |
| ***nbumps*** | Feature | Number of bumps in the seismic event | Continuous | - |
| ***nbumps2*** | Feature | Number of bumps in the seismic event in the last 2 hours | Continuous | - |
| ***nbumps3*** | Feature | Number of bumps in the seismic event in the last 3 hours | Continuous | - |
| ***nbumps4*** | Feature | Number of bumps in the seismic event in the last 4 hours | Continuous | - |
| ***nbumps5*** | Feature | Number of bumps in the seismic event in the last 5 hours | Continuous | - |
| ***nbumps6*** | Feature | Number of bumps in the seismic event in the last 6 hours | Continuous | - |
| ***nbumps7*** | Feature | Number of bumps in the seismic event in the last 7 hours | Continuous | - |
| ***nbumps89*** | Feature | Number of bumps in the seismic event in the last 8 hours | Continuous | - |
| ***energy*** | Feature | total energy of seismic bumps registered within previous shift | Continuous | - |
| ***maxenergy*** | Feature | the maximum energy of the seismic bumps registered within previous shift | Continuous | - |
| ***class*** | **Target** | Occurrence of dangerous seismic bumps: "1" means that high energy seismic bump occurred in the next shift ('hazardous state'), "0" means that no high energy seismic bumps occurred in the next shift ('non-hazardous state'). | Categorical | "0", "1" |

---

## Target Variable

- **Name**: *class*
- **Type**: Categorical
- **Values**:
  - 0 = No dangerous seismic bump
  - 1 = Dangerous seismic bump

---

## Dataset Details

- **Has missing values?**: no
- **Number of Instances**: 2584 instances
- **Number of Features**: 18
- **Class Distribution**:
  - 0 = 2414 instances
  - 1 = 170 instances

---

## File Structure

- `seismic_bumps.csv`: Main dataset file.
- `README.md`: Documentation file (this file).
- `configuration.json`: Configuration file containing the instructions for DatasetPreprocessor.
- `results_images/`: A folder containing the charts of the metrics analyzed.
- `results_metrics.json`: The json file containing the results of the models for this dataset.

---

## Sample Data

An example of how the dataset is structured:

| seismic | seismoacoustic | shift | genergy | gpuls | gdenergy | gdpuls | ghazard | nbumps | nbumps2 | nbumps3 | nbumps4 | nbumps5 | nbumps6 | nbumps7 | nbumps89 | energy | maxenergy | ***class*** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| b | a | W | 48980.0 | 1007.0 | 54.0 | 21.0 | a | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | ***0*** |
| b | a | W | 76610.0 | 987.0 | 141.0 | 19.0 | a | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | ***0*** |
| b | a | W | 99010.0 | 1360.0 | 82.0 | 62.0 | a | 3.0 | 1.0 | 2.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 4200.0 | 2000.0 | ***1*** |

---

## Performance Metrics

| Classifier | Accuracy | Balanced Accuracy | Micro F1 | Macro F1 | Training Time | Prediction Time | Total Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Random Forest | 93.3% | 50.8% | 93.3% | 50.1% | 0.048s | 0.002s | 0.051s |
| Extra Trees | 92.8% | 50.5% | 92.8% | 49.8% | 0.035s | 0.003s | 0.038s |
| XGBoost | 93.3% | 52.7% | 93.3% | 53.4% | 0.021s | 0.001s | 0.022s |
| ***AdaBoost*** | ***93.6%*** | 50.0% | ***93.6%*** | 48.3% | 0.063s | 0.004s | 0.066s |
| Gradient Boosting | 92.9% | 50.6% | 92.9% | 49.9% | 0.085s | 0.001s | 0.086s |
| ***SimilarityForest[cityblock]*** | 86.3% | ***59.2%*** | 86.3% | ***56.7%*** | 0.086s | 0.006s | 0.092s |
| SimilarityForest[cosine] | 87.8% | 53.4% | 87.8% | 53.1% | 0.025s | 0.004s | 0.029s |
| SimilarityForest[euclidean] | 87.0% | 57.7% | 87.0% | 56.1% | 0.023s | 0.004s | 0.026s |
| SimilarityForest[braycurtis] | 88.5% | 53.8% | 88.5% | 53.7% | 0.033s | 0.004s | 0.037s |
| SimilarityForest[canberra] | 86.3% | 52.7% | 86.3% | 52.1% | 0.036s | 0.004s | 0.041s |
| SimilarityForest[chebyshev] | 90.7% | 52.2% | 90.7% | 52.6% | 0.022s | 0.003s | 0.026s |
| SimilarityForest[correlation] | 86.7% | 51.0% | 86.7% | 50.8% | 0.035s | 0.004s | 0.039s |
| SimilarityForest[hamming] | 89.6% | 54.4% | 89.6% | 54.6% | 0.024s | 0.004s | 0.028s |

---

## Acknowledgments

Sikora, M. & Wrobel, L. (2010). seismic-bumps [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5W902.
