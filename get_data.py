import pandas as pd

def get_data(url: string):
	data  = pd.read_csv(url, delimiter=';')
	return data
