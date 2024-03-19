import json

# Open input config
def loadconfig():
    fileHandler = open('..\input\config.json')
    data = json.load(fileHandler)


def validateconfig():
