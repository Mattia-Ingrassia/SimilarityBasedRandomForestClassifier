# Telescope

**Description**:  

The data are MC generated (see below) to simulate registration of high energy gamma particles in a ground-based atmospheric Cherenkov gamma telescope using the imaging technique. Cherenkov gamma telescope observes high energy gamma rays, taking advantage of the radiation emitted by charged particles produced inside the electromagnetic showers initiated by the gammas, and developing in the atmosphere. This Cherenkov radiation (of visible to UV wavelengths) leaks through the atmosphere and gets recorded in the detector, allowing reconstruction of the shower parameters. The available information consists of pulses left by the incoming Cherenkov photons on the photomultiplier tubes, arranged in a plane, the camera. Depending on the energy of the primary gamma, a total of few hundreds to some 10000 Cherenkov photons get collected, in patterns (called the shower image), allowing to discriminate statistically those caused by primary gammas (signal) from the images of hadronic showers initiated by cosmic rays in the upper atmosphere (background).

---

## Table of Contents
- [Telescope](#telescope)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - MAGIC Gamma Telescope](https://archive.ics.uci.edu/dataset/159/magic+gamma+telescope)
  
- **Domain**: Physics and Chemistry

- **Format**: CSV  

---

## Variables

| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***fLength*** | Feature | Length of the major axis of the ellipse [mm] | Continuous | - |
| ***fWidth*** | Feature | Width of the minor axis of the ellipse [mm] | Continuous | - |
| ***fSize*** | Feature | 10-log of sum of content of all pixels [in #phot] | Continuous | - |
| ***fConc*** | Feature | Ratio of sum of two highest pixels over fSize [ratio] | Continuous | - |
| ***fConc1*** | Feature | Ratio of highest pixel over fSize [ratio] | Continuous | - |
| ***fAsym*** | Feature | Distance from highest pixel to center, projected onto major axis [mm] | Continuous | - |
| ***fM3Long*** | Feature | 3rd root of third moment along major axis [mm] | Continuous | - |
| ***fM3Trans*** | Feature | 3rd root of third moment along minor axis [mm] | Continuous | - |
| ***fAlpha*** | Feature | Angle of major axis with vector to origin [deg] | Continuous | - |
| ***fDist*** | Feature | Distance from origin to center of ellipse [mm] | Continuous | - |
| ***class*** | **Target** | Gamma (signal) or Hadron (background) | Categorical | g, h |

---

## Target Variable

- **Name**: *class*  
- **Type**: Categorical
- **Values**:
  - g = Gamma (signal)
  - h = Hadron (background)

---

## Dataset Details

- **Has missing values?**: no
- **Number of Instances**: 19020 instances 
- **Number of Features**: 10
- **Class Distribution**:
  - g = 12332 instances
  - h = 6688 instances
 
---

## File Structure

- `telescope.csv`: Main dataset file.  
- `README.md`: Documentation file (this file).  
- `configuration.json`: Configuration file containing the instructions for DatasetPreprocessor.  

---

## Sample Data

An example of how the dataset is structured:

| fLength | fWidth | fSize | fConc | fConc1 | fAsym | fM3Long | fM3Trans | fAlpha | fDist | class |
|---------|--------|-------|-------|--------|-------|---------|----------|--------|-------|-------|
| 56.2216 | 18.7019 | 2.9297 | 0.2516 | 0.1393 | 96.5758 | -41.2969 | 11.3764 | 5.911 | 197.209 | **g** |
| 31.5125 | 19.2867 | 2.9578 | 0.2975 | 0.1515 | 38.1833 | 21.6729 | -12.0726 | 17.5809 | 171.227 | **g** |
| 93.7035 | 37.9432 | 3.1454 | 0.168 | 0.1011 | 53.2566 | 89.0566 | 11.8175 | 14.1224 | 231.9028 | **h** |

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

Bock, R. (2004). MAGIC Gamma Telescope [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C52C8B.