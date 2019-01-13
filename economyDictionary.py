import pandas as pd
import requests
import zipfile
import io
import math

#https://stat.gov.pl/download/gfx/portalinformacyjny/pl/defaultaktualnosci/5473/2/39/1/pow11_15____.xls

def economyDictionary(url):

	wojTable = ['Dolnoslaskie', 'Kujawsko-pomorskie', 'Lubelskie', 'Lubuskie', 'Lodzkie', 'Malopolskie', 'Mazowieckie', 'Opolskie', 'Podkarpackie', 'Podlaskie', 'Pomorskie', 'Slaskie', 'Swietokrzyskie', 'Warminsko-mazurskie', 'Wielkopolskie', 'Zachodnio-pomorskie' ]
	retDictionary = {}
	max_ = 0.0
	data = pd.read_excel(url['unemployment'], sheet_name=0)
	
	retDictionary['normal'] = {'unemployment' : max_}
	for x, y, z in zip(data[data.columns[1]], data[data.columns[5]], data[data.columns[0]]):
		if(str(x) == "0" and str(z) != "0"):
			retDictionary[(wojTable[int(str(z))//2-1])] = {'unemployment' : -1*float(str(y))}
			if(float(str(y)) > max_):
				max_ = float(str(y))
				retDictionary['normal']['unemployment'] = max_

	r = requests.get(url['income'], stream=True)
	with zipfile.ZipFile(io.BytesIO(r.content)) as z:
		with z.open("Dzial_06_Dochody ludnosci_Budzety_gospodarstw_domowych.xlsx") as f:
			baza = pd.read_excel(f)
			maks=0.0
			for i in range(11, 26):
				retDictionary[wojTable[i-11]]['Income']=baza["Unnamed: 2"][i]
				if baza["Unnamed: 2"][i] > maks:
					maks = baza["Unnamed: 2"][i]
			retDictionary['normal']['Income']=maks

	return retDictionary

# -*- coding: utf-8 -*-

#LINK: https://www.dane.gov.pl/media/resources/20160114/rocznik-statystyczny-wojewodztw-2017-tablice.zip