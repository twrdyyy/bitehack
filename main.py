from  createDictionary import *
import pandas

if __name__ == '__main__':
    data = pandas.DataFrame(createDictionary()).T
    print(data)
