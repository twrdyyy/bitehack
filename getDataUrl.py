from apiclient import APIClient
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class daneGovPl(APIClient):
    BASE_URL = 'https://api.dane.gov.pl/resources/'
    def callDataset(self,ID):
        return self.call(ID)['data']['attributes']['file_url']

def getUrlDict():
    res = {"health":{},"safety":{},"economy":{}}
    daneGov = daneGovPl()     
    res["health"].update({"tumor":daneGov.callDataset('3945')})
    res["safety"].update({"murder":daneGov.callDataset('10420')})
    res["safety"].update({"rape":daneGov.callDataset('10445')})
    res["safety"].update({"theft":daneGov.callDataset('10431')})
    res["safety"].update({"drugs":daneGov.callDataset('10451')})
    res["safety"].update({"battery":daneGov.callDataset('5938')})
    res["health"].update({"health":'https://stat.gov.pl/download/gfx/portalinformacyjny/pl/defaultaktualnosci/5513/6/6/1/stan_zdrowia_ludnosci_polski_w_2014_r-tablie.zip'})
    res["economy"].update({"unemployment":"https://stat.gov.pl/download/gfx/portalinformacyjny/pl/defaultaktualnosci/5473/2/39/1/pow11_15____.xls"})
    return res

if __name__ == '__main__':
    # tumor.tumorDictionary(getUrlDict()['health']['tumor'])
    # print(tumor.healthDictionary(getUrlDict()['health']['health']))
    # print(getUrlDict())
    #print(tumor.healthDictionary(getUrlDict()['health']))
    # print(healthDictionary.healthDictionary(getUrlDict()['health']))
    # getUrlDict()['economy']['unemployment']
    pass