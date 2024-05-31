
# Kryds og boller

""" 
Stadie 1: 

    class spil: 
        ønskerSpil 
        logik
        
        logik.startspil()


    class spilLogik: 
        spilErAktiv: Bool
        ønsketSymbol : Str
        ønskerStart : Bool
        bræt : [str] 

        def __afbryd(): 
            spilErAktiv = False

        def __forberedSpil():
            Kryds eller bolle? 
            ØnskerStart? 
        
        def __tilføjSymbol(ønsketFælt) -> Bool: 
            Hvis ønsketFælt er optaget : return False 
            Hvis ønsketFælt ikke eksistere: return False
            Hvis ønsketFælt er et gyldigt træk:
                bræt[ønsketFælt] = ønsketSymbol
                return true
        
        def __afventTræk(): 
            trækGyldigt: Bool? = False
            while trækGyldigt != True
                Hvilket nummer fælt ønsker du at lave et træk på?
                TilføjSymbol(ønsketFælt) hvis gyldigt ændre trækGyldigt til True

        def __computerTræk(): 
            Tjek vindere for menneske <- Forsvar
            Tjek vindere for computer <- Angrib
            Tjek vindere for igangværende forsøg
                Er vinderen blokeret?

        def __lavRunde(): 
            hvis ønskerStart, afvent træk og derefter lad computeren vælge. 
                TjekScore()
            Hvis der ikke ønskes start, lad computeren vælge og afvent derefter træk. 
                TjekScore

        def kørSpil(): 
            __forberedSpil()
            while spilErAktiv: 
                __lavRunde(): 

        def __tjekScore(): 
            Har vundet?:
                gevinst():  
            Brættet fyldt?
                startSpil(): 
"""

from time import sleep
import os

class Formatter(): 
    def isIntInString(self, inp: str) -> bool:
        #Checks whether or not an int is in the string.
        if inp.isdigit(): 
            return True
        else: 
            return False 

    def standardFormat(self, inp: str) -> str: 
        #Ændrer str formattet så det kan sammenligninges.
        a = inp.strip().upper()
        return a

class SpilDisplay(): 
    def vis(self, bræt: list[str]):
        self.__Top()
        self.__fælter(bræt[1],bræt[2],bræt[3])
        self.__verticalSpacer() 
        self.__fælter(bræt[4], bræt[5], bræt[6])
        self.__verticalSpacer()
        self.__fælter(bræt[7], bræt[8], bræt[9], erBund = True)
        print("\n")

    def __fælter(self, nr1: int, nr2: int, nr3: int, erBund = False): 
        hSpacer = "   " #Horizontal margin
        margin = f"\t|{hSpacer} {hSpacer}|{hSpacer} {hSpacer}|{hSpacer} {hSpacer}|"
        centrum = f"\t|{hSpacer}{nr1}{hSpacer}|{hSpacer}{nr2}{hSpacer}|{hSpacer}{nr3}{hSpacer}|"
        bund = "\t|" + "_" * 7 + "|" + "_" * 7 + "|" + "_" * 7 + "|"
        
        if erBund == True: 
            print(margin)
            print(centrum)
            print(bund)
            return
        print(margin)
        print(centrum)
        print(margin)

    def __verticalSpacer(self): 
        print("\t|"+ "-" * 7 + "+" + "-" * 7 + "+" + "-" * 7 + "|") 

    def __Top(self, bund = False):
        print("\t " + "_" * 23)

class spilKonstanter(): 
    prioriteter: tuple(tuple()) = (
        [5], #Midten 
        [1,3,7,9], #Hjørner. 
        [2,4,6,8] #Rest 
    )
    vindere: tuple(tuple()) = (
        #Horisontale
        (1,2,3),
        (4,5,6),
        (7,8,9),

        #Vertikale
        (1,4,7),
        (2,5,8),
        (3,6,9),

        #På kryds af hinanden.
        (1,5,9),
        (3,5,7)
    )
    feltNumre: list[str] = ["1","2", "3", "4", "5", "6", "7", "8", "9"]

