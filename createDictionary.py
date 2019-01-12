'''
Funkcja tworząca słownik zawierający wszystkie słowniki
WIP, czekamy na resztę funkcji
'''

def createDictionary():
    URLDict=GetUrlDict()
    #Create base dictionary using healthDictionary()
    retDict=healthDictionary(URLDict["Health"])
    catList=healthCriteria()
    #Unemployment
    tempDict=unemploymentDictionary(URLDict["Unemployment"])
    catList.append("Unemployment")
    for i in tempDict:
        retDict[i]["Unemployment"]=tempDict[i]
    #Safety
    tempDict=safetyDictionary(URLDict["Safety"])
    catList.append("Safety")
    for i in tempDict:
        retDict[i]["Safety"]=tempDict[i]
    #
