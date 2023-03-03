import numpy as np 
import matplotlib.pyplot as plt
a = np.array([
    [2, 2, 4, 1, 3, 7, 12, 3],
    [3, 3, 3, 1, 9, 2, 2, 9], 
    [1, 1, 4, 2, 5, 12, 3, 7],
    [2, 2, 4, 1, 3, 7, 12, 3],
    [3, 3, 3, 1, 9, 2, 2, 9],
    [2, 2, 4, 1, 3, 7, 12, 3]]) # Vilkårlig numpy array med to akser.

# Opgave 5.1. Forklar hvad følgende operationer gør ved a: 

def opgave_5_1(): 
    
    a[2, [1,3,4,6]] = 1 # a. Hypotesen var, at dette ville gøre alle disse indekser i række 2 til 1, hvilket den også gør.
    a[:, [3,1]] = a[:, [1,3]] # c. Bytter søjle 3 og 1 ud med at være søjle 1 og 3, i de skrevne rækkefølger. Hvilket den gør
    a[2:5, 0]  = np.array([0, 1, 2]) # d. Ændre første søjle, række 2,3,4 til værdierne 0, 1, 2 
    a[4, 3:8:2] += 6 # e. Række 4. Hver anden værdi op til 8, får lagt 6 til. "min":"max":"increment by"
    a[np.ix_([1,2], [4,6])] = np.array([[0, 1], [2, 3]]) # f. Tager række index 1 og ændre søjle indeksne 4 & 6 til at være 0 og 1. 
    # Næste række index i de samme søjleindex bliver værdierne 2, 3. 
    # Index(ix_()), række 1 & 2, søjle 4 & 6 = nye værdier


def opgave_5_2():
    # Beregn den inverse til A
    A = np.array(
        [[1, 2, 2], 
         [2, 1, -1], 
         [-1, 2, 1]], dtype= float)
    
    # Identites matricen implementeres.
    A = np.array(
        [[1, 2, 2,    1, 0, 0], 
         [2, 1, -1,   0, 1, 0], 
         [-1, 2, 1,   0, 0, 1]], dtype= float)
    
    A[0, :] -= 1 * A[2, :] # R_0 - R_2 
    A[1, :] -= 1 * A[0, :] # R_1 - R_0
    A[2, :] *= 2 # R_2 *2 
    A[2, :] += A[0, :] #R_2 += R_0 
    A[2, :] -= 4 * A[1, :]
    A[0, :] *= 1/2
    A[2, :] *= 1/11
    A[1, :] += 2* A[2, : ]
    A[0, :] -= 1/2 * A[2, :]

    # Resultat 
    # [[ 1.          0.          0.          0.27272727  0.18181818 -0.36363636]
    # [ 0.          1.          0.         -0.09090909  0.27272727  0.45454545]
    # [ 0.          0.          1.          0.45454545 -0.36363636 -0.27272727]]

    # Bonus opgave er at tælle flops, men det er simpelthen slave arbejde. Hvis dette ønskes, så må man selv gøre det. 
    # Operationerne bliver taget på rækker som fungerer som vektorer, så her kan man se på vektor sum / skalar multiplikation på vektorer. 

    print(A)



opgave_5_2()

def opgave_5_3(): 
    # a. Hvor mange pivotelementer er der i echelonformen for A.
    u = np.array([1,-1,2])[:, np.newaxis]; v = np.array([1,2,-1,-2])
    A = u*v
    print(A)
    # Da vi ikke har en værdi for resultatet af A, vil der ikke laves rækkeoperationer på den. 
    # Antal pivotelementer = 1
    #   [[ 1  2 -1 -2]
    #   [-1 -2  1  2]
    #   [ 2  4 -2 -4]]

    # b. For u in reeel**m og v in reel**n, hvor mange pivotelementer kan der være i echelonformen for B?
    B = u*v
    # Antallet af rækker er bestemmende. 
    # u indeholder m rækker. Der kan være m pivotelementer. 

    # c. 
    w = np.array([1,1,1])[:, np.newaxis]
    x = np.array([1,0,0,0])
    C = u*v + w*x
    print(C)
    # Samme som sidste opgave, så kan det maksimale antal pivotelementer være antallet af rækker, som er 3. 

