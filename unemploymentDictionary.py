import pandas as pd

#https://stat.gov.pl/download/gfx/portalinformacyjny/pl/defaultaktualnosci/5473/2/39/1/pow11_15____.xls

def unemploymentDictionary(url: str):

	wojTable = ['Dolnoslaskie', 'Kujawsko-pomorskie', 'Lubelskie', 'Lubuskie', 'Lodzkie', 'Malopolskie', 'Mazowieckie', 'Opolskie', 'Podkarpackie', 'Podlaskie', 'Pomorskie', 'Slaskie', 'Swietokrzyskie', 'Warminsko-mazurskie', 'Wielkopolskie', 'Zachodnio-pomorskie' ]
	retDict = {}

	data = pd.read_excel(url, sheet_name=0)
	
	for x, y, z in zip(data[data.columns[1]], data[data.columns[5]], data[data.columns[0]]):
		if(str(x) == "0" and str(z) != "0"):
			retDict[wojTable[int(str(z))//2-1]] = float(str(y))

			return retDict

