from calendar import weekday
import datetime as dt
from time import strftime
from typing import Dict

class Aflevering_SkudÅr: 
    __ugeDage: dict = {}
    initialYear: int
    endYear: int

    def setupDict(self, fra,til): 
        initialRest = fra % 4
        self.initialYear = fra + initialRest
        endRest = til % 4
        self.endYear = til + endRest
        
        def getWeekDay(year): 
            day = dt.date(year, 2,29)
            #En del af f strings funktioner kan få komponentet omskrevet til læselig datoer: 
            return day.strftime("%A")

        for year in range(self.initialYear, self.endYear, +4): 
            if year % 100 == 0: 
                if year % 400 == 0: 
                    self.__ugeDage.update({ year : getWeekDay(year)}) 
            else: 
                self.__ugeDage.update({ year : getWeekDay(year)}) 

    def printValues(self):
        #Typisk brugte
        tab = "\t"
        n = "\n"

        #Hjælpe funktioner
        def newLine(): 
            print(n)

        def makeMargin(i): 
            linje = "["+ tab*10 + "]"
            print((linje+n)*(i-1)+linje)
        
        def horizontalBorder(symbol):
            if (type(symbol) == type("")):
                print(symbol*80)
            else: 
                print(f"Ah den går ikke makker, det er en {type(symbol)} ikke en <class 'str'>")

        def printPænt():
            newLine() 
            horizontalBorder("_")
            makeMargin(3)

        def endPrint():
            makeMargin(2)
            horizontalBorder("-")
            newLine()

        def makeHeader(title, credit): 
            bold = '\033[1m'
            nonBold = '\033[0m'
            italic = "\x1B[3m"
            nonItalic = "\x1B[0m"

            def format(formatÆndring, formatTilbageStiller, text, antalTabs): 
                if (type(formatÆndring) != type("") or type(formatTilbageStiller) != type("") or type(text) != type("")): 
                    print(f"Fejl i format, en af følgende er ikke en string: 1. {type(formatÆndring)}, 2.{type(formatTilbageStiller)}, 3. {type(text)}")
                    return
                elif type(antalTabs) != type(1): 
                    print(f"Fejl i format, antalTabs er ikke en integer")
                    return 
                else: 
                    return "[" + tab + formatÆndring + text + formatTilbageStiller + "\t"*antalTabs + "]"

            print(format(bold, nonBold, title, 6))
            print(format(italic, nonItalic, credit, 5))
            makeMargin(1)

        def makeBody(): 
            for key in self.__ugeDage:
                tekst = f"Skudår i år {key}, var på en {self.__ugeDage[key]}"
                print("[" + tab + tekst + tab*5 +"]")
        
        #Actions 
        printPænt()
        makeHeader(f"Skudår fra år {self.initialYear} til {self.endYear}", "Aflevering lavet af Jesper Bertelsen")
        makeBody()  
        endPrint()


aflevering3 = Aflevering_SkudÅr
aflevering3.setupDict(aflevering3,1850,2050)
aflevering3.printValues(aflevering3)





    
    

