import numpy as np 
import matplotlib.pyplot as plt

# Opgave 3.1 Lad 
s = 2
t = 3, 
A = np.array([[2.0, 1.0, -1.0],
              [0.0, 2.0, 5.0]])
B = np.array([[1.0, -1.0, 0.0], 
              [0.0, 1.0, -1.0]])

# Hvilke af de følgende udtryk er tilladt? For dem, der er tilladt, beregn svaret. 
# For dem der ikke er tilladte, forklar hvorfor. 
# Jeg rangere ud fra hvilke der er er tilladte, og hvilke der ikke er. 

# Tilladte matrix operationer.
 
s*B # a. Blot en skalering af matrixen, den er altid gældende. 

A + t*B # b. Ved addition med matricer, skal matrixer have samme m rækker og samme n søjler.
        #   A har 3 rækker, 2 søjler. 
        #   B har 3 rækker, 2 søjler. 
        #   t er blot en skalering af vektoren. 
        #   Dette er en tilladt operation.

A.T # c. Alle matricer kan denne operation, men beregningerne bagefter er muligvis ikke gyldige.

s*A.T - t*B.T # e. Denne operation skulle være gyldig. To produkter som skaleres.
        #   Deres rækker og søjler byttes, man da dette gøres på begge produkter,
        #   er det muligt at lave substitution. 

A.T @ B # h. Her kommer vi til det som matrix multiplikationen kan, men som addition ikke kan.
        # Det er dette tilfælde, som vi manglede i punkt g.
        # Da dette er en søjle række multiplikation ser vi et ydre produkt,
        # hvor slut dimensionen er 3x3 altså større end hver af de to matricer.

s * A @ B.T # i. Denne operation skulle også være gyldig.
        # Her har vi et række søjle produkt. 
        # Hvor vi i punkt h havde et ydre produkt, har vi her et indre produkt.

B @ A.T @ B * t # j. 


# Ikke tilladte matrix operationer. 

# A.T + s*B #d. Regnereglen for matrixoperationer forklaret til punkt b, er ikke opfyldt her.
        #   A.T = 2 rækker, 3 søjler. 
        #   s*B = 3 rækkker, 2 søjler. 

# A @ B     # f. Skulle ikke være muligt. 
    # For matrix_1 af m X n, kræves det at matrix 2 er af j X m, hvor n & j er vilkårlige tal. 
# B @ A     # g. Igen samme problem 
        # B & A har samme matrix form, så rækkefølgen er ligegyldig.
        # De kan bare ikke multiplikeres.




# Opgave 3.2. Lad R_0 og R_1 være rotationmatricerne fra eksempel 4.8 i Notesæt 4, 
# taget med c = 0.8, 0.6. Beregn matrixprodukterne

#                           R_0 * R_1  & R_1 * R_0
# og bekræft at resulaterne er forskellige. Hvad betyder dette for en opgraderet version af robotarmen
# fra Afleveringsopave 1, hvor ledende kan bøje sig i tre dimensioner? 

R_0 = np.array([
    [1.0, 0.0, 0.0],
    [0.0, 0.8, -0.6], 
    [0.0, 0.6, 0.8]])
R_1 = np.array([
    [0.8, 0.0, -0.6],
    [0.0, 1.0, 0.0], 
    [0.6, 0.6, 0.8]])

print(R_0 @ R_1)
print(R_1 @ R_0)
# Der ses to forskellige matricer. 
# Hvad det betyder for robotarmen, hvis den blev opgraderet til 3D, vides ikke.



# Opgave 3.3 Computernetværker. 


# Opgave 3.4 Landsflag

# Danmark ålæ
v = np.array([1.0, 1.0, 0.0, 1.0, 1.0])[:, np.newaxis] 
wt = np.array([[1.0, 1.0, 0.0, 1.0, 1.0, 1.0]])

fig, ax = plt.subplots()
ax.matshow(v @ wt, cmap='Reds', clim=(0.0,1.2))

# Ud fra søjle vektoren 

#       [ 1 ]
#       [ 1 ]
#  v =  [ 0 ] ,  w = [1, 1, 0, 1, 1, 1 ]
#       [ 1 ]
#       [ 1 ]

# Ganges hvert af v's rækker med w's rækker

# [1*1, 1*1, 1*0, 1*1, 1*1, 1*1]
# [1*1, 1*1, 1*0, 1*1, 1*1, 1*1]

# Indtil at det er v's række der er nul.
# [0*1, 0*1, 0*0, 0*1, 0*1, 0*1]

# Som danner den horizontale hvide stribe i denne farvemode. 

# Fuldændt ser det ydre produkt sådan ud: 
# 1   1   0   1   1   1
# 1   1   0   1   1   1
# 0   0   0   0   0   0 
# 1   1   0   1   1   1
# 1   1   0   1   1   1 


# Find tilsvarende ydreprodukter og valg af cmap og clim, som giver følgende flag:

# a. Østrig.

v = np.array([1.0, 1.0, 0.0, 0.0, 1.0, 1.0])[:, np.newaxis] 
wt = np.array([[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]])
ax.matshow(v @ wt, cmap = "Reds", clim=(0.0, 1.2))


# b. England. 
v = np.array([1.0, 1.0, 0.0, 1.0, 1.0])[:, np.newaxis] 
wt = np.array([[1.0, 1.0, 0.0, 1.0, 1.0, 1.0]])

# 0   0   1   0   0 
# 0   0   1   0   0 
# 1   1   1   1   1 
# 0   0   1   0   0 
# 0   0   1   0   0

v = np.array([0.0, 0.0, 1.0, 0.0, 0.0])[:, np.newaxis]
wt = np.array([1.0, 1.0, 1.0, 1.0, 1.0])
b = np.array([0.0, 0.0, 1.0, 0.0, 0.0])
w = np.array([1.0, 1.0, 1.0, 1.0, 1.0])[:, np.newaxis]
# opskrift
# Tanken er v som den ene vektor ganget med en række af 1'ttere. 
# En anden vektor regnes på næsten samme måde for at danne den horizontale række.

ax.matshow(v @ wt + w @ b, cmap='Reds', clim=(0.0, 1.2))
