# Bank

**Description**:  

The data is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed. 

---

## Table of Contents
- [Bank](#bank)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing)
  
- **Domain**: Business

- **Format**: CSV

---

## Variables

| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| - | - | - | - | - |
| ***age*** | Feature | Age of the individual | Integer | - |
| ***job*** | Feature | Job of the individual | Categorical | admin, blue-collar, entrepreneur, housemaid, management, retired, self-employed, services, student, technician, unemployed, unknown |
| ***marital*** | Feature | Marital status | Categorical | divorced, married, single, unknown |
| ***education*** | Feature | Education level | Categorical | basic.4y , basic.6y , basic.9y , high.school , illiterate , professional.course , university.degree , unknown	|
| ***default*** | Feature | Has credit in default? | Categorical | yes, no |
| ***balance*** | Feature | Average yearly balance | Integer | - |
| ***housing*** | Feature | Has housing loan? | Categorical | yes, no |
| ***loan*** | Feature | Has personal loan? | Categorical | yes, no |
| ***contact*** | Feature | Contact communication type | Categorical | cellular, telephone |
| ***day_of_week*** | Feature | Last contact day of the week | Integer | 1-31 |
| ***month*** | Feature | Last contact month of year | Categorical | jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec |
| ***duration*** | Feature | Last contact duration, in seconds (numeric). Important note: this attribute highly affects the output target (e.g., if duration=0 then target='no'). Yet, the duration is not known before a call is performed. Also, after the end of the call y is obviously known. Thus, this input should only be included for benchmark purposes and should be discarded if the intention is to have a realistic predictive model. | Integer | - |
| ***campaign*** | Feature | Number of contacts performed during this campaign and for this client (numeric, includes last contact)	| Integer | - |
| ***pdays*** | Feature | number of days that passed by after the client was last contacted from a previous campaign (numeric; -1 means client was not previously contacted) | Integer | - |
| ***previous*** | Feature | Number of contacts performed before this campaign and for this client | Integer | - |
| ***poutcome*** | Feature | Outcome of the previous marketing campaign | Categorical | failure, nonexistent, success | - |
| ***y*** | **Target** | Has the client subscribed a term deposit? | Categorical | yes, no |

---

## Target Variable

- **Name**: **y**
- **Type**: Categorical  
- **Values**: yes, no  

---

## Dataset Details

- **Has missing values?**: yes - marked with unknown
- **Number of Instances**:
  - with missing values: 45211 instances
  - without missing values: 7842 instances 
- **Number of Features**: 16
- **Class Distribution**:
  - with missing values: no: 39922 , yes: 5289
  - without missing values: no: 6056, yes: 1786
 
---

## File Structure

- `bank.csv`: Main dataset file.  
- `README.md`: Documentation file (this file).  
- `configuration.json`: Configuration file containing the istructions for DatasetPreprocessor.  

---

## Sample Data


An example of how the dataset is structured:

| age | job | marital | education | default | balance | housing | loan | contact | day_of_week  | month | duration | campaign | pdays | previous | poutcome | **y** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 44 | entrepreneur | married | tertiary | no | 3463 | yes | yes | cellular | 28 | jan | 290 | 2 | 153 | 3 | failure | no |
33 | services | married | secondary | no | 3444 | yes | no | telephone | 21 | oct | 144 | 1 | 91 | 4 | failure | yes |
34 | management | single | tertiary | no | 1494 | yes | no | cellular | 18 | nov | 596 | 1 | 182 | 1 | other | yes |


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

This dataset is publicly available for research purposes and was created by Paulo Cortez (University of Minho) and Sérgio Moro (ISCTE-IUL) in 2012. It contains data related to direct marketing campaigns of a Portuguese banking institution. 

Moro, S., Rita, P., & Cortez, P. (2014). Bank Marketing [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5K306.

