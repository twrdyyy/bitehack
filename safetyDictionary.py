import pandas as pd

def safetyDictionary(URL, LiczbaLudnosci):
    Dane = {}
    df = pd.read_csv(URL, header=None, encoding="latin1", error_bad_lines=False, sep=";")
    #print(df)
    #print(df.iloc[[34]])

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

    wojTable = ['Dolnoslaskie', 'Kujawsko-pomorskie', 'Lubelskie', 'Lubuskie', 'Lodzkie', 'Malopolskie', 'Mazowieckie', 'Opolskie', 'Podkarpackie',
                'Podlaskie', 'Pomorskie', 'Slaskie', 'Swietokrzyskie', 'Warminsko-mazurskie', 'Wielkopolskie', 'Zachodnio-pomorskie' ]
    # nazwa wojewodztwa = wojTable[liczba//2-1]
    retDictionary = {'Dolnoslaskie':0, 'Kujawsko-pomorskie':0, 'Lubelskie':0, 'Lubuskie':0, 'Lodzkie':0, 'Malopolskie':0, 'Mazowieckie':0, 'Opolskie':0, 'Podkarpackie':0, 'Podlaskie':0, 'Pomorskie':0, 'Slaskie':0, 'Swietokrzyskie':0, 'Warminsko-mazurskie':0, 'Wielkopolskie':0, 'Zachodnio-pomorskie':0}

    tab = ["KWP Kraków", "KWP Rzeszów", "KWP Lublin", "KWP Bia³ystok", "KWP Bydgoszcz", "KWP Gdañsk", "KWP Szczecin", "KWP Wroc³aw", "KWP Opole", "KWP Katowice",
           "KWP Olsztyn", "KWP Kielce", "KSP Warszawa", "KWP z/s w Radomiu", "KWP Gorzów Wielkpolski", "KWP Poznañ", "KWP £ód"]

    for x, y, z in zip(df[df.columns[0]], df[df.columns[1]], df[df.columns[2]]):
        if x in tab and int(str(y)) > 2015:
            retDictionary[Woj[x]] += int(str(z))

    maxi = 0
    for i in retDictionary:
        if i > maxi:
            maxi = i

    for i in retDictionary:
        i = i / float(maxi) * 100

    return retDictionary
