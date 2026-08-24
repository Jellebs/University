import numpy as np
import matplotlib.pyplot as plt

interval = [0, 1] # +1 
# Opgave 2.1. Brug python til at beregne længde og vinkel for de følgende vektorer i planen:

a = np.array([0.0, 1.0]) 
b = np.array([1.0, -1.0])
c = np.array([-0.5, -0.8660254037844386])

# Længde af vektorerne er bestem ved vektorens x y kvadreret lagt sammen, og taget deres kvadratrod. 
# Hvad jeg leder efter er normen, og funktionen jeg finder denne med er linalg.norm. Det er bare pythagoras der bliver taget for hver vektorer. 
arr = [a,b,c] # Liste lavet til bekvem

print("\n"* 4) # Skub rodet væk.

def len_vektorer():
    len = 0.0
    for værdi in arr: 
        len = len + np.linalg.norm(værdi)
    return len

def cos_vinkel(): # returnerer cos(vinkel)
    cos_theta = 0.0 
    for vektor in arr: 
        cos_theta = cos_theta + vektor[0] / np.linalg.norm(vektor) # x / √ ( x^2 + y^2 )
    return cos_theta 


def besvarelse_et():
    print("Længde af vektorer: " + str(len_vektorer()))
    print("Cos til vinklen: " + str(cos_vinkel()))
    theta = np.arccos(0.2) # Radianer
    print("Vinklen i radianer: " + str(theta))
    print("Vinklen i pi: " + str(theta / np.pi) + " * pi")  # 1.369 / 3.14.... 43/100 pi ca. 
    print("Vinklen i grader: " + str(np.degrees(theta))) # Radianer som standard. 

def besvarelse_to(): 
    # Denne opgave tager udgangspunkt i funktionen y = (2sin(x)/(1+x^2))

    x = np.linspace(1, 7, 100) # Der laves 100 punkter mellem 1 & 7
    y = 2 * np.sin(x) / (1 + x**2 )

    # Plotting 
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.plot(x,y)
    plt.show()
    # Done

def besvarelse_tre():
    # Til denne opgave er der følgende funktioner: 
    # y = x**8 - 8*x**7 + 28*x**6 - 56*x**5 + 70*x**4 - 56*x**3 + 28*x**2 - 8*x + 1 
    # & z = (x - 1)**8 
    # Der fåes at vide at de rent matematisk er ens. Nu skal der findes ud af, hvilken der er bedst i python.
    # Med de samme x værdier fra opgave to skal vi plotte fejlende for y i forhold til z. 
    
    # Formlen for fejl findes ved 
    # x' - x
    # y - z 
    x = np.linspace(1,7, 100)
    y = x**8 - 8*x**7 + 28*x**6 - 56*x**5 + 70*x**4 - 56*x**3 + 28*x**2 - 8*x + 1 
    z = (x - 1)**8

    fig, ax = plt.subplots()
    ax.set_ylim((-10**(-9)),10**(-8))
    ax.plot(x,(y - z)) # Fejl - Den stabile graf. Efter x = 5 begynder der at ske store udsving. Grafen svinger både over og under x aksen. Begge funktioner må have deres fordele og ulemper.
    # fig.savefig('Fejl y - z.pdf') # Plottet er gemt. 
    ax.plot(x,(y - z)/z) # Relative fejl - Den mere ustabile graf.
    # fig.savefig('Relativ fejl - Stor i begyndelsen.pdf') - Billede af det store hak i starten.
    # fig.savefig('Relativ fejl - Stabil efter x = 1.pdf') - Billede af tendensens efter det store hak. Det er helt nede i 10*-15 plan, at de relative fejl begynder at kunne ses.
    #fig.savefig('Fejl og relativ fejl.pdf')
    plt.show()  


# Tegning til næste besvarelse.

class Hus(): 
    __Hus = np.array(
        [
        [7, 0], # Fundament
        [0, 0], 
        [0, 5], 
        [3.5, 7], # Tag
        [7, 5],
        [7, 0]
        ]
    )
    __dør = np.array( 
        [
        [2.5, 0], 
        [2,5, 3],
        [4.5, 3], 
        [4.5, 0]
        ]
    )
    def lavFigur(self, withApplication: tuple(np.array(list))):
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        for punkt in self.__Hus: 
            ax.plot(punkt[0], punkt[1])
        
        for punkt in self.__dør: 
            ax.plot(punkt[0], punkt[1])
        
        fig.show()

    





#besvarelse_et()
#besvarelse_to()
#besvarelse_tre()

def besvarelse_fire(): 
    hus = Hus()
    hus.lavFigur(None)

    
besvarelse_fire() 