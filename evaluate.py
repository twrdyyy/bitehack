# from random import randint
import operator
def best(VarDict):
    # return list(VarDict.keys())[randint(0,len(list(VarDict.keys()))-2)]
    '''
    max_ = {}
    res_ = ['', 0]
    for key in VarDict:
        max_[key]=0
    for key in VarDict:
        for var_ in VarDict[key]:
            max_[key] += VarDict[key][var_]
        if max_[key] > res_[1]:
            res_[1] = max_[key]
            res_[0] = key
    return res_[0]
    '''
    sumDict = {}
    for key in VarDict:
        sumDict[key] = sum([VarDict[key][x] for x in ['Economy','Health','Safety']])
    return max(sumDict.items(), key=operator.itemgetter(1))[0]

