import json

def readJsonFile(filename):
    data = ""
    try:
        with open(filename) as jsonFile:
            data = json.load(jsonFile)
    except IOError:
        print("could not read the file")
    return data