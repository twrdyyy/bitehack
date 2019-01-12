# -*- coding: utf-8 -*-
import pandas as pd

Dane = {}
df = pd.read_csv("https://www.dane.gov.pl/media/resources/20180521/postepowaniawszczete-zgwalcenie.csv", header=None, encoding="latin1", error_bad_lines=False, sep=";")
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
Rep = [0]*33

tab = ["KWP Kraków", "KWP Rzeszów", "KWP Lublin", "KWP Bia³ystok", "KWP Bydgoszcz", "KWP Gdañsk", "KWP Szczecin", "KWP Wroc³aw", "KWP Opole", "KWP Katowice",
       "KWP Olsztyn", "KWP Kielce", "KSP Warszawa", "KWP z/s w Radomiu", "KWP Gorzów Wielkpolski", "KWP Poznañ", "KWP £ód"]

for x, y, z in zip(df[df.columns[0]], df[df.columns[1]], df[df.columns[2]]):
    if x in tab and int(str(y)) > 2015:
        Rep[Woj[x]] += int(str(z))

print(Rep)
