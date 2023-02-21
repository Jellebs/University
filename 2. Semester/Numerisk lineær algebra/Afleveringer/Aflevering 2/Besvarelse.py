# Besvarelse til opgave 2. 
# Af Jesper Bertelsen: AU-ID: au689481

import numpy as np 
import matplotlib.pyplot as plt


# Opgave beskrivelse: 
# Et signal af formen: y(x) = 8cos(x) - 3sin(7x),    0 ≤ x ≤ 9
# Formindsk støjen.

# a. Lav et plot af funktionen 
n = 100 # Antallet af punkter
x = np.linspace(0, 9, n) # 100 punkter mellem 0 & 9.
y = 8*np.cos(x) - 3*np.sin(7*x) 

fig, ax = plt.subplots()
ax.set_aspect = "equal"
ax.plot(x,y)
#fig.savefig("Signalet fra start.pdf")

# b. Tilføj støj
rng = np.random.default_rng()
støj = rng.standard_normal(n)

y = y + støj
#ax.plot(x,y) # Plot med støj. 
#fig.savefig("Signalet med & uden støj.pdf")

# c. Kréer A matrice med diagonal form, vist i opgaven.

offset = 1
v = np.ones(n, dtype=float) # 100 elementer, til midten.
v_1 = np.ones(n-1, dtype=float) # 99 elementer, til siden.

# diagonal matrice
vægtning = 1./3. 
A = np.diag(v_1*vægtning, offset) + np.diag(v_1*vægtning, -offset) + np.diag(v*vægtning, 0)

# d. Plot Ay_støj. Det burde ses at den har en form, som er tættere på y end på y_støj. Forklar hvorfor

ax.plot(x, A @ y)
#fig.savefig("Plot med Ay_støj.pdf")

def lavDiag(række_søjle_antal, offsetMax: int): 
    diag = None 
    vægtning = float(offsetMax + offsetMax+1)
    for i in range(0, offsetMax+1):
        if i == 0: 
            diag = np.diag(np.ones(række_søjle_antal - i, dtype= float) / vægtning, i)
            continue
        v = np.ones(række_søjle_antal - i, dtype= float)
        diag += np.diag(v/vægtning, i)
        diag += np.diag(v/vægtning, -i)

    return diag 

def plotDiag(matrix):
    ax.plot(x, matrix @ y)

B = lavDiag(100, 2) # 5 diagonaler
C = lavDiag(100, 3) # 7 diagonaler

plotDiag(B)
plotDiag(C)

fig.savefig("Formindsk støjen.pdf")