from apiclient import APIClient
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class daneGovPl(APIClient):
    BASE_URL = 'https://api.dane.gov.pl/resources/'
    def callDataset(self,ID):
        # print(self.call(ID))
        return self.call(ID)['data']['attributes']['file_url']

def getUrlList():
    res = []
    daneGov = daneGovPl()
     
    res.append(tuple(["health","tumor",daneGov.callDataset('3945')]))
    res.append(tuple(["safety","murder",daneGov.callDataset('10420')]))
    res.append(tuple(["safety","rape",daneGov.callDataset('10445')]))
    res.append(tuple(["safety","theft",daneGov.callDataset('10431')]))
    res.append(tuple(["safety","drugs",daneGov.callDataset('10451')]))
    res.append(tuple(["safety","battery",daneGov.callDataset('5938')]))


    return res

if __name__ == '__main__':
    print(getUrlList())   
