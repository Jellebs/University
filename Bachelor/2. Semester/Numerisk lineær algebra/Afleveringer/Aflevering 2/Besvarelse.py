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
ax.plot(x,y, label="y")
#fig.savefig("Signalet fra start.pdf")

# b. Tilføj støj
rng = np.random.default_rng()
støj = rng.standard_normal(n)

y = y + støj
#ax.plot(x,y, label="y_støj") # Plot med støj. 
#fig.savefig("Signalet med & uden støj.pdf")

# c. Kréer A matrice med diagonal form, vist i opgaven.

offset = 1
v = np.ones(n, dtype=float) # 100 elementer, til midten.
v_1 = np.ones(n-1, dtype=float) # 99 elementer, til siden.

# diagonal matrice
vægtning = 1./3. 
A = np.diag(v_1*vægtning, offset) + np.diag(v_1*vægtning, -offset) + np.diag(v*vægtning, 0)

# d. Plot Ay_støj. Det burde ses at den har en form, som er tættere på y end på y_støj. Forklar hvorfor

ax.plot(x, A @ y, label="Ay_støj")
fig.legend()
#fig.savefig("Plot med Ay_støj.pdf")


def lavDiag(række_søjle_antal, offsetMax: int, vægtning): 
    diag = None 
    for i in range(0, offsetMax+1):
        if i == 0: 
            diag = np.diag(np.ones(række_søjle_antal - i, dtype= float) * vægtning, i)
            continue
        v = np.ones(række_søjle_antal - i, dtype= float)
        diag += np.diag(v * vægtning, i)
        diag += np.diag(v * vægtning, -i)

    return diag 

def plotDiag(matrix, label):
    ax.plot(x, matrix @ y, label= label)


B = lavDiag(100, 2, 1/5) # 5 diagonaler
plotDiag(B, "x = 5 ")
fig.legend()
fig.savefig("Formindsk støjen.pdf")


# 1. Eftertjek.
# Ændring på antal diagonaler, med fastholdt vægtning, bliver værre for hvert diagonal der lægges til. 
# Ændringen medførte for diagonaler > 5 en forhøjet amplitude
# Interesant nok var amplituden mindre ved diagonaler = 5. 

# 2. Eftertjek
# Ændring i vægtning med fastholdt antal diagonaler, medførte et skift i amplitude.
# For 1/x, som er vægtningen, ville x < antal diagonaler medfører en højere amplitude en A
# For x > antal diagonaler medføre en mindre amplituden. 

# 3. Eftertjek. 
# x = antal diagonaler & 1/x = vægtningen. 
# Jo større x bliver, jo mere flader grafen sig ud. 
# Da 3 diagonaler er den mindste anden end 1, som giver identitetsmatricen, 
# Identitetsmatricen giver ingen støjreduktion. x = 3 må være den bedste værdi.
# A må da være den bedst mulige støjreduktionsløsning for x som heltal. 




