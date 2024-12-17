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
- `results_images/`: A folder containing the charts of the metrics analyzed.
- `results_metrics.json`: The json file containing the results of the models for this dataset.

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

| Classifier | Accuracy | Balanced Accuracy | Micro F1 | Macro F1 | Training Time | Prediction Time | Total Time |
|  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |
| Random Forest | 87.6% | 85.0% | 87.6% | 86.1% | 1.215s | 0.018s | 1.233s |
| Extra Trees | 86.8% | 83.8% | 86.8% | 85.0% | 0.262s | 0.024s | 0.286s |
| XGBoost | 86.9% | 84.0% | 86.9% | 85.2% | 0.039s | 0.001s | 0.041s |
| AdaBoost | 81.9% | 77.8% | 81.9% | 79.1% | 0.509s | 0.007s | 0.515s |
| Gradient Boosting | 84.0% | 79.5% | 84.0% | 81.3% | 1.299s | 0.003s | 1.302s |
| SimilarityForest[cityblock] | 80.9% | 78.7% | 80.9% | 79.0% | 0.621s | 0.023s | 0.644s |
| SimilarityForest[cosine] | 81.1% | 79.2% | 81.1% | 79.4% | 0.554s | 0.021s | 0.575s |
| SimilarityForest[euclidean] | 80.2% | 78.3% | 80.2% | 78.4% | 0.578s | 0.023s | 0.600s |
| SimilarityForest[braycurtis] | 81.1% | 79.0% | 81.1% | 79.3% | 0.536s | 0.023s | 0.559s |
| SimilarityForest[canberra] | 80.7% | 78.7% | 80.7% | 78.9% | 0.618s | 0.023s | 0.641s |
| SimilarityForest[chebyshev] | 80.4% | 78.3% | 80.4% | 78.6% | 0.542s | 0.021s | 0.564s |
| SimilarityForest[correlation] | 80.5% | 78.7% | 80.5% | 78.8% | 0.624s | 0.022s | 0.645s |
| SimilarityForest[hamming] | 81.2% | 79.3% | 81.2% | 79.5% | 0.541s | 0.021s | 0.563s |

---

## Acknowledgments

Bock, R. (2004). MAGIC Gamma Telescope [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C52C8B.