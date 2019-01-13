import math
from getDataUrl import *

def normalMaximum(UrlDict):
	res = {}
	firsKey = list(UrlDict.keys())[0]
	for issue in UrlDict[firsKey]:
		res.update({issue:UrlDict[firsKey][issue]})
	for key in UrlDict:
		if key!='normal':
			for issue in UrlDict[key]:
				res[issue] = max(res[issue],UrlDict[key][issue])
	# print(res)	
	return res
def normalRemap(UrlDict):
	res = {'min':{},'max':{}}
	firstKey = list(UrlDict.keys())[0]
	for issue in UrlDict[firstKey]:
		res['max'].update({issue:UrlDict[firstKey][issue]})
		res['min'].update({issue:UrlDict[firstKey][issue]})
	for key in UrlDict:
		if key!='normal':
			for issue in UrlDict[key]:
				res['max'][issue] = max(res['max'][issue],UrlDict[key][issue])
				res['min'][issue] = min(res['min'][issue],UrlDict[key][issue])
	
	# print(res)	
	return res


def normalize(UrlDict, func=None):
	if func=='Max':
		UrlDict['normal'] = normalMaximum(UrlDict)
	if func=='Remap':
		normal = normalRemap(UrlDict)
	for key in UrlDict:
		if key != 'normal':
			for issue in UrlDict[key]:	
				UrlDict[key][issue] = (UrlDict[key][issue]*(1.0/UrlDict['normal'][issue]) if func!='Remap' else (UrlDict[key][issue]-normal['min'][issue])/(normal['max'][issue]-normal['min'][issue]))
				if func==None:
					UrlDict[key][issue] += 1
					UrlDict[key][issue] /= 2
	return UrlDict

