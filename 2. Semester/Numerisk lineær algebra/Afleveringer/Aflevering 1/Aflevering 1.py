# Dokumentet startes med importsne
import numpy as np
import matplotlib.pyplot as plt

#                                               Opgavebeskrivelse: 

# En robotarm består af 4 stænger OA, AB, BC og CP samlet i planen således at armen kan bøjes ved ledderne O,A,B og C.
# Lad a= vector(O->A), b = vector(A -> B), c = vector(B -> C) og d = vector(c -> d). Robotarmens stilling er bestemt af matricen

#                                               S = [ a | b | c | d]

# a. Vælg nogle rimelige værdier for indgangerne i a, b, c og ⁡d, og brug derefter matplotlib til at lave en tegningen af robotarmen som ovenfor.
O = np.array([0,0])
A = np.array([2,5])
B = np.array([2.5, 5.5])
C = np.array([3, 4])
P = np.array([2.75, 3.75])

a = A - O 
b = B - A
c = C - B
d = P - C 

#En funktion til at plotte vektorerne ud fra en startposition: 
def lavArm(vectors: list[list[float]], startkoordinat: list[float]): # Indsæt vektorer med 2 søjler, 1 med x den anden med y.
    i = 0
    x = [startkoordinat[0]]
    y = [startkoordinat[1]]
    for vector in vectors: # Hver vektorer er en 1x2 vektorer, og består af søjle 1 = x, søjle 2 = y.
        x.append(vector[0] + x[i]) # Tilføjer koordinat ud fra vector og dens startpunkt.
        y.append(vector[1] + y[i])
        i = i + 1 
    ax.plot(x,y)
    #fig.savefig("Bøj om A.pdf")

vectors = np.array([a, b, c, d])
fig, ax = plt.subplots()

lavArm(vectors, O) # listen af vektorer med start i origo.



# b. Bestem vektoren vector(OP) ud fra a, b, c, d

e_vec = np.array([P - O]) # Hvor O blot er koordinat men erstatter en vektorer, da noget - origo(0,0) = noget. 
lavArm(e_vec, O)
# fig.savefig("Robotarm med vektor OP.pdf") billede gemt til senere.



# c. Gør rede for at når armen bøjes i ledet C, svarer det til at anvende en rotationsmatrix R_C på d, dvs.
#                               bøjC(S) = [a | b | c | R_(C)d]
# Lav en matplotlibtegning der viser dette. 

# Funktion, som indsætter vinklen i formlen for rotation i 2D.
def rotation(vinkel: int): 
    return np.array([[np.cos(vinkel), -np.sin(vinkel)], 
                    [np.sin(vinkel),  np.cos(vinkel)]])

# Jeg lader rotationsvinklen være 60°
d_rot = rotation(60) @ d 
R_C_d = np.array([rotation(60) @ d])

lavArm(R_C_d, C) 
# Grunden til at vi bare kan ændre vektoren og forsætte fra de andre vektorers startposition er,
# at vektorerne er uafhængig af dens position. En ændring i vektoren ændre dermed ikke dens startposition.



# d. Giv en opskrift for bøjA(S), hvor robotarmen bøjes kun i ledet A. Vis dette i en tegning

# Den metode som er min opskrift er, først at rotere den vektor som bliver påvirket af rotationen om ledet.
# b vektoren bliver påvirket af et bøj om A ledet.

b_rot = rotation(-20) @ b

# Så laves rækkefølgen af vektorer.
vectors = np.array([a,b_rot, c, d])

# Og så ind i min funktion til placering af vektorer.

lavArm(vectors, O)
#fig.savefig("Bøj om A.pdf")


# e. Vis generelt at 
#               bøjA(bøjC(S)) = bøjC(bøjA(S))
#    dvs. det har ingen betydning for slutstilligen hvilket led vi bøjer først.

# Vi har allerede alt vi skal bruge. 

# Rotationen om C har vi set på, at det kun ændre den sidste vektor. 

#fig.savefig("Bøj om C & bøj om A.pdf")

# Vektorernes størrelse og værdier er uafhængige af dens placering.
# Vektoren bliver placeret ud i en position. 
# Ved at bøje A først, ændre vi den sidste vektores startplacering.
# Ved at bøje C først, ændre vi slutvektoren. Ved at bøje A sidst ændre vi placeringerne til sidst.

# Om man bøjer om C først, og derefter A, ses med min funktion som det samme som hvis jeg gør det omvendt.
# Med min metode er rækkefølgen i bøj ligegyldigt. Jeg tager en liste med vektorer og bruger de tidligere vektorer til at bestemme startpunkt.
# Jeg ved ikke, om jeg kunne have vist det på en mere matematisk måde, så jeg bedre ville kunne vise det.

vectors = np.array([a,b_rot, c, d_rot])
lavArm(vectors, O)
# Her til sidst bliver den røde arm, som er bøjet om A, overlappet af bøjet om A og dernæst bøj om C. Den eneste ændring er d vektoren til sidst.

#fig.savefig("Alle opgaver lavet.pdf") 
