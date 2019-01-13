def getResult(VarDict):
	
	max_ = {}
	res_ = ['', 0]
	for key in VarDict:
		for var_ in VarDict[key]:
			max_[key] += VarDict[key][var_]
		if max_[key] > res_[1]:
			res_[1] = max_key
			res[0] = key
	
	return res_	
	
