import pandas as pd 


input_xls_path = "data/default_credit_card/default_credit_card.xls"
output_csv_path = "data/default_credit_card/default_credit_card.csv"

read_file = pd.read_excel (input_xls_path, engine='calamine') 
read_file.to_csv (output_csv_path, index = None, header=False)
	
