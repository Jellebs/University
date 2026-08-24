from sympy import * 
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
init_printing(use_latex=True)

# v_2(s) = Zc/(Zr+Zc)
C1, R1, V1, s= symbols("C1 R1 V1 s")

Zc = 1/(C1 * s)
Zr = R1
# Laplace kredsløb 
V2 = Zc/(Zr+Zc) * V1 

# 2. Vis at overføringsfunktionen kan skrives som TLP(s) = K/(s+alpha) hvor alpha = 1/(R1C1). Hvad bliver K? 
TLP = V2/V1 
pprint(TLP) # = alpha / (s + alpha)
alpha = 1/(C1*R1)
# K = 1

# 3. Lavpasfilteret ønskes implementeret til at give følgende overføringsfunktion: 
# Bestem R1

c1 = 100e-9
alpha = alpha.subs(C1, c1)
r1 = solve(alpha - 62832)
# ====================================
alpha = alpha.subs(R1, r1[0]) # 160Ohm
# ====================================
TLP = alpha/(s+alpha)
pprint(TLP)

# 4. Tegn et bodeplot for TLP(s), der inkluderer både amplitudekarakteristikken (i dB) og fasekarakteristikken (i grader), med en logaritmisk frekvensakse i området 1 KHz til 1 MHz.

f = np.logspace(2, 7, 100)
w = 2*np.pi*f
s = 1.0j * w 

p = 62832.0*2*np.pi
Gjw = 62832.0/(s + 62832.0)
db_mag = 20*np.log10(np.abs(Gjw))


def plot(y, ylabel): 
    fig, ax = plt.subplots()
    ax.semilogx(f, y)
    ax.set_ylabel(ylabel)
    fig.savefig(f"Frequency, {ylabel} graf.pdf")

#plot(db_mag, 'dB magnitude')
# print(db_mag[:50]) # -3db, ved index 35
# print(f[:50]) # index 35 = 10722.6722201

phase = np.degrees(np.arctan2(np.imag(Gjw), np.real(Gjw)*180/np.pi))
# == # 
# plot(phase, 'phase')
angle = np.angle(Gjw, deg= True)
# plot(angle, 'angle')

# 5. Hvad er tidskonstanten for kredsløbet. 
# Hvad er en tidskonstant. Efter 5*tidskonstanter, så opnår funktionen sit min eller maximums punkt. 

# Set med brillerne fra phase billedet af, så går den fra at være i bevægelse, til at være fladet ud i intervallet: 
# [10^3: 10^6]
# 5 tau = 10^6 - 10^3

tau = (1e6 - 1e3) / 5 
print(tau) # = 199800