v0 = np.array([2,1,-2])[:, np.newaxis]
v1 = np.array([1,0,1])[:, np.newaxis] 
v2 = np.array([1,-4,-1])[:, np.newaxis]
vektorer = [v0, v1, v2]
x = []
w = np.array([4,5,6])
w_parseval: float = None

def opgave_5_4(): 
    # a. 
    print(np.vdot(v0, v1) + np.vdot(v0, v2) + np.vdot(v1, v2)) # = 0 derfor en ortogonal samling
    
    # b. 
    # Formel 8.9 også fundet i formelsamlingen, selv lavet.
    for vektor in [v0, v1, v2]: 
        x.append(np.vdot(w, vektor) / np.vdot(vektor, vektor)) # <u,v_k> / ||v_k||_2**2
    print(v0*x[0] + v1*x[1] + v2*x[2]) # = [4, 5, 6], hvilket er w. 

    def beregnParsevalsIdentitet(skalar, vektor): 
        x_værdi = skalar ** 2 
        vektor_værdi = np.vdot(vektor, vektor)
        return x_værdi*vektor_værdi

    for i in range(len([v0, v1, v2])):
         if i == 0: 
            w_parseval = beregnParsevalsIdentitet(x[i], vektorer[i])   
            continue
         w_parseval += beregnParsevalsIdentitet(x[i], vektorer[i])   
    
    print(w_parseval) # == 77.0, hvilket sagtens kan være. 
    print(np.vdot(w, w)) # == 77, så dette må passe. 


Punkter = np.array([ # Der skal korrigeres så u vides ud fra origo. 
    [0, 0],
    [1, -3],
    [4, -3], 
    [5, 0]]) 

def opgave_5_5(): # Betragt vektoren og bestem den korteste afstand fra hvert linjestykke til punktet. 
    # Der skal korrigeres
    def projektionSkalar(u, v):                 # Også skrevet som formel i formelsamlingen under ortogonalitet og projektion.
        return np.vdot(u, v) / np.vdot(v, v)    # <u, v> / ||v||_2**2 
    
    def lavVektorer(): 
        v = None
        for i in range(1, len(Punkter)): 
            x_komponent = Punkter[i, 0] - Punkter[i-1, 0]
            y_komponent = Punkter[i, 1] - Punkter[i-1, 1]
            if i == 1: 
                v = np.array([[x_komponent, y_komponent]])
                continue
            v = np.append(v, [[x_komponent, y_komponent]], axis = 0) # Axis laver det til en række for sig.
        return v
    fig, ax = plt.subplots()
    def findAfstande(): 
        afstande = None
        for i in range(0, len(vektorer)): # 3 vektorer, 0, 1, 2 
            projektion = projektionSkalar(u, vektorer[i])*vektorer[i]
            afstand = np.sqrt(np.vdot(u, u) - np.vdot(projektion, projektion)) # Afstand far linje til punkt: √(||u||_2**2 - ||pr_v(u)||_2**2)
            print(i, afstand, projektion)
            if i == 0: 
                afstande = np.array([[afstand]])
                continue
            afstande = np.append(afstande, [[afstand]], axis = 0) 
            
        return afstande
    vektorer = lavVektorer()
    u = np.array([2, -1])
    afstande = findAfstande() 
    
    for i in range(len(vektorer)):
        ax.plot(vektorer[i, 0], vektorer[i, 1], color ="Red")  
        # Det her er blot til fejlfinding... Men python har givet op på projektet, så nu kan den kysse min rumpe.

    ax.plot(u[0], u[1], marker="o", markersize= 20) 
    # Der er noget galt her. 
    # Det antages, at det har noget med den måde, som jeg beregner afstanden fra. 
    # Jeg trækker afstanden fra første punkt til origo fra alle punkter.
    # Måske skulle man tage afstanden fra hvert punkt til origo, og flytte både punkt og u med det. 
    # Jeg har løst opgaven på sin vis, jeg har benyttet de rigtige metoder, men jeg har fundet et andet resultat, end hvad de søgte.   
    
opgave_5_5()



