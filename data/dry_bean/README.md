# Dry Bean

**Description**:

Images of 13611 grains of 7 different registered dry beans were taken with a high-resolution camera. A total of 16 features; 12 dimensions and 4 shape forms, were obtained from the grains.

---

## Table of Contents
- [Dry Bean](#dry-bean)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Dry Bean](https://archive.ics.uci.edu/dataset/602/dry+bean+dataset)

- **Domain**: Biology

- **Format**: CSV

---

## Variables

| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***Area*** | Feature | The area of a bean zone and the number of pixels within its boundaries | Integer | - |
| ***Perimeter*** | Feature | Bean circumference is defined as the length of its border. | Continuous | - |
| ***Major axis length*** | Feature | The distance between the ends of the longest line that can be drawn from a bean | Continuous | - |
| ***Minor axis length*** | Feature | The longest line that can be drawn from the bean while standing perpendicular to the main axis | Continuous | - |
| ***Aspect ratio*** | Feature | Defines the relationship between MajorAxisLength and MinorAxisLength | Continuous | - |
| ***Eccentricity*** | Feature | Eccentricity of the ellipse having the same moments as the region	 | Continuous | - |
| ***Convex area*** | Feature | Number of pixels in the smallest convex polygon that can contain the area of a bean seed | Integer | - |
| ***Equivalent diameter*** | Feature | Equivalent diameter: The diameter of a circle having the same area as a bean seed area | Continuous | - |
| ***Extent*** | Feature | The ratio of the pixels in the bounding box to the bean area | Continuous | - |
| ***Solidity*** | Feature | Also known as convexity. The ratio of the pixels in the convex shell to those found in beans. | Continuous | - |
| ***Roundness*** | Feature | Calculated with the following formula: (4piA)/(P^2) | Continuous | - |
| ***Compactness*** | Feature | Measures the roundness of an object | Continuous | - |
| ***ShapeFactor1*** | Feature | - | Continuous | - |
| ***ShapeFactor2*** | Feature | - | Continuous | - |
| ***ShapeFactor3*** | Feature | - | Continuous | - |
| ***ShapeFactor4*** | Feature | - | Continuous | - |
| ***Class*** | **Target** | type of bean | Categorical | Seker, Barbunya, Bombay, Cali, Dermosan, Horoz, Sira |


---

## Target Variable

- **Name**: *Class*
- **Type**: Categorical
- **Values**:
- Possible classes or ranges.
  - SEKER
  - BARBUNYA
  - BOMBAY
  - CALI
  - HOROZ
  - SIRA
  - DERMASON

---

## Dataset Details

- **Has missing values?**: no
- **Number of Instances**: 13611 instances
- **Number of Features**: 16
- **Class Distribution**:
  - SEKER: 2027 instances
  - BARBUNYA: 1322 instances
  - BOMBAY: 522 instances
  - CALI: 1630 instances
  - HOROZ: 1928 instances
  - SIRA: 2636 instances
  - DERMASON: 3546 instances

---

## File Structure

- `dry_bean.csv`: Main dataset file.
- `README.md`: Documentation file (this file).
- `configuration.json`: Configuration file containing the istructions for DatasetPreprocessor.
- `results_images/`: A folder containing the charts of the metrics analyzed.
- `results_metrics.json`: The json file containing the results of the models for this dataset.

---

## Sample Data

An example of how the dataset is structured:

| Area | Perimeter | Major axis length | Minor axis length | Aspect ratio | Eccentricity | Convex area | Equivalent diameter | Extent | Solidity | Roundness | Compactness | ShapeFactor1 | ShapeFactor2 | ShapeFactor3 | ShapeFactor4 | Class |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 254616.0 | 1985.37 | 738.8601534818813 | 447.41832874876803 | 1.6513855289481494 | 0.7958056520436629 | 263261.0 | 569.3743583287609 | 0.7837473450918829 | 0.9671618659809087 | 0.8117319584911376 | 0.7706118074517647 | 0.00290186065872483 | 0.0006312464571718085 | 0.5938425577840758 | 0.980663006398178 | BOMBAY |
| 45504.0 | 793.417 | 295.4698305520384 | 196.3118224893667 | 1.5051046177722822 | 0.7473721581277368 | 45972.0 | 240.70208192624517 | 0.7377790748577265 | 0.9898198903680501 | 0.9083567245276849 | 0.8146418247728765 | 0.0064932715926520395 | 0.0017640469732470574 | 0.6636413026692821 | 0.9988495891919492 | CALI |
| 40443.0 | 753.761 | 278.6161751535683 | 185.16160587890639 | 1.5047189390643985 | 0.7472207324111643 | 40926.0 | 226.92207232379178 | 0.737150043744532 | 0.9881982114059522 | 0.8945114443917778 | 0.8144612286013774 | 0.006889107513131278 | 0.0018699258511014382 | 0.6633470928948652 | 0.9981509338522142 | DERMASON |


---

## Performance Metrics

| Classifier | Accuracy | Balanced Accuracy | Micro F1 | Macro F1 | Training Time | Prediction Time | Total Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Random Forest | 92.5% | 93.1% | 92.5% | 93.3% | 0.880s | 0.010s | 0.889s |
| Extra Trees | 92.1% | 92.9% | 92.1% | 93.1% | 0.146s | 0.013s | 0.159s |
| ***XGBoost*** | ***93.0%*** | ***93.6%*** | ***93.0%*** | ***93.8%*** | 0.143s | 0.002s | 0.146s |
| AdaBoost | 77.8% | 65.1% | 77.8% | 62.0% | 0.626s | 0.009s | 0.635s |
| Gradient Boosting | 91.6% | 92.4% | 91.6% | 92.6% | 10.636s | 0.011s | 10.646s |
| SimilarityForest[cityblock] | 87.0% | 87.2% | 87.0% | 87.6% | 0.365s | 0.014s | 0.379s |
| SimilarityForest[cosine] | 88.3% | 89.3% | 88.3% | 89.6% | 0.526s | 0.014s | 0.540s |
| SimilarityForest[euclidean] | 85.7% | 85.9% | 85.7% | 86.3% | 0.297s | 0.012s | 0.310s |
| SimilarityForest[braycurtis] | 89.3% | 90.4% | 89.3% | 90.5% | 0.550s | 0.014s | 0.564s |
| SimilarityForest[canberra] | 88.8% | 90.0% | 88.8% | 90.0% | 0.508s | 0.014s | 0.522s |
| SimilarityForest[chebyshev] | 86.1% | 82.7% | 86.1% | 84.1% | 0.314s | 0.012s | 0.326s |
| SimilarityForest[correlation] | 88.3% | 89.3% | 88.3% | 89.6% | 0.533s | 0.014s | 0.546s |
| SimilarityForest[hamming] | 89.5% | 90.6% | 89.5% | 90.7% | 0.500s | 0.013s | 0.512s |

---

## Acknowledgments

Dry Bean [Dataset]. (2020). UCI Machine Learning Repository. https://doi.org/10.24432/C50S4B.


