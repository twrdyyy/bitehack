# -*- coding: utf-8 -*-
import pandas as pd
import requests
import zipfile
import io
import math

#LINK: https://www.dane.gov.pl/media/resources/20160114/rocznik-statystyczny-wojewodztw-2017-tablice.zip

def income(arg1):
    wojTable = ['Dolnoslaskie', 'Kujawsko-pomorskie', 'Lubelskie', 'Lubuskie', 'Lodzkie', 'Malopolskie', 'Mazowieckie', 'Opolskie', 'Podkarpackie', 'Podlaskie', 'Pomorskie', 'Slaskie', 'Swietokrzyskie', 'Warminsko-mazurskie', 'Wielkopolskie', 'Zachodnio-pomorskie' ]
    retDictionary = {wojTable[0]:{}, wojTable[1]:{}, wojTable[2]:{}, wojTable[3]:{}, wojTable[4]:{}, wojTable[5]:{}, wojTable[6]:{}, wojTable[7]:{}, wojTable[8]:{}, wojTable[9]:{}, wojTable[10]:{}, wojTable[11]:{}, wojTable[12]:{}, wojTable[13]:{}, wojTable[14]:{}, wojTable[15]:{}, "normal":{}}
    r = requests.get(arg1, stream=True)
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
