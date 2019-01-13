import pandas as pd
import numberResidents

def safetyDictionary(url):
    numberOfResidents = numberResidents.numberResidents()
    # URL = {'gwałty':"https://www.dane.gov.pl/media/resources/20180521/postepowaniawszczete-zgwalcenie.csv",
        #    'morderstwa':"https://www.dane.gov.pl/media/resources/20180521/postepowaniawszczete-zabojstwo.csv",
        #    'kradzieże':"https://www.dane.gov.pl/media/resources/20180521/postepowaniawszczete-rozbojnicze.csv"}

    Woj = {}
    Woj["KWP Kraków"] = 'Malopolskie'
    Woj["KWP Rzeszów"] = 'Podkarpackie'
    Woj["KWP Lublin"] = 'Lubelskie'
    Woj["KWP Bia³ystok"] = 'Podlaskie'
    Woj["KWP Bydgoszcz"] = 'Kujawsko-pomorskie'
    Woj["KWP Gdañsk"] = 'Pomorskie'
    Woj["KWP Szczecin"] = 'Zachodnio-pomorskie'
    Woj["KWP Wroc³aw"] = 'Dolnoslaskie'
    Woj["KWP Opole"] = 'Opolskie'
    Woj["KWP Katowice"] = 'Slaskie'
    Woj["KWP Olsztyn"] = 'Warminsko-mazurskie'
    Woj["KWP Kielce"] = 'Swietokrzyskie'
    Woj["KSP Warszawa"] = 'Mazowieckie'
    Woj["KWP z/s w Radomiu"] ='Mazowieckie'
    Woj["KWP Gorzów Wielkpolski"] = 'Lubuskie'
    Woj["KWP Poznañ"] = 'Wielkopolskie'
    Woj["KWP £ód"] = 'Lodzkie'

    wojTable = ['Dolnoslaskie', 'Kujawsko-pomorskie', 'Lubelskie', 'Lubuskie', 'Lodzkie', 'Malopolskie', 'Mazowieckie',
                'Opolskie', 'Podkarpackie',
                'Podlaskie', 'Pomorskie', 'Slaskie', 'Swietokrzyskie', 'Warminsko-mazurskie', 'Wielkopolskie',
                'Zachodnio-pomorskie']
    # nazwa wojewodztwa = wojTable[liczba//2-1]

    F = ['murder', 'rape', 'theft']

    retDictionary = {}
    for woj in wojTable:
        retDictionary[woj]={'murder':0,'rape':0,'theft':0}
    retDictionary['normal']={'murder':0,'rape':0,'theft':0}

    tab = ["KWP Kraków", "KWP Rzeszów", "KWP Lublin", "KWP Bia³ystok", "KWP Bydgoszcz", "KWP Gdañsk", "KWP Szczecin",
           "KWP Wroc³aw", "KWP Opole", "KWP Katowice",
           "KWP Olsztyn", "KWP Kielce", "KSP Warszawa", "KWP z/s w Radomiu", "KWP Gorzów Wielkpolski", "KWP Poznañ",
           "KWP £ód"]



    for arg in F:
        df = pd.read_csv(url[arg], header=None, encoding="latin1", error_bad_lines=False, sep=";")
        # print(arg)
        for x, y, z in zip(df[df.columns[0]], df[df.columns[1]], df[df.columns[2]]):
            if x in tab and int(str(y)) > 2015:
                retDictionary[Woj[x]][arg] -= int(z.replace(" ", ""))

    #print(retDictionary)

    for x in retDictionary:
        if x!='normal':
            for y in retDictionary[x]:
                retDictionary[x][y] = retDictionary[x][y] * (numberOfResidents['All'] / float(numberOfResidents[x]))
    for arg in F:
        maxi = 0
        for j in retDictionary:
            for k in F:
                if k == arg and retDictionary[j][k] < maxi:
                    maxi = retDictionary[j][k]
        retDictionary['normal'][arg] = maxi

    return retDictionary


if __name__ == '__main__':
    from getDataUrl import *
    print(safetyDictionary(getUrlDict()['safety']))
