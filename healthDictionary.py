# -*- coding: utf-8 -*-
import pandas as pd
import requests
import zipfile
import io
import math

posSearch = ['Samoocena stanu zdrowia', 'Długotrwałe problemy zdrowotne', 'Chorujący przewlekle', 'Niepełnosprawność wg kryterium polskiego', 'Opóźnienia w dostępie z powodu długiego  czasu oczekiwania']
wojTable = ['Dolnoslaskie', 'Kujawsko-pomorskie', 'Lubelskie', 'Lubuskie', 'Lodzkie', 'Malopolskie', 'Mazowieckie', 'Opolskie', 'Podkarpackie', 'Podlaskie', 'Pomorskie', 'Slaskie', 'Swietokrzyskie', 'Warminsko-mazurskie', 'Wielkopolskie', 'Zachodnio-pomorskie' ]
retDictionary = {wojTable[0]:{}, wojTable[1]:{}, wojTable[2]:{}, wojTable[3]:{}, wojTable[4]:{}, wojTable[5]:{}, wojTable[6]:{}, wojTable[7]:{}, wojTable[8]:{}, wojTable[9]:{}, wojTable[10]:{}, wojTable[11]:{}, wojTable[12]:{}, wojTable[13]:{}, wojTable[14]:{}, wojTable[15]:{}}

def healthDictionary(arg1):
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
                        for k in wojTable:
                            woj=wojTable[tmpCount-4]
                            tmpName='Unnamed: ' + str(tmpCount);
                            tmpCount=tmpCount+1;
                            retDictionary[woj][i]=baza[tmpName][itCount-1]
                itCount=itCount+1
    return retDictionary