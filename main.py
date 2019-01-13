from  createDictionary import *
import pandas

if __name__ == '__main__':
    data = pandas.DataFrame(createDictionary()).drop('normal',axis=1).T
    print(data)