class SpilLogik(): 
    spilErAktivt: bool = None
    ønsketSymbol: str = None
    ønskerStart: bool = None
    bræt : list[str] = None
    format: Formatter = Formatter() 
    konstanter: spilKonstanter = spilKonstanter()
    display: SpilDisplay = SpilDisplay()

    def __clearTerminal(self): 
                os.system('cls')
                os.system('clear')

    def __afbryd(self): 
        self.spilErAktivt = False

    def __forberedSpil(self): 
        self.__clearTerminal()
        if self.ønsketSymbol != None: # Spillet er blevet initialiseret, brættet genstartes.
             self.bræt = self.konstanter.feltNumre[:]
             self.bræt.insert(0, "")
             return 

        #Resten af funktionen bliver kaldt, hvis spillet ikke er initialiseret: 
        self.bræt = self.konstanter.feltNumre[:]
        self.bræt.insert(0, "")
        self.spilErAktivt = True
        
        #Kryds eller bolle?? 
        print("Ønsker du at være kryds? Hvis ja skriv \"Ja\", ellers indtast noget vilkårligt for bolle")
        inp = self.format.standardFormat(inp = input())
        if inp == "JA": 
            self.ønsketSymbol = "X"
        else: 
            self.ønsketSymbol = "O"
        
        #Ønsker start?? 
        print("Ønsker du at starte? Hvis ja skriv \"Ja\" ellers indtast noget vilkårligt for at computeren starter")
        inp = self.format.standardFormat(input())
        if inp == "JA": 
            self.ønskerStart = True
        else: 
            self.ønskerStart = False
    
    def __gevinst(self, erMenneske: bool): 
        if erMenneske: 
            print("Hurra du har vundet")
        else: 
            print("Hvor er du dårlig, du tabte til en computer")
        
        self.__genstart()

    def __genstart(self): 
        print("Spillet genstartes")
        sleep(8)
        self.__forberedSpil()


    def __tjekScore(self, erMenneske: bool):
        
        def trePaaStripe(symbol: str) -> bool :
            harVundet: bool = False
            for vinder in self.konstanter.vindere: 
                for felt in vinder: 
                    if self.bræt[felt] == symbol: 
                        if vinder[-1] == felt:
                             harVundet = True
                        continue
                    else: 
                        break 
            return harVundet

        if erMenneske: 
            if trePaaStripe(self.ønsketSymbol): 
                self.__gevinst(erMenneske = True) 

        else: 
            if self.ønsketSymbol == "X": 
                if trePaaStripe("O"): 
                    self.__gevinst(erMenneske = False) 
    
            else: 
                if trePaaStripe("X"): 
                    self.__gevinst(erMenneske = False) 
        
        tal = self.konstanter.feltNumre 
        for i in tal: 
            if i in self.bræt: 
                return 
        self.__genstart() 
        
    
    def __tilføjSymbol(self, ØnsketFelt: int): 
        #Indsætter symbol i det ønskede felt. 
        
        self.bræt[ØnsketFelt] = self.ønsketSymbol

    def __afventTræk(self): 
        trækGyldigt : bool = False 

        while trækGyldigt != True:  
            ønsketFelt: str = ""
            while self.format.isIntInString(ønsketFelt) != True:  # 
                print("Hvilket felt ønsker du at lave dit træk i?")
                ønsketFelt = input()
                if self.format.isIntInString(ønsketFelt): 
                    trækGyldigt = True
                    self.__tilføjSymbol(int(ønsketFelt))
        self.display.vis(self.bræt)
        self.__tjekScore(erMenneske = True)
    
    def __computerTræk(self): 
        symbolPlaceret: bool = False
        symbol = "" # Computerens symbol
        if self.ønsketSymbol == "X": symbol = "O"
        else: symbol = "X" 

        def placerFelt(vinder: int) -> bool:
            if self.bræt[vinder] == str(vinder): 
                self.bræt[vinder] = symbol
                return True
            return False

        for vinder in self.konstanter.vindere: 
            #Angrib 
            if self.bræt[vinder[0]] == symbol and self.bræt[vinder[1]] == symbol \
            or self.bræt[vinder[1]] == symbol and self.bræt[vinder[2]] == symbol \
            or self.bræt[vinder[0]] == symbol and self.bræt[vinder[2]] == symbol: 
                #Placerer symbol i den der mangler for 3 på stribe. 
                for i in range(0, 3):
                    if placerFelt(vinder[i]) == True: 
                        symbolPlaceret = True 
                        break
            
            if symbolPlaceret: break 
            
            #Forsvar
            elif self.bræt[vinder[0]] == self.ønsketSymbol and self.bræt[vinder[1]] == self.ønsketSymbol \
            or self.bræt[vinder[1]] == self.ønsketSymbol and self.bræt[vinder[2]] == self.ønsketSymbol \
            or self.bræt[vinder[0]] == self.ønsketSymbol and self.bræt[vinder[2]] == self.ønsketSymbol: 
                #Placerer symbol i den der mangler for 3 på stribe. 
                for i in range(0, 3): 
                    symbolPlaceret = placerFelt(vinder[i])
        
        if symbolPlaceret: 
            self.display.vis(self.bræt)
            self.__tjekScore(erMenneske = False)
            return 
        #Bliver kun eksikveret, hvis ingen af de to scenarier ovenover var gældende.
        #Vælg det klogeste felt at tage. 
        for prioritet in self.konstanter.prioriteter: 
            for vinder in self.konstanter.vindere:
                for tal in prioritet: 
                    if tal in vinder:  #Tjek om prioriteten er en del af vinderen. Er løsningen også fri?
                        if self.bræt[vinder[0]] != self.ønsketSymbol and self.bræt[vinder[1]] != self.ønsketSymbol and self.bræt[vinder[2]] != self.ønsketSymbol: #Vinderen må være ledig.
                            self.bræt[tal] = symbol
                            symbolPlaceret = True
                            break
                    if symbolPlaceret == True: break
                if symbolPlaceret == True: break
            if symbolPlaceret == True: break
        self.display.vis(self.bræt)
        self.__tjekScore(erMenneske = False)
    
    def __lavRunde(self): 
        if self.ønskerStart: 
            self.__afventTræk()
            sleep(2)
            print("Computeren vælger felt")
            self.__computerTræk() 
        else: 
            self.__computerTræk()
            self.__afventTræk()
    
    def kørSpil(self):
        #Min main funktion, de andre funktioner er private og kan kun tilgåes indefra klassen. .
        self.__forberedSpil()
        self.display.vis(self.bræt)
        while self.spilErAktivt: 
            self.__lavRunde()






class Spil(): 
    ønskerSpil: bool = True
    logik: SpilLogik = SpilLogik()
    SpilLogik.kørSpil(logik)

bræt = [1,2,3,4,5,6,7,8,9]
bræt.insert(0,"")
display = SpilDisplay()
display.vis(bræt)

#Hvis computeren vinder opfatter den det som om, at det er mennesket der har vundet. 