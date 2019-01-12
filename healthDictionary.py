# -*- coding: utf-8 -*-
import pandas as pd
import requests
import zipfile
import io
import math

def healthDictionary(arg1):
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
                        tmpCount=4;
                        maks=0.0
                        for k in wojTable:
                            woj=wojTable[tmpCount-4]
                            tmpName='Unnamed: ' + str(tmpCount);
                            tmpCount=tmpCount+1;
                            retDictionary[woj][i]=baza[tmpName][itCount-1]
                            if baza[tmpName][itCount-1] > maks:
                                maks = baza[tmpName][itCount-1]
                        retDictionary["normal"][i]=maks
                itCount=itCount+1
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
