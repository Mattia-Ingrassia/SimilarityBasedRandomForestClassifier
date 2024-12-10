import pandas as pd
from scipy.io import arff

input_arff_path = "data/dry_bean/dry_bean.arff"
output_csv_path = "data/dry_bean/dry_bean.csv"

data, meta = arff.loadarff(input_arff_path)
dataframe = pd.DataFrame(data)
dataframe.to_csv(output_csv_path, index=False, header=False)
