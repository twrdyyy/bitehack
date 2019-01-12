from unemploymentDictionary import * 
from healthDictionary import *
import math
from getDataUrl import *

if __name__ == '__main__':
	health = healthDictionary(getUrlDict()['health']['health'])
	unemp = unemploymentDictionary(geturlDict()['economy']['unemployment'])
	tumor = tumorDictionary(getUrlDict()['health']["tumor"])

	print(health)