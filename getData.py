import pandas as pd

def get_data(url: str):
	data  = pd.read_csv(url, delimiter=';')
	return data
