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

---

## Sample Data

| seismic | seismoacoustic | shift | genergy | gpuls | gdenergy | gdpuls | ghazard | nbumps | nbumps2 | nbumps3 | nbumps4 | nbumps5 | nbumps6 | nbumps7 | nbumps89 | energy | maxenergy | ***class*** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| b | a | W | 48980.0 | 1007.0 | 54.0 | 21.0 | a | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | ***0*** |
| b | a | W | 76610.0 | 987.0 | 141.0 | 19.0 | a | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | ***0*** |
| b | a | W | 99010.0 | 1360.0 | 82.0 | 62.0 | a | 3.0 | 1.0 | 2.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 4200.0 | 2000.0 | ***1*** |

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

Sikora, M. & Wrobel, L. (2010). seismic-bumps [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5W902.
