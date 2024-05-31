from .TimeData import TimeData
#https://docs.python.org/3/tutorial/modules.html#intra-package-references

    
class VejrData: 
    #Lists containing hourly data 
    __dato: str = None
    __timeData: list = None

    def __init__(self, dato):
        self.__dato = dato
    
    def dato(self): 
        return self.__dato

    def timeData(self) -> list[TimeData]: 
        return self.__timeData

    def addToList(self, timeData: TimeData): 
        if self.__timeData is None: 
            self.__timeData = []
        self.__timeData.append(timeData)