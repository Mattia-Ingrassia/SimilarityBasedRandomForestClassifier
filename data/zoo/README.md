# Zoo

**Description**:  

A simple database containing 17 Boolean-valued attributes.  The "type" attribute appears to be the class attribute. 

---

## Table of Contents
- [Zoo](#zoo)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Zoo](https://archive.ics.uci.edu/dataset/111/zoo)
  
- **Domain**: Biology

- **Format**: CSV  

---

## Variables

| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***animal_name*** | ID | Name of the animal | Categorical | - |
| ***hair*** | Feature | Presence of hair | Binary | 0, 1 |
| ***feathers*** | Feature | Presence of feathers | Binary | 0, 1 |
| ***eggs*** | Feature | Lays eggs | Binary | 0, 1 |
| ***milk*** | Feature | Produces milk | Binary | 0, 1 |
| ***airborne*** | Feature | Can fly | Binary | 0, 1 |
| ***aquatic*** | Feature | Lives in water | Binary | 0, 1 |
| ***predator*** | Feature | Is a predator | Binary | 0, 1 |
| ***toothed*** | Feature | Has teeth | Binary | 0, 1 |
| ***backbone*** | Feature | Has a backbone | Binary | 0, 1 |
| ***breathes*** | Feature | Breathes air | Binary | 0, 1 |
| ***venomous*** | Feature | Is venomous | Binary | 0, 1 |
| ***fins*** | Feature | Has fins | Binary | 0, 1 |
| ***legs*** | Feature | Number of legs | Integer | 0, 2, 4, 5, 6, 8 |
| ***tail*** | Feature | Has a tail | Binary | 0, 1 |
| ***domestic*** | Feature | Is domesticated | Binary | 0, 1 |
| ***catsize*** | Feature | Size relative to a cat | Binary | 0, 1 |
| ***class_type*** | **Target** | Type of animal | Categorical | 1, 2, 3, 4, 5, 6, 7 |

---

## Target Variable

- **Name**: *class_type*  
- **Type**: Categorical
- **Values**:
  - 1 = Mammal
  - 2 = Bird
  - 3 = Reptile
  - 4 = Fish
  - 5 = Amphibian
  - 6 = Insect
  - 7 = Other

---

## Dataset Details

- **Has missing values?**: no
- **Number of Instances**: 101 instances 
- **Number of Features**: 16
- **Class Distribution**:
  - 1 = Mammal = 41 instances
  - 2 = Bird = 20 instances
  - 3 = Reptile = 5 instances
  - 4 = Fish = 13 instances
  - 5 = Amphibian = 4 instances
  - 6 = Insect = 8 instances
  - 7 = Other = 10 instances
 
---

## File Structure

- `zoo.csv`: Main dataset file.  
- `README.md`: Documentation file (this file).  
- `configuration.json`: Configuration file containing the instructions for DatasetPreprocessor.  

---

## Sample Data

An example of how the dataset is structured:

| animal_name | hair | feathers | eggs | milk | airborne | aquatic | predator | toothed | backbone | breathes | venomous | fins | legs | tail | domestic | catsize | class_type |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cheetah | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 4 | 1 | 0 | 1 | **1** |
| chicken | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 2 | 1 | 1 | 0 | **2** |
| chub | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | **4** |

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

Forsyth, R. (1990). Zoo [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5R59V.