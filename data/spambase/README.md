# Spambase

**Description**:  

This dataset contains information about emails, with the goal of classifying them as spam or non-spam based on various attributes extracted from the email content.

---

## Table of Contents
- [Spambase](#spambase)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Spambase](https://archive.ics.uci.edu/ml/datasets/Spambase)
  
- **Domain**: Email Filtering

- **Format**: CSV  

---

## Variables

List the features (columns) in the dataset along with descriptions, data types, and possible values. Example:

| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***word_freq_make*** | Feature | Frequency of the word "make" | Continuous | - |
| ***word_freq_address*** | Feature | Frequency of the word "address" | Continuous | - |
| ***word_freq_all*** | Feature | Frequency of the word "all" | Continuous | - |
| ***word_freq_3d*** | Feature | Frequency of the word "3d" | Continuous | - |
| ***word_freq_our*** | Feature | Frequency of the word "our" | Continuous | - |
| ***word_freq_over*** | Feature | Frequency of the word "over" | Continuous | - |
| ***word_freq_remove*** | Feature | Frequency of the word "remove" | Continuous | - |
| ***word_freq_internet*** | Feature | Frequency of the word "internet" | Continuous | - |
| ***word_freq_order*** | Feature | Frequency of the word "order" | Continuous | - |
| ***word_freq_mail*** | Feature | Frequency of the word "mail" | Continuous | - |
| ***word_freq_receive*** | Feature | Frequency of the word "receive" | Continuous | - |
| ***word_freq_will*** | Feature | Frequency of the word "will" | Continuous | - |
| ***word_freq_people*** | Feature | Frequency of the word "people" | Continuous | - |
| ***word_freq_report*** | Feature | Frequency of the word "report" | Continuous | - |
| ***word_freq_addresses*** | Feature | Frequency of the word "addresses" | Continuous | - |
| ***word_freq_free*** | Feature | Frequency of the word "free" | Continuous | - |
| ***word_freq_business*** | Feature | Frequency of the word "business" | Continuous | - |
| ***word_freq_email*** | Feature | Frequency of the word "email" | Continuous | - |
| ***word_freq_you*** | Feature | Frequency of the word "you" | Continuous | - |
| ***word_freq_credit*** | Feature | Frequency of the word "credit" | Continuous | - |
| ***word_freq_your*** | Feature | Frequency of the word "your" | Continuous | - |
| ***word_freq_font*** | Feature | Frequency of the word "font" | Continuous | - |
| ***word_freq_000*** | Feature | Frequency of the word "000" | Continuous | - |
| ***word_freq_money*** | Feature | Frequency of the word "money" | Continuous | - |
| ***word_freq_hp*** | Feature | Frequency of the word "hp" | Continuous | - |
| ***word_freq_hpl*** | Feature | Frequency of the word "hpl" | Continuous | - |
| ***word_freq_george*** | Feature | Frequency of the word "george" | Continuous | - |
| ***word_freq_650*** | Feature | Frequency of the word "650" | Continuous | - |
| ***word_freq_lab*** | Feature | Frequency of the word "lab" | Continuous | - |
| ***word_freq_labs*** | Feature | Frequency of the word "labs" | Continuous | - |
| ***word_freq_telnet*** | Feature | Frequency of the word "telnet" | Continuous | - |
| ***word_freq_857*** | Feature | Frequency of the word "857" | Continuous | - |
| ***word_freq_data*** | Feature | Frequency of the word "data" | Continuous | - |
| ***word_freq_415*** | Feature | Frequency of the word "415" | Continuous | - |
| ***word_freq_85*** | Feature | Frequency of the word "85" | Continuous | - |
| ***word_freq_technology*** | Feature | Frequency of the word "technology" | Continuous | - |
| ***word_freq_1999*** | Feature | Frequency of the word "1999" | Continuous | - |
| ***word_freq_parts*** | Feature | Frequency of the word "parts" | Continuous | - |
| ***word_freq_pm*** | Feature | Frequency of the word "pm" | Continuous | - |
| ***word_freq_direct*** | Feature | Frequency of the word "direct" | Continuous | - |
| ***word_freq_cs*** | Feature | Frequency of the word "cs" | Continuous | - |
| ***word_freq_meeting*** | Feature | Frequency of the word "meeting" | Continuous | - |
| ***word_freq_original*** | Feature | Frequency of the word "original" | Continuous | - |
| ***word_freq_project*** | Feature | Frequency of the word "project" | Continuous | - |
| ***word_freq_re*** | Feature | Frequency of the word "re" | Continuous | - |
| ***word_freq_edu*** | Feature | Frequency of the word "edu" | Continuous | - |
| ***word_freq_table*** | Feature | Frequency of the word "table" | Continuous | - |
| ***word_freq_conference*** | Feature | Frequency of the word "conference" | Continuous | - |
| ***char_freq_;*** | Feature | Frequency of the character ';' | Continuous | - |
| ***char_freq_(*** | Feature | Frequency of the character '(' | Continuous | - |
| ***char_freq_[*** | Feature | Frequency of the character '[' | Continuous | - |
| ***char_freq_!*** | Feature | Frequency of the character '!' | Continuous | - |
| ***char_freq_$*** | Feature | Frequency of the character '$' | Continuous | - |
| ***char_freq_#*** | Feature | Frequency of the character '#' | Continuous | - |
| ***capital_run_length_average*** | Feature | Average length of uninterrupted sequences of capital letters | Continuous | - |
| ***capital_run_length_longest*** | Feature | Length of longest uninterrupted sequence of capital letters | Integer | - |
| ***capital_run_length_total*** | Feature | Total number of capital letters in the email | Integer | - |
| ***class*** | **Target** | Whether the email is spam (1) or not (0) | Binary | 0 / 1 |

---

## Target Variable

- **Name**: *class*  
- **Type**: Binary
- **Values**:
  - 0 = Non-spam
  - 1 = Spam

---

## Dataset Details

- **Has missing values?**: no
- **Number of Instances**: 4601 instances 
- **Number of Features**: 57
- **Class Distribution**:
  - 0 = Non-spam = 2788 instances
  - 1 = Spam = 1813 instances
 
---

## File Structure

- `spambase.csv`: Main dataset file.  
- `README.md`: Documentation file (this file).  
- `configuration.json`: Configuration file containing the instructions for DatasetPreprocessor.  

---

## Sample Data

| word_freq_make | word_freq_address | word_freq_all | word_freq_3d | word_freq_our | word_freq_over | word_freq_remove | word_freq_internet | word_freq_order | word_freq_mail | word_freq_receive | word_freq_will | word_freq_people | word_freq_report | word_freq_addresses | word_freq_free | word_freq_business | word_freq_email | word_freq_you | word_freq_credit | word_freq_your | word_freq_font | word_freq_000 | word_freq_money | word_freq_hp | word_freq_hpl | word_freq_george | word_freq_650 | word_freq_lab | word_freq_labs | word_freq_telnet | word_freq_857 | word_freq_data | word_freq_415 | word_freq_85 | word_freq_technology | word_freq_1999 | word_freq_parts | word_freq_pm | word_freq_direct | word_freq_cs | word_freq_meeting | word_freq_original | word_freq_project | word_freq_re | word_freq_edu | word_freq_table | word_freq_conference | char_freq_; | char_freq_( | char_freq_[ | char_freq_! | char_freq_$ | char_freq_# | capital_run_length_average | capital_run_length_longest | capital_run_length_total | class |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0.53 | 0 | 0.53 | 0 | 0.53 | 0 | 0 | 1.07 | 0 | 0 | 0 | 0 | 0 | 0 | 2.15 | 0 | 3.22 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.082 | 0 | 0 | 4.391 | 66 | 101 | 1 |
| 0 | 0.31 | 0.42 | 0 | 0 | 0.1 | 0 | 0.52 | 0.21 | 0.52 | 0 | 0.52 | 0.63 | 0.1 | 0.1 | 0.21 | 0.31 | 0.21 | 2.53 | 0.42 | 1.69 | 0.31 | 0 | 0.1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.1 | 0 | 0 | 0 | 0 | 0.016 | 0 | 0.887 | 0.032 | 0.049 | 3.446 | 318 | 1003 | 1 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.022 | 0.022 | 0.019 | 0.022 | 0.022 | 0.022 | 3.482 | 5 | 5902 | 0 |

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

Hopkins, M., Reeber, E., Forman, G., & Suermondt, J. (1999). Spambase [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C53G6X.