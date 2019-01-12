# -*- coding: utf-8 -*-
import pandas as pd
import requests
import zipfile
import io
import math
import numberResidents

categoriesSearch = ['Samoocena stanu zdrowia', 'Długotrwałe problemy zdrowotne', 'Chorujący przewlekle', 'Niepełnosprawność wg kryterium polskiego', 'Opóźnienia w dostępie z powodu długiego  czasu oczekiwania','Nowotwory']

def healthCriteria():
    return posSearch

def healthDictionary(healthUrls):
    mainDict = mainHealthDictionary(healthUrls['health'])
    tumorDict = tumorDictionary(healthUrls['tumor'])
    for wojewodztwo in mainDict.keys():
        mainDict[wojewodztwo]={**mainDict[wojewodztwo],**tumorDict[wojewodztwo]}
    return mainDict


def mainHealthDictionary(arg1):
    posSearch = ['Samoocena stanu zdrowia', 'Długotrwałe problemy zdrowotne', 'Chorujący przewlekle', 'Niepełnosprawność wg kryterium polskiego', 'Opóźnienia w dostępie z powodu długiego  czasu oczekiwania']
    wojTable = ['Dolnoslaskie', 'Kujawsko-pomorskie', 'Lubelskie', 'Lubuskie', 'Lodzkie', 'Malopolskie', 'Mazowieckie', 'Opolskie', 'Podkarpackie', 'Podlaskie', 'Pomorskie', 'Slaskie', 'Swietokrzyskie', 'Warminsko-mazurskie', 'Wielkopolskie', 'Zachodnio-pomorskie' ]
    retDictionary = {wojTable[0]:{}, wojTable[1]:{}, wojTable[2]:{}, wojTable[3]:{}, wojTable[4]:{}, wojTable[5]:{}, wojTable[6]:{}, wojTable[7]:{}, wojTable[8]:{}, wojTable[9]:{}, wojTable[10]:{}, wojTable[11]:{}, wojTable[12]:{}, wojTable[13]:{}, wojTable[14]:{}, wojTable[15]:{}, "normal":{}}
    r = requests.get(arg1, stream=True)
    with zipfile.ZipFile(io.BytesIO(r.content)) as z:
        with z.open("P1.xlsx") as f:
            baza = pd.read_excel(f)
            tablica1=baza['Unnamed: 0'].values
            itCount=1
            for i in tablica1:
                for j in posSearch:
                    if i == j:
                        tmpCount=4
                        maks=0.0
                        for k in wojTable:
                            woj=wojTable[tmpCount-4]
                            tmpName='Unnamed: ' + str(tmpCount)
                            tmpCount=tmpCount+1
                            retDictionary[woj][i]=baza[tmpName][itCount-1]
                            if i != posSearch[0]:
                                retDictionary[woj][i]*=-1
                            if baza[tmpName][itCount-1] > maks:
                                maks = baza[tmpName][itCount-1]
                        retDictionary["normal"][i]=maks
                itCount=itCount+1
    return retDictionary

def tumorDictionary(url):
    wojTable = ['Dolnoslaskie', 'Kujawsko-pomorskie', 'Lubelskie', 'Lubuskie', 'Lodzkie', 'Malopolskie', 'Mazowieckie', 'Opolskie', 'Podkarpackie', 'Podlaskie', 'Pomorskie', 'Slaskie', 'Swietokrzyskie', 'Warminsko-mazurskie', 'Wielkopolskie', 'Zachodnio-pomorskie' ]
    retDictionary = {wojTable[0]:{}, wojTable[1]:{}, wojTable[2]:{}, wojTable[3]:{}, wojTable[4]:{}, wojTable[5]:{}, wojTable[6]:{}, wojTable[7]:{}, wojTable[8]:{}, wojTable[9]:{}, wojTable[10]:{}, wojTable[11]:{}, wojTable[12]:{}, wojTable[13]:{}, wojTable[14]:{}, wojTable[15]:{}}
    numberOfResidents = numberResidents.numberResidents()

    data = pd.read_csv(url, delimiter=';');    
    data = data.drop('ICD10',axis=1)
    data = data.drop('Plec',axis=1)
    data = data.drop('Grupa_wieku',axis=1)
    year = data['Rok'].max()
    data = data[data['Rok']==year]
    data = data.drop('Rok', axis=1)
    grouped = data.groupby('Wojewodztwo').sum().reset_index()
    normalId = 0
    normal = grouped['Liczba'][normalId]*numberOfResidents['All']/numberOfResidents[wojTable[grouped['Wojewodztwo'][normalId]//2-1]]
    for index,row in grouped.iterrows():
        valuePerResident =(row['Liczba']*numberOfResidents['All']/numberOfResidents[wojTable[row['Wojewodztwo']//2-1]])
        normal = max(normal,valuePerResident)
        retDictionary[wojTable[row['Wojewodztwo']//2-1]]={"Nowotwory":-1*valuePerResident}
    retDictionary['normal']={'Nowotwory':normal}    
    return retDictionary

'''
#Kod do testowania, czy zwraca poprawne wartości
healthDictionary("https://stat.gov.pl/download/gfx/portalinformacyjny/pl/defaultaktualnosci/5513/6/6/1/stan_zdrowia_ludnosci_polski_w_2014_r-tablie.zip")            
for i in retDictionary:
    print(i)
    for j in retDictionary[i]:
        print(j)
        print(retDictionary[i][j])
'''
