# Covertype

**Description**:

Classification of pixels into 7 forest cover types based on attributes such as elevation, aspect, slope, hillshade, soil-type, and more.

---

## Table of Contents
- [Covertype](#covertype)
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

- **Source**: This dataset comes from [UC Irvine Machine Learning Repository - Covertype](https://archive.ics.uci.edu/dataset/31/covertype)
  
- **Domain**: Biology

- **Format**: CSV  

---

## Variables

| Variable Name | Role | Description | Data Type | Range / Values |
|---|---|---|---|---|
| ***Elevation*** | Feature | Elevation in meters | Integer | - | 
| ***Aspect*** | Feature | Aspect in degrees azimuth | Integer | - | 
| ***Slope*** | Feature | Slope in degrees | Integer | - | 
| ***Horizontal_Distance_To_Hydrology*** | Feature | Horizontal Distance to nearest surface water features | Integer | - | 
| ***Vertical_Distance_To_Hydrology*** | Feature | Vertical Distance to nearest surface water features | Integer | - | 
| ***Horizontal_Distance_To_Roadways*** | Feature | Horizontal Distance to nearest roadway | Integer | - | 
| ***Hillshade_9am*** | Feature | Hillshade index at 9am, summer solstice | Integer | 0-255 | 
| ***Hillshade_Noon*** | Feature | Hillshade index at noon, summer solstice | Integer | 0-255 | 
| ***Hillshade_3pm*** | Feature | Hillshade index at 3pm, summer solstice | Integer | 0-255 | 
| ***Horizontal_Distance_To_Fire_Points*** | Feature | Horizontal Distance to nearest wildfire ignition points | Integer | - | 
| ***Wilderness_Area1*** | Feature | column 1 of 4 binary columns - wilderness area designation | Integer | 0 - 1 | 
| ***Wilderness_Area2*** | Feature | column 2 of 4 binary columns - wilderness area designation | Integer | 0 - 1 | 
| ***Wilderness_Area3*** | Feature | column 3 of 4 binary columns - wilderness area designation | Integer | 0 - 1 | 
| ***Wilderness_Area4*** | Feature | column 4 of 4 binary columns - wilderness area designation | Integer | 0 - 1 | 
| ***Soil_Type1*** | Feature | column 1 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type2*** | Feature | column 2 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type3*** | Feature | column 3 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type4*** | Feature | column 4 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type5*** | Feature | column 5 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type6*** | Feature | column 6 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type7*** | Feature | column 7 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type8*** | Feature | column 8 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type9*** | Feature | column 9 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type10*** | Feature | column 10 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type11*** | Feature | column 11 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type12*** | Feature | column 12 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type13*** | Feature | column 13 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type14*** | Feature | column 14 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type15*** | Feature | column 15 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type16*** | Feature | column 16 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type17*** | Feature | column 17 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type18*** | Feature | column 18 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type19*** | Feature | column 19 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type20*** | Feature | column 20 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type21*** | Feature | column 21 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type22*** | Feature | column 22 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type23*** | Feature | column 23 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type24*** | Feature | column 24 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type25*** | Feature | column 25 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type26*** | Feature | column 26 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type27*** | Feature | column 27 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type28*** | Feature | column 28 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type29*** | Feature | column 29 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type30*** | Feature | column 30 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type31*** | Feature | column 31 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type32*** | Feature | column 32 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type33*** | Feature | column 33 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type34*** | Feature | column 34 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type35*** | Feature | column 35 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type36*** | Feature | column 36 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type37*** | Feature | column 37 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type38*** | Feature | column 38 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type39*** | Feature | column 39 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Soil_Type40 binary columns*** | Feature | column 40 of 40 binary columns - Soil type designation | Integer | 0 - 1 | 
| ***Cover_Type*** | **Target** | Forest Cover Type designation | Categorical | 1 - 7|

---

## Target Variable

- **Name**: *Cover_type* 
- **Type**: Categorical  
- **Values**: 
  - 1 = Spruce/Fir
  - 2 = Lodgepole Pine
  - 3 = Ponderosa Pine
  - 4 = Cottonwood/Willow
  - 5 = Aspen
  - 6 = Douglas-fir
  - 7 = Krummholz 

---

## Dataset Details

- **Has missing values?**: no 
- **Number of Instances**: 581012 instances 
- **Number of Features**: 54
- **Class Distribution**:
  - 1 = Spruce/Fir = 211840 instances
  - 2 = Lodgepole Pine = 283301 instances
  - 3 = Ponderosa Pine = 35754 instances
  - 4 = Cottonwood/Willow = 2747 instances
  - 5 = Aspen = 9493 instances
  - 6 = Douglas-fir = 17367 instances
  - 7 = Krummholz = 20510 instances
 
---

## File Structure

- `covertype.csv`: Main dataset file.  
- `README.md`: Documentation file (this file).  
- `configuration.json`: Configuration file containing the istructions for DatasetPreprocessor.  

---

## Sample Data

An example of how the dataset is structured:

| Elevation | Aspect | Slope | Horizontal_Distance_To_Hydrology | Vertical_Distance_To_Hydrology | Horizontal_Distance_To_Roadways | Hillshade_9am | Hillshade_Noon | Hillshade_3pm | Horizontal_Distance_To_Fire_Points | Wilderness_Area1 | Wilderness_Area2 | Wilderness_Area3 | Wilderness_Area4 | Soil_Type1 | Soil_Type2 | Soil_Type3 | Soil_Type4 | Soil_Type5 | Soil_Type6 | Soil_Type7 | Soil_Type8 | Soil_Type9 | Soil_Type10 | Soil_Type11 | Soil_Type12 | Soil_Type13 | Soil_Type14 | Soil_Type15 | Soil_Type16 | Soil_Type17 | Soil_Type18 | Soil_Type19 | Soil_Type20 | Soil_Type21 | Soil_Type22 | Soil_Type23 | Soil_Type24 | Soil_Type25 | Soil_Type26 | Soil_Type27 | Soil_Type28 | Soil_Type29 | Soil_Type30 | Soil_Type31 | Soil_Type32 | Soil_Type33 | Soil_Type34 | Soil_Type35 | Soil_Type36 | Soil_Type37 | Soil_Type38 | Soil_Type39 | Soil_Type40 | Cover_Type |
|------------|--------|-------|---------------------------------|-------------------------------|----------------------------------|---------------|----------------|---------------|------------------------------------|------------------|------------------|------------------|------------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
| 2686 | 354 | 12 | 0 | 0 | 3167 | 200 | 219 | 157 | 6155 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| 2699 | 347 | 3 | 0 | 0 | 2096 | 213 | 234 | 159 | 6853 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| 2570 | 346 | 2 | 0 | 0 | 331 | 215 | 235 | 158 | 5745 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |

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

Blackard, J. (1998). Covertype [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C50K5N.

