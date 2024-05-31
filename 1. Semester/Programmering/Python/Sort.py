import random as rand

# -- Generel sort -- # 
class Sort: 
    def getSorted(self, liste: list[any]) -> list[any]: 
        print("Sorts list")
        return []
    def findMin(self,liste: list[any]): 
        print("Finder min")
        return 0







# -- Selection sort -- # 
class SelectionSort(Sort): 
    
    def getSorted(self,liste: list[any]) -> list[any]:      
        tom = []
        for i in range(len(tom),len(liste)):
            min = self.findMin(liste)
            tom.append(min)
            liste.remove(min)
        return tom
        
    def findMin(self, liste: list[any]): 
        min: int = None
        for x in liste: 
            if min is None: 
                min = x
                continue
            if x < min: 
                min = x
        return min



# -- BubbleSort -- #
class BubbleSort(Sort): 
    def getSorted(self, liste: list[any]) -> list[any]:
        x: int = None
        y: int = None
        maxIndex: int = None
        
        for _ in range(0,len(liste)):
            if maxIndex is None: 
                maxIndex = len(liste)-1
            maxIndex = self.bytVærdier(liste, maxIndex)
        return liste

    def bytVærdier(self, liste: list[any], endIndex) -> int: 
        størsteVærdi: int = None
        for i in range(0,endIndex): 
            if størsteVærdi is None: 
                størsteVærdi = liste[i+1]
            x = liste[i] 
            y = liste[i+1]
            if self.findMin(x, y): 
                (liste[i], liste[i+1]) = (liste[i+1], liste[i])
            if y > størsteVærdi: størsteVærdi = y 


    def findMin(self, x: int, y: int) -> bool:
       return y < x

import cProfile 
antal = 1000
liste = []  
for _ in range(0, antal): 
    liste.append(rand.randint(0,100))

sort = SelectionSort()
cProfile.run('sort.getSorted(liste[:]) ')

sort = BubbleSort()
cProfile.run('sort.getSorted(liste[:])')