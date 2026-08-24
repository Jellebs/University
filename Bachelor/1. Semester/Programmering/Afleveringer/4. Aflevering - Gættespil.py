import os
import random
from textwrap import indent
import time
from turtle import clear
from xmlrpc.client import Boolean

class Gættespil: 
    maxGæt: int = 0
    gæt: int = 0
    hemmeligtTal: int = 0

    def __init__(self, maxGæt):
        self.maxGæt = maxGæt
    
    def prøvSpil(self): 
        ØnskerOmmer: bool = True
        def lavHemmeligtTal():
            self.hemmeligtTal = random.randint(1,100)
        def clearTerminal(): 
                os.system('cls')
                os.system('clear')
        def gevinst(): 
            animationCount = 4
            tab = "\t"
            newLine = "\n"
            clearTerminal()
            #Linje 31 -> 86 er animation.
            def fyrværkeri(i): 
                clearTerminal()
                def verticalLine(withSides: bool, bottom: bool): 
                    if withSides == True and bottom == False:
                        print(tab*8 + "|")
                        print(tab*7 + "      " + "\ | / ")
                    elif withSides == True and bottom == True: 
                        print(tab*7 + "      " + "/ | \ ")
                        print(tab*8 + "|")
                    else: 
                        print(tab*8 + "|")

                def makeTrail(): 
                    verticalLine(False, False)
                    verticalLine(False, False)
                
                def makeCore(stadie): 
                    if stadie == 1: 
                        verticalLine(False, False)
                        print(tab*7 + "     " + "--   --")
                        verticalLine(False, False)
                    elif stadie == 2: 
                        verticalLine(True, False)
                        print(tab*7 + "    " + "---   ---")
                        verticalLine(True, True)
                
                def verticalSpacing(spacing): 
                    print(newLine*spacing)

                verticalSpacing(20)
                if i == 0: 
                    makeTrail()
                    verticalSpacing(2)
                elif i == 1: 
                    makeTrail()
                    newLine
                    makeTrail()
                    verticalSpacing(4)
                elif i == 2: 
                    makeCore(1)
                    newLine
                    makeTrail()
                    verticalSpacing(6)
                elif i == 3: 
                    makeCore(2)
                    verticalSpacing(6)
                else: 
                    return 
            
            for i in range(0, animationCount): 
                print("\n")
                fyrværkeri(i)
                if i == animationCount -1: 
                    print("Hurra, du har vundet!!")
                time.sleep(1.5) 
        #Logik
        def gætTal():
            print("Gæt et tal: ")
            self.gæt = int(input())
            print("\n")
            def tjekVærdi():
                if self.gæt > self.hemmeligtTal: 
                    print("Dit tal er højere end det hemmelige tal")
                elif self.gæt < self.hemmeligtTal: 
                    print("Dit tal er lavere end det hemmelige tal")
                else:
                    gevinst()

            tjekVærdi()
        
        def startSpil(): 
            clearTerminal()
            lavHemmeligtTal()
            for _ in range(0, self.maxGæt):
                if self.gæt == self.hemmeligtTal: 
                    break
                gætTal()

        startSpil()
        def reaktion() -> bool: 
            reaktion = input()         
            if reaktion.upper().strip() == "JA":
                return True
            else: 
                return False

        def tab() -> bool:
            print("Game over, du klarede den desværre ikke, men det skal ikke stoppe dig fra at prøve igen")
            print("Har du lyst til at prøve igen Ja/Nej")
            return reaktion()
        def vundet() -> bool: 
            print("Har du lyst til at prøve igen? Ja/Nej")
            return reaktion()
        while ØnskerOmmer == True:
            if self.gæt == self.hemmeligtTal: 
                ØnskerOmmer = vundet()
                
            elif self.gæt != self.hemmeligtTal: 
                ØnskerOmmer = tab()
            if ØnskerOmmer == True:
                startSpil()
            else: 
                clearTerminal()
            

Aflevering4 = Gættespil(5) 
Aflevering4.prøvSpil()







