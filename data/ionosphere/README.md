# Ionosphere

**Description**:  

This radar data was collected by a system in Goose Bay, Labrador.  This system consists of a phased array of 16 high-frequency antennas with a total transmitted power on the order of 6.4 kilowatts.  See the paper for more details.  The targets were free electrons in the ionosphere. "Good" radar returns are those showing evidence of some type of structure in the ionosphere.  "Bad" returns are those that do not; their signals pass through the ionosphere.  

Received signals were processed using an autocorrelation function whose arguments are the time of a pulse and the pulse number.  There were 17 pulse numbers for the Goose Bay system.

Instances in this databse are described by 2 attributes per pulse number, corresponding to the complex values returned by the function resulting from the complex electromagnetic signal.

---

## Table of Contents
- [Ionosphere](#ionosphere)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Ionosphere](https://archive.ics.uci.edu/dataset/52/ionosphere)
  
- **Domain**: Physics and Chemistry

- **Format**: CSV  

---

## Variables

| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***attribute1*** | Feature | First attribute | Continuous | - |
| ***attribute2*** | Feature | Second attribute | Continuous | - |
| ***attribute3*** | Feature | Third attribute | Continuous | - |
| ***attribute4*** | Feature | Fourth attribute | Continuous | - |
| ***attribute5*** | Feature | Fifth attribute | Continuous | - |
| ***attribute6*** | Feature | Sixth attribute | Continuous | - |
| ***attribute7*** | Feature | Seventh attribute | Continuous | - |
| ***attribute8*** | Feature | Eighth attribute | Continuous | - |
| ***attribute9*** | Feature | Ninth attribute | Continuous | - |
| ***attribute10*** | Feature | Tenth attribute | Continuous | - |
| ***attribute11*** | Feature | Eleventh attribute | Continuous | - |
| ***attribute12*** | Feature | Twelfth attribute | Continuous | - |
| ***attribute13*** | Feature | Thirteenth attribute | Continuous | - |
| ***attribute14*** | Feature | Fourteenth attribute | Continuous | - |
| ***attribute15*** | Feature | Fifteenth attribute | Continuous | - |
| ***attribute16*** | Feature | Sixteenth attribute | Continuous | - |
| ***attribute17*** | Feature | Seventeenth attribute | Continuous | - |
| ***attribute18*** | Feature | Eighteenth attribute | Continuous | - |
| ***attribute19*** | Feature | Nineteenth attribute | Continuous | - |
| ***attribute20*** | Feature | Twentieth attribute | Continuous | - |
| ***attribute21*** | Feature | Twenty-first attribute | Continuous | - |
| ***attribute22*** | Feature | Twenty-second attribute | Continuous | - |
| ***attribute23*** | Feature | Twenty-third attribute | Continuous | - |
| ***attribute24*** | Feature | Twenty-fourth attribute | Continuous | - |
| ***attribute25*** | Feature | Twenty-fifth attribute | Continuous | - |
| ***attribute26*** | Feature | Twenty-sixth attribute | Continuous | - |
| ***attribute27*** | Feature | Twenty-seventh attribute | Continuous | - |
| ***attribute28*** | Feature | Twenty-eighth attribute | Continuous | - |
| ***attribute29*** | Feature | Twenty-ninth attribute | Continuous | - |
| ***attribute30*** | Feature | Thirtieth attribute | Continuous | - |
| ***attribute31*** | Feature | Thirty-first attribute | Continuous | - |
| ***attribute32*** | Feature | Thirty-second attribute | Continuous | - |
| ***class*** | **Target** | Good or bad radar return | Categorical | g, b |

---

## Target Variable

- **Name**: *class*  
- **Type**: Categorical
- **Values**:
  - g for good radar return
  - b for bad radar return

---

## Dataset Details

- **Has missing values?**: no
- **Number of Instances**: 351 instances 
- **Number of Features**: 34
- **Class Distribution**:
  - g for good radar return = 225 instances
  - b for bad radar return = 126 instances
 
---

## File Structure

- `ionosphere.csv`: Main dataset file.  
- `README.md`: Documentation file (this file).  
- `configuration.json`: Configuration file containing the instructions for DatasetPreprocessor.  

---

## Sample Data

| a1 | a2 | a3 | a4 | a5 | a6 | a7 | a8 | a9 | a10 | a11 | a12 | a13 | a14 | a15 | a16 | a17 | a18 | a19 | a20 | a21 | a22 | a23 | a24 | a25 | a26 | a27 | a28 | a29 | a30 | a31 | a32 | a33 | a34 | class |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0 | 0.99539 | -0.05889 | 0.85243 | 0.02306 | 0.83398 | -0.37708 | 1 | 0.03760 | 0.85243 | -0.17755 | 0.59755 | -0.44945 | 0.60536 | -0.38223 | 0.84356 | -0.38542 | 0.58212 | -0.32192 | 0.56971 | -0.29674 | 0.36946 | -0.47357 | 0.56811 | -0.51171 | 0.41078 | -0.46168 | 0.21266 | -0.34090 | 0.42267 | -0.54487 | 0.18641 | -0.45300 | g |
| 1 | 0 | 1 | -0.18829 | 0.93035 | -0.36156 | -0.10868 | -0.93597 | 1 | -0.04549 | 0.50874 | -0.67743 | 0.34432 | -0.69707 | -0.51685 | -0.97515 | 0.05499 | -0.62237 | 0.33109 | -1 | -0.13151 | -0.45300 | -0.18056 | -0.35734 | -0.20332 | -0.26569 | -0.20468 | -0.18401 | -0.19040 | -0.11593 | -0.16626 | -0.06288 | -0.13738 | -0.02447 | b |
| 1 | 0 | 1 | -0.03365 | 1 | 0.00485 | 1 | -0.12062 | 0.88965 | 0.01198 | 0.73082 | 0.05346 | 0.85443 | 0.00827 | 0.54591 | 0.00299 | 0.83775 | -0.13644 | 0.75535 | -0.08540 | 0.70887 | -0.27502 | 0.43385 | -0.12062 | 0.57528 | -0.40220 | 0.58984 | -0.22145 | 0.43100 | -0.17365 | 0.60436 | -0.24180 | 0.56045 | -0.38238 | g |

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

Sigillito, V., Wing, S., Hutton, L., & Baker, K. (1989). Ionosphere [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5W01B.

Sigillito, V. G., Wing, S. P., Hutton, L. V., & Baker, K. B. (1989). Classification of radar returns from the ionosphere using neural networks. Johns Hopkins APL Technical Digest, 10, 262-266.