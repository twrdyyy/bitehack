import pandas as pd

#https://stat.gov.pl/download/gfx/portalinformacyjny/pl/defaultaktualnosci/5473/2/39/1/pow11_15____.xls

def economyDictionary(url: str):

	wojTable = ['Dolnoslaskie', 'Kujawsko-pomorskie', 'Lubelskie', 'Lubuskie', 'Lodzkie', 'Malopolskie', 'Mazowieckie', 'Opolskie', 'Podkarpackie', 'Podlaskie', 'Pomorskie', 'Slaskie', 'Swietokrzyskie', 'Warminsko-mazurskie', 'Wielkopolskie', 'Zachodnio-pomorskie' ]
	retDict = {}
	max_ = 0.0
	data = pd.read_excel(url['unemployment'], sheet_name=0)
	
	retDict['normal'] = {'unemployment' : max_}
	for x, y, z in zip(data[data.columns[1]], data[data.columns[5]], data[data.columns[0]]):
		if(str(x) == "0" and str(z) != "0"):
			retDict[(wojTable[int(str(z))//2-1])] = {'unemployment' : -1*float(str(y))}
			if(float(str(y)) > max_):
				max_ = float(str(y))
				retDict['normal']['unemployment'] = max_

	return retDict


if __name__ == '__main__':
	print(economyDictionary("https://stat.gov.pl/download/gfx/portalinformacyjny/pl/defaultaktualnosci/5473/2/39/1/pow11_15____.xls"))