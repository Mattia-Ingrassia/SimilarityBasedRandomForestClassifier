from collections import Counter
import os
import numpy as np
from pandas import read_csv
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from numpy import load, save
from scipy.sparse import issparse


class DatasetPreprocessor:
    def __init__(
            self,
            dataset_name: str,
            columns: list,
            target_column: str,
            input_data_path: str,
            output_data_path: str,
            needs_y_encoding: bool = False,
            categorical_features: list = None,
            ignored_columns: list = None,
            na_values: list = None,
    ):
        self.dataset_name = dataset_name
        self.columns = columns
        self.target_column = target_column
        self.input_data_path = input_data_path
        self.output_data_path = output_data_path
        self.needs_y_encoding = needs_y_encoding
        self.categorical_features = categorical_features
        self.ignored_columns = ignored_columns
        self.na_values = na_values
        self.output_dir = output_data_path + f"/{dataset_name}"
        self.dataset_path = f"{input_data_path}/{dataset_name}.csv"
        self.classes_encoder = None


    def load_dataset(self, from_scratch:bool = True) -> tuple[np.ndarray, np.ndarray]:
        if from_scratch:
            return self.pre_processing()
        else:
            try:
                # Tenta di caricare i file .npy
                X_path = self.output_dir + "/X.npy"
                y_path = self.output_dir + "/y.npy"
                X = load(X_path, allow_pickle=True)
                y = load(y_path, allow_pickle=True)
                return X, y
            except Exception as e:
                print(f"Errore nel caricamento dei dati del dataset {self.dataset_name}: {e}")


    # Esegue il pre-processing del dataset, salva i risultati
    # e restituisce X e y
    def pre_processing(self) -> tuple[np.ndarray, np.ndarray]:
        
        try:
            data = read_csv(self.dataset_path, names=self.columns, na_values=self.na_values, skipinitialspace=True)
        except FileNotFoundError:
            print(f"Dataset file {self.dataset_path} not found")
        except Exception as e:
            print(f"Error reading dataset file {self.dataset_path}: {e}")
        
        # Rimuove le righe con valori mancanti
        if self.na_values is not None:
            data = data.dropna()

        # Rimuove le colonne da non tenere in considerazione
        if self.ignored_columns is not None:
            data = data.drop(columns=self.ignored_columns)

        # Prepare the target column y
        y = data[self.target_column].to_numpy()
        if self.needs_y_encoding:
            self.classes_encoder = LabelEncoder()
            y = self.classes_encoder.fit_transform(y)
        
        # Prepare the features columns X
        X = data.drop(columns=self.target_column)
        
        if self.categorical_features is not None:
            features_encoder = ColumnTransformer(
                transformers = [("onehot", OneHotEncoder(), self.categorical_features)],
                remainder = "passthrough"
            )
            X = features_encoder.fit_transform(X)
            if(issparse(X)):
                X = X.toarray()
        else:
            X = X.to_numpy()
        
        # Save the preprocessed dataset
        os.makedirs(self.output_dir, exist_ok=True)
        save(f"{self.output_dir}/X.npy", X)
        save(f"{self.output_dir}/y.npy", y)
        return X, y