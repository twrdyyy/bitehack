from healthDictionary import *
from economyDictionary import *
from safetyDictionary import *
from normalizer import *

def createDictionary():
    #Tablica wojewodztw
    wojTable = ['Dolnoslaskie', 'Kujawsko-pomorskie', 'Lubelskie', 'Lubuskie', 'Lodzkie', 'Malopolskie', 'Mazowieckie', 'Opolskie', 'Podkarpackie', 'Podlaskie', 'Pomorskie', 'Slaskie', 'Swietokrzyskie', 'Warminsko-mazurskie', 'Wielkopolskie', 'Zachodnio-pomorskie' ]
    #Słownik: {wojewodztwo:{kategoria:wartość}}
    retDictionary = {wojTable[0]:{}, wojTable[1]:{}, wojTable[2]:{}, wojTable[3]:{}, wojTable[4]:{}, wojTable[5]:{}, wojTable[6]:{}, wojTable[7]:{}, wojTable[8]:{}, wojTable[9]:{}, wojTable[10]:{}, wojTable[11]:{}, wojTable[12]:{}, wojTable[13]:{}, wojTable[14]:{}, wojTable[15]:{}, "normal":{} }
    #========ECONOMY========
    tempDict=economyDictionary(getUrlDict()['economy'])
    tempDict=normalize(tempDict)
    #Dla kazdego wojewodztwa w EconomyDictionary
    for i in tempDict:
        #Dla kazdej kategorii w wojewodztwie zsumuj wyniki        
        suma=0.0
        for j in tempDict[i]:
            suma=suma+tempDict[i][j]
        #Podziel sume przez ilosc kategorii i zapisz
        retDictionary[i]["Economy"]=suma/len(tempDict[i])
    #========HEALTH========
    tempDict=healthDictionary(getUrlDict()['health'])
    tempDict=normalize(tempDict)
    #Dla kazdego wojewodztwa w HealthDirectory
    for i in tempDict:
        #Dla kazdej kategorii w wojewodztwie zsumuj wyniki
        suma=0.0
        for j in tempDict[i]:
            suma=suma+tempDict[i][j]
        #Podziel sume przez ilosc kategorii i zapisz
        retDictionary[i]["Health"]=suma/len(tempDict[i])
    #========Safety========
    tempDict=safetyDictionary(getUrlDict()['safety'])
    tempDict=normalize(tempDict)
    #Dla kazdego wojewodztwa w SafetyDictionary
    for i in tempDict:
        #Dla kazdej kategorii w wojewodztwie zsumuj wyniki
        suma=0.0
        for j in tempDict[i]:
            suma=suma+tempDict[i][j]
        #Podziel sume przez ilosc kategorii i zapisz
        retDictionary[i]["Safety"]=suma/len(tempDict[i])
    # return retDictionary
    return normalize(retDictionary,'Remap')
