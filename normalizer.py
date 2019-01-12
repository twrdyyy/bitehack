import math
from getDataUrl import *


def normalize(UrlDict):
	
	for key in UrlDict:
		if key != 'normal':
			for issue in UrlDict[key]:	
				UrlDict[key][issue] *= (1.0/UrlDict['normal'][issue])
				UrlDict[key][issue] += 1
				UrlDict[key][issue] /= 2
	return UrlDict

