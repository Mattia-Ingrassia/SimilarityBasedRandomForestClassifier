# Similarity Based Random Forest Classifier

This project implements a Similarity Based Random Forest Classifier and evaluates its performance on various datasets, confronting the results with other ensemble methods.
More information on the model can be found in the classifier folder.

---

## Table of Contents
- [Similarity Based Random Forest Classifier](#similarity-based-random-forest-classifier)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Project Structure](#project-structure)
  - [Datasets](#datasets)
  - [Configuration](#configuration)
  - [Running the Project](#running-the-project)
  - [Results](#results)

---

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Mattia-Ingrassia/SimilarityBasedRandomForestClassifier.git
    cd SimilarityBasedRandomForestClassifier
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:

   - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

---

## Project Structure

```
├── classifier/
│   ├── README.md
│   └── SimilarityBasedRandomForestClassifier.py
|
├── data/ 
│   ├── adult/ 
│   ├── bank/ 
│   ├── banknote/ 
│   ├── breast_cancer_wisconsin/ 
│   ├── car/ 
│   ├── connect_4/ 
│   ├── covertype/ 
│   ├── default_credit_card/ 
│   ├── dropout/ 
│   ├── dry_bean/ 
│   ├── ecoli/ 
│   ├── glass/ 
│   ├── heart_failure/ 
│   ├── ionosphere/ 
│   ├── iris/ 
│   ├── letter_recognition/
│   ├── mushroom/
│   ├── obesity/ 
│   ├── poker_hand/ 
│   ├── rice/
│   ├── seeds/
│   ├── seismic_bumps/
│   ├── shuttle/
│   ├── spambase/
│   ├── telescope/
│   ├── tic_tac_toe/
│   ├── vehicles/
│   ├── wine/ 
│   └── zoo/ 
|
├── .gitignore
├── DatasetPreprocessor.py 
├── requirements.txt 
├── run_configuration.json 
└── run_handler.py

```

---

## Datasets

The `data` directory contains various datasets used for evaluating the classifier. Each dataset has its own subdirectory containing the dataset files and a `README.md` file with detailed information about the dataset.

---

## Configuration

The `run_configuration.json` file contains the configuration for running the project. It includes parameters such as random states, number of estimators, test sizes, and distance metrics.

```json
{   
    "random_states": [23],
    "number_of_estimators": [25],
    "test_sizes": [0.3],
    "distance_metrics": ["cityblock", "cosine", "euclidean","braycurtis", "canberra", "chebyshev", "correlation", "hamming"]
}

```

---

## Running the Project

To run the project, execute the run_handler.py script. This script will load the datasets, preprocess them, initialize the classifiers, and evaluate their performance.


```bash
python run_handler.py
```

This scripts uses ```DatasetPreprocessor.py``` for prepraring the datasets for the models.
After the first execution, it is possible to avoid the preprocessing part if you don't need to edit the configuration of the datasets by setting the value of ```FROM_SCRATCH``` variable to false.

---

## Results

The results of the evaluations are saved in the ```results_metrics.json``` file within each dataset's subdirectory.
The results include metrics such as accuracy, balanced accuracy, micro F1, macro F1, training time, and prediction time.

