from random import randint
def best(data):
    return list(data.keys())[randint(0,len(list(data.keys())))]