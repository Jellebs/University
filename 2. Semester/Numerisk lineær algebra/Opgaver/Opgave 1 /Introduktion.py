import numpy as np
import matplotlib as mpl 


ANTALCIFRE = 1 
divider = " "+"-"*23
###         Opgave 1 med distance til universitet          ###         
distance = 3.1 #km
distance_min = 3.05
distance_max = 3.15
hastighed = 5.8 #km/t
hastighed_min = 5.75
hastighed_max = 5.85 

def printOpgaveTo():
    tidBrugt = (distance / hastighed * 60).__round__(ANTALCIFRE)
    tidBrugt_min = (distance_min / hastighed_min * 60).__round__(ANTALCIFRE)
    tidBrugt_max = (distance_max / hastighed_max * 60).__round__(ANTALCIFRE)
    def printTekst(string: str):
        print(divider)
        print(string)

    printTekst("| Beregning: " + str(tidBrugt) + "\t|")
    printTekst("| Min: " + str(tidBrugt_min) + "\t"*2 + "|")
    printTekst("| Max: " + str(tidBrugt_max) + "\t"*2 + "|")
    print(divider)

###              Opgave 2 med AAA batterier                ###

modstand = 20 # Ohm +- 5% 

usikkerhed_Spænding = 0.05
usikkerhed_Resistor = modstand * 0.05 

spænding = 1.5 # Volt 
spænding_min = spænding - usikkerhed_Spænding
spænding_max = spænding + usikkerhed_Spænding

modstand_min = modstand - usikkerhed_Resistor 
modstand_max = modstand + usikkerhed_Resistor 

def printOpgaveTre():
    divider = " "+"-"*31
    def lF(værdi: float) -> float: # Lav float
        return værdi.__round__(5)

    strøm = lF(spænding / modstand) 
    strøm_min = lF(spænding_min / modstand_min)
    strøm_max = lF(spænding_max / modstand_max)

    effekt = lF(spænding * strøm)
    effekt_min = lF(spænding_min * strøm_min)
    effekt_max = lF(spænding_max * strøm_max) 

    def printTekst(string: str):
        print(divider)
        print(string)
        
    printTekst("| Strøm beregning: " + str(strøm) + "\t|")
    printTekst("| Strøm min: " + str(strøm_min) + "\t"*2 + "|")
    printTekst("| Strøm max: " + str(strøm_max) + "\t"*2 + "|")
    print(divider)
    print("\n")
    printTekst("| Effekt beregning: " + str(effekt) + "\t|")
    printTekst("| Effekt min: " + str(effekt_min) + "\t"*2 + "|")
    printTekst("| Effekt max: " + str(effekt_max) + "\t"*2 + "|")
    print(divider)


def printOpgaveFire(): 
    # 1.2, 2, 1.555 er en løsning til første del
    a = 1.2
    b = 2
    c = 1.5573261111
    
    def printEksempel(): 
        print(a * (b+c))
        print(a*b + a*c )
        print("\n")
        print(a*(b/c))
        print(a * b / c )
    print("Løsning er fundet til 2 eksempler, hvor den resultaterne er forskellige fra hinanden.")
    printEksempel()

printOpgaveFire()
