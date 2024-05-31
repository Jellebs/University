from array import array
from multiprocessing.dummy import Array
from sys import modules
from typing import List


class aflevering:
    fibonacciTal = [] 
    tværSumsTal = [] 
    tværSumsTotal = []
    antalAtPrinte = 100
    def __init__(self):
        self.lavFibonacciListe() 
        #Lav tværsum liste 
        self.udregnTværsum(True)
        #Lav tværsums total liste 
        self.udregnTværsum(False)

    def lavFibonacciListe(self): 
        self.fibonacciTal.append(1)
        self.fibonacciTal.append(1)
        for i in range(2, 100):
            self.fibonacciTal.append((self.fibonacciTal[i-1] + self.fibonacciTal[i-2]))
    
    def udregnTværsum(self, fib):
        dict = []
        for tal in range(0, self.antalAtPrinte): 
            #Min metode: 
            # Et tal indsættes og "moduleres" for at finde resten efter division af 10. 
            # Et nyt tal findes ved at dele det samme tal med 10, denne moduleres også på samme måde. 
            # Processen fortsætter indtil at længden af tallet er 1, da er bunden nået.
            number: int
            if fib: 
                number = self.fibonacciTal[tal]
            else: 
                number = self.tværSumsTal[tal] 
            array = []

            def modulesRest(i): 
                length = len(str(i))
                #Nået til bunden af "Recursion" træet
                if length == 1:
                    array.append(i)
                    return 
                #Gå til næste græn i træet.
                else: 
                    array.append(int(i % 10)) 
                    n = int(i / 10)
                    modulesRest(n)
                    return
            
            
            def addNumbers(array):  
                newValue = 0
                for number in array:
                    newValue += number
                return newValue

            modulesRest(number)
            dict.append(addNumbers(array))
            if fib: 
                self.tværSumsTal = dict 
            else: 
                self.tværSumsTotal = dict

    def printVærdier(self): 
        print("\n\n\n")
        tab = "\t"
        printFormat = "Count," + tab + tab + "Fibonacci," + tab + "Tværsum," + tab + "Tværsums total "
        
        fib = self.fibonacciTal
        tværSum = self.tværSumsTal
        tværSumsTotal = self.tværSumsTotal
        count = min(len(fib), len(tværSum))
        print(printFormat)
        
        for i in range(0,count):
            text = f"{str(i) + tab + tab + str(fib[i]) + tab + tab + str(tværSum[i]) + tab + tab + str(tværSumsTotal[i])} "
            print(text)

        print("\n\nTadaaaa")
        print("Aflevering lavet af: Jesper Bertelsen")

aflevering2 = aflevering()
aflevering2.printVærdier()
