import os
import pandas as pd

# Directory containing the .dat files
input_dat_path = "data/vehicles/"
output_csv_path = "data/vehicles/vehicles.csv"

# Nomi delle colonne (modifica secondo le informazioni del dataset)
columns = [
    "compactness",
    "circularity",
    "distance_circularity",
    "radius_ratio",
    "pr.axis_aspect_ratio",
    "max.length_aspect_ratio",
    "scatter_ratio",
    "elongatedness",
    "pr.axis_rectangularity",
    "max.length_rectangularity",
    "scaled_variance_major_axis",
    "scaled_variance_minor_axis",
    "scaled_radius_of_gyration",
    "skewness_major_axis",
    "skewness_minor_axis",
    "kurtosis_minor_axis",
    "kurtosis_major_axis",
    "hollows_ratio",
    "class"
]


files = []
for f in os.listdir(input_dat_path):
    if f.endswith(".dat"):
        files.append(os.path.join(input_dat_path, f))

dataframes = []

# Lista per salvare i dati puliti
cleaned_data = []

# Leggi ogni file e processa i dati
for file in files:
    with open(file, "r") as f:
        for line in f:
            # Rimuovi virgole aggiuntive e spazi multipli
            clean_line = line.strip().split(",")[0].strip()
            # Separa i valori sulla base degli spazi
            values = clean_line.split()
            # Aggiungi i dati alla lista
            cleaned_data.append(values)

# Crea un DataFrame dai dati puliti
df = pd.DataFrame(cleaned_data, columns=columns)

# Salva il DataFrame in un file CSV pulito
df.to_csv(output_csv_path, index=False, header=False)

print(f"File CSV pulito creato: {output_csv_path}")