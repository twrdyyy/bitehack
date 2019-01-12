from getDataUrl import getUrlDict
import healthDictionary
import unemploymentDictionary

if __name__ == '__main__':
    print(unemploymentDictionary.unemploymentDictionary(getUrlDict()['economy']['unemployment']))