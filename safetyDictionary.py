import pandas as pd
def safetyDictionary():

    URL = {'gwałty':"https://www.dane.gov.pl/media/resources/20180521/postepowaniawszczete-zgwalcenie.csv",
           'morderstwa':"https://www.dane.gov.pl/media/resources/20180521/postepowaniawszczete-zabojstwo.csv",
           'kradzieże':"https://www.dane.gov.pl/media/resources/20180521/postepowaniawszczete-rozbojnicze.csv"}

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

    F = ['morderstwa', 'gwałty', 'kradzieże']

    retDictionary = {'Dolnoslaskie': {'morderstwa': 0, 'gwałty': 0, 'kradzieże': 0}, 'Kujawsko-pomorskie': {'morderstwa': 0, 'gwałty': 0, 'kradzieże': 0}, 'Lubelskie': {'morderstwa': 0, 'gwałty': 0, 'kradzieże': 0}, 'Lubuskie': {'morderstwa': 0, 'gwałty': 0, 'kradzieże': 0}, 'Lodzkie': {'morderstwa': 0, 'gwałty': 0, 'kradzieże': 0},
                     'Malopolskie': {'morderstwa': 0, 'gwałty': 0, 'kradzieże': 0}, 'Mazowieckie': {'morderstwa': 0, 'gwałty': 0, 'kradzieże': 0}, 'Opolskie': {'morderstwa': 0, 'gwałty': 0, 'kradzieże': 0},
                     'Podkarpackie': {'morderstwa': 0, 'gwałty': 0, 'kradzieże': 0}, 'Podlaskie': {'morderstwa': 0, 'gwałty': 0, 'kradzieże': 0}, 'Pomorskie': {'morderstwa': 0, 'gwałty': 0, 'kradzieże': 0}, 'Slaskie': {'morderstwa': 0, 'gwałty': 0, 'kradzieże': 0}, 'Swietokrzyskie': {'morderstwa': 0, 'gwałty': 0, 'kradzieże': 0},
                     'Warminsko-mazurskie': {'morderstwa': 0, 'gwałty': 0, 'kradzieże': 0},
                     'Wielkopolskie': {'morderstwa': 0, 'gwałty': 0, 'kradzieże': 0}, 'Zachodnio-pomorskie': {'morderstwa': 0, 'gwałty': 0, 'kradzieże': 0}, 'Normal' : {'morderstwa': 0, 'gwałty': 0, 'kradzieże': 0}}

    tab = ["KWP Kraków", "KWP Rzeszów", "KWP Lublin", "KWP Bia³ystok", "KWP Bydgoszcz", "KWP Gdañsk", "KWP Szczecin",
           "KWP Wroc³aw", "KWP Opole", "KWP Katowice",
           "KWP Olsztyn", "KWP Kielce", "KSP Warszawa", "KWP z/s w Radomiu", "KWP Gorzów Wielkpolski", "KWP Poznañ",
           "KWP £ód"]



    for arg in F:
        df = pd.read_csv(URL[arg], header=None, encoding="latin1", error_bad_lines=False, sep=";")
        print(arg)
        for x, y, z in zip(df[df.columns[0]], df[df.columns[1]], df[df.columns[2]]):
            if x in tab and int(str(y)) > 2015:
                #print(x + " " + y + " " + z)
                retDictionary[Woj[x]][arg] -= int(z.replace(" ", ""))

        maxi = 0
        for j in retDictionary:
            for k in F:
                if k == arg and retDictionary[j][k] < maxi:
                    maxi = retDictionary[j][k]
        retDictionary['Normal'][arg] = maxi

    #print(retDictionary)

    return retDictionary
if __name__ == '__main__'
print(safetyDictionary())
