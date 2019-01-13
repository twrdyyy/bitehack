# from random import randint
import operator
def best(VarDict):
    # return list(VarDict.keys())[randint(0,len(list(VarDict.keys()))-2)]
    sumDict = {}
    for key in VarDict:
        sumDict[key] = sum([VarDict[key][x] **2 for x in ['Economy','Health','Safety']])
    return max(sumDict.items(), key=operator.itemgetter(1))[0]

