import pandas as pd 


def tumorDictionary(url):
    wojTable = ['Dolnoslaskie', 'Kujawsko-pomorskie', 'Lubelskie', 'Lubuskie', 'Lodzkie', 'Malopolskie', 'Mazowieckie', 'Opolskie', 'Podkarpackie', 'Podlaskie', 'Pomorskie', 'Slaskie', 'Swietokrzyskie', 'Warminsko-mazurskie', 'Wielkopolskie', 'Zachodnio-pomorskie' ]
    retDictionary = {wojTable[0]:{}, wojTable[1]:{}, wojTable[2]:{}, wojTable[3]:{}, wojTable[4]:{}, wojTable[5]:{}, wojTable[6]:{}, wojTable[7]:{}, wojTable[8]:{}, wojTable[9]:{}, wojTable[10]:{}, wojTable[11]:{}, wojTable[12]:{}, wojTable[13]:{}, wojTable[14]:{}, wojTable[15]:{}}

    data = pd.read_csv('https://www.dane.gov.pl/media/resources/20180411/Zachorowania1999-2015wojewodztwo.csv', delimiter=';');    
    data = data.drop('ICD10',axis=1)
    data = data.drop('Plec',axis=1)
    data = data.drop('Grupa_wieku',axis=1)
    year = data['Rok'].max()
    data = data[data['Rok']==year]
    data = data.drop('Rok', axis=1)
    grouped = data.groupby('Wojewodztwo').sum().reset_index()
    for index,row in grouped.iterrows():
        retDictionary[wojTable[row['Wojewodztwo']//2-1]]=row['Liczba']
    # print(retDictionary)
    return retDictionary