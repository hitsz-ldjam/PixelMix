from xml.etree.ElementTree import *

class Preferences:
    def __init__(self, filename):
        self.__filename = filename
        self.__tree = parse(filename)

    # def __del__(self):
    #     self.savePreference()

    def getPreference(self, preferenceName):
        return self.__tree.getroot().findall(preferenceName)[0].text

    def setPreference(self, preferenceName, value):
        self.__tree.getroot().findall(preferenceName)[0].text = str(value)

    def savePreference(self):
        self.__tree.write(self.__filename)
