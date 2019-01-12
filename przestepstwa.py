import pandas as pd

def SafetyDictionary(URL):
    Dane = {}
    df = pd.read_csv(URL, header=None, encoding="latin1", error_bad_lines=False, sep=";")
    #print(df)
    #print(df.iloc[[34]])

    Woj = {}
    Woj["KWP Kraków"] = 12
    Woj["KWP Rzeszów"] = 18
    Woj["KWP Lublin"] = 6
    Woj["KWP Bia³ystok"] = 20
    Woj["KWP Bydgoszcz"] = 22
    Woj["KWP Gdañsk"] = 22
    Woj["KWP Szczecin"] = 32
    Woj["KWP Wroc³aw"] = 2
    Woj["KWP Opole"] = 16
    Woj["KWP Katowice"] = 24
    Woj["KWP Olsztyn"] = 24
    Woj["KWP Kielce"] = 26
    Woj["KSP Warszawa"] = 14
    Woj["KWP z/s w Radomiu"] = 14
    Woj["KWP Gorzów Wielkpolski"] = 30
    Woj["KWP Poznañ"] = 30
    Woj["KWP £ód"] = 10

    k = 2
    retDictionary = {2:0, 4:0, 6:0, 8:0, 10:0, 12:0, 14:0, 16:0, 18:0, 20:0, 22:0, 24:0, 26:0, 28:0, 30:0, 32:0}

    tab = ["KWP Kraków", "KWP Rzeszów", "KWP Lublin", "KWP Bia³ystok", "KWP Bydgoszcz", "KWP Gdañsk", "KWP Szczecin", "KWP Wroc³aw", "KWP Opole", "KWP Katowice",
           "KWP Olsztyn", "KWP Kielce", "KSP Warszawa", "KWP z/s w Radomiu", "KWP Gorzów Wielkpolski", "KWP Poznañ", "KWP £ód"]

    for x, y, z in zip(df[df.columns[0]], df[df.columns[1]], df[df.columns[2]]):
        if x in tab and int(str(y)) > 2015:
            retDictionary[Woj[x]] += int(str(z))

    return retDictionary
