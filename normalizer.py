from unemploymentDictionary import * 
from healthDictionary import *
import math
from getDataUrl import *


def normalize(UrlDict):
	
	for key in UrlDict:
		for issue in UrlDict[key]:
			pass


if __name__ == '__main__':
	health = healthDictionary(getUrlDict()['health'])
	unemp = unemploymentDictionary(getUrlDict()['economy']['unemployment'])
	tumor = tumorDictionary(getUrlDict()['health']["tumor"])

	for key in health:
		for issue in health[key]:
			print( key + ' ' + issue + ' ' + str(health[key][issue]))
			#ReLu
			health[key][issue] *= (-1)*(1.0/health['normal'][issue])

			if issue == "samoocena stanu zdrowia":
				health[key][issue] *= -1
			print( key + ' ' + issue + ' ' + str(health[key][issue]))