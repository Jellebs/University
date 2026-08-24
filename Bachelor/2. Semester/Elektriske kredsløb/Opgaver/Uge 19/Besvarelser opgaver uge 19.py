from sympy import * 
from Formelsamling.Elektriske_Kredsløb import * 
import matplotlib.pyplot as plt
import numpy as np

# Opgave 12.31
# Design an RLC bandpass filter with a center frequency of 1000 rad/s and a Q of 20. 
# The passband gain is +20 dB. Use practical values for R, L, and C 

# filter_omega0()
# filter_qualityFactor()

# Nu har vi en ligning for nogle ubekendte 
# 1000 rad/s = 1/√(LC)
# B = R / L
# Q = omega0/B = √(L/C)/R = 20
# Q = omega0/(R/L) = 20



L, C, R, s = symbols("L C R s")
eq = 1/sqrt(L*C) - 1000*1/s
eq1 = (1000*1/s)/(R/L) - 20

# En "Typisk" værdi for R er 10kOhm
# => 200H & 5nF
# 200 H er alt for højt og af en hurtig google søgning, så virker det ikke praktisk. 
# Lad os prøve med 100Ohm
eq1 = eq1.subs(R, 100)
# pprint(solve([eq, eq1])[0]) # 2 H & (1/2M)F = 0,5uF
# Hvilket virker mere virkeligt. 

svar = """
R = 100Ohm
L = 2H 
C = 0,5uF 

"""
opgaveBesvarelse("Opgave 12.31", svar)




# Opgave 12.33 
# A parallel RLC bandpass circuit with C = 0.01uF and Q = 10 has a center frequency of 500 krad/s.
# Find R, L, and the two cutoff frequencies. 
# Could you design this circuit using a cascade connection of two first-order filters separated by a follower? Why or why not?

# Parallel RLC => 1/R, L, C
C = 0.01e3

filter_omega0()
filter_qualityFactor()

eq = 1/sqrt(L*C) - 500e3 # Omskrivning af omega0 # Solve kan ikke løses med den her beregning, lad os omskrive den: 
eq = sqrt(L*C)/(L*C) - 500e3 
eq = L * C / ((L*C)**2) - 500e3
pprint(cancel(eq))

eq1 = sqrt(L/C)/R - 10 # Omskrivning af Q

pprint(solve([eq, eq1], dict=True)) # L = 0,2uH, R = 14uOhm

# 14 uOhm virker meget småt, jeg har kun prøvet at have med miliOhm at gøre. 



# Opgave 12-46 - For the following transfer function: 

#   T(s) = 100(s + 10)/(s(s + 100))

# a. construct the straight-line Bode plot of the gain. Is this a low_pass, high pass, bandpass or bandstop function? 
#    Estimate the cutoff frequency and passband gain. 

# Transfer funktionen har 2 poler, når s = 0 & s = 100, og et nulpunkt, når s = 10
# Poler får grafen til at falde med 20db/decade. Nulpunkter får grafen til at vokse med 20db/decade. 

# Så fald [0:10], udlignet [10:100], fald [100: ∞[ 
# Dette giver fald, vandret, fald. 
# Så Lowpass til konstant til lowpass? 

# Der er en måde at regne det ud på, lad os plotte grafen. 

f = np.logspace(0, 2, 100)
w = 2*np.pi*f # Vinkelfrekvens til Hz 
s = 1.0j * w # s -> jw 

Gjw = 100 * (s + 10 ) / (s**2 + 100*s + 0)
db_mag = 20*np.log10(np.abs(Gjw)) # db(magnitude) funktion.
phase = np.angle(Gjw, deg= True)

def plot(y, ylabel, f = f, save = False): 
    fig, ax = plt.subplots()
    ax.semilogx(f, y)
    ax.set_ylabel(ylabel)
    if save == True: fig.savefig(f"Frequency, {ylabel} graf.pdf")

plot(db_mag, 'dB magnitude')
plot(phase, 'phase')

# som spået går den fra en lowpass til konstant til lowpass

# Design a circuit using practical values for the components that has the same transfer function. 
# This filter contains 2 lowpass filters and 1 highpass filter. 
# Cascading these will have the order: 
# Low pass - High Pass - Low pass
#   T(s) = (100s + 1000) / (s^2 + 100s)
#   T(s) = (s + 10) / (s^2/100 + s)
#   T(s) = (s + 10) / (s/100)(s + 10000) 

# Low pass filter first order: K / (s + alpha)
# High pass filter first order: Ks / (s + alpha)

# k1/(s + alpha1) * (k2s2 /(s + alpha2)) * (k3 / (s + alpha3))
# (k1*k2s*k3) / ((s^2 + salpha2 + salpha1+alpha1alpha2)* (s + alpha3))
# (k1k2k3s) / ((s^2 + sa2 + sa1+a1a2)* (s + alpha3)) =  T(s) = (100s + 1000) / (s^2 + 100s)

# Transfer functionen ligner en bandpass, den har en pol af anden ordenen, men med 2 lowpass og 1 high pass, så for jeg en 3 ordens pol.
# Jeg springer den her opgave over 




# Opgave 12-48
# For the following transfer function

# T(s) = (100s(s - 300))/((s+30)(s+3000))

# a. Construct the straight line Bode plot of the gain. Is this a low-pass, high-pass, bandpass, or bandstop function?
# Estimate the cutoff frequency and passband gain. 

# Nulpunkt ses ved s = 0, & 300
# Pol ses ved s = 30, 3000
s = Symbol('s')
nulpunkter = solve(100*s*(s - 300)) 
poler = solve((s+30)*(s+3000))
print(nulpunkter)
print(poler) 
# Holder tjek
# T(s) = (100(s^2 - 300s))/((s+30)(s+3000))
# Gain, K = 100

s = 1.0j * w # s -> jw 

Gjw = (100*(s**2 - 300*s))/((s+30)*(s+3000))
db_mag = 20*np.log10(np.abs(Gjw)) # db(magnitude) funktion.
phase = np.angle(Gjw, deg= True)

plot(db_mag, "Graf i dB")


# (100s - 30000s) / (s^2 + s * 3000 + 30*s + 30*3000)
# (100s - 30000s) / (s^2 + s(3000 + 30) + 90000)
# (100s - 30000s) / (s^2 + s(3000 + 30) + 90000)
# (-29900) / (s + 3000 + 30 + 90000/s)





# Opgave 12-53 Considre the gain plot in Figure P12-53. 
# a. Find the transfer function corresponding to the straight-line gain plot

# Start i 5. + 5. 
# Nulpunkt i 5 
# Pol i 50 & 250
# Gain, K = 10
# Gain ved 50 & 250 
# Gainet er -10 ved w = ]0:5] & igen ved w = 2500






# !!!! Hvad der er vigtigt at tage med fra estimationerne !!!!
# Generel form for bandpass gain: 
# Tjw = T1 x T2 = K1*jw/(jw+a1) * K2/(jw+a2)
# |Tjw| = K1w/√(w^2 + a1^2) * K2/√(w^2 + a2^2)

# Lave frekvenser: 
#   w << a1 << a2 = w << 50 << 250
#  |Tjw| = K1w/a1 * k2w/a2
 
# For middelfrekvenser: 
#   a1 << w << a2
#  |Tjw| = K1K2/a2

# For høje frekvenser: 
#   w >> a2 >> a1 = w >> 250 >> 50
#  |Tjw| = K1w/w * K2/w = K1K2/w 

# formel for gain med dB
# Tjwdb = 20*log10(|Tjw|)
# |Tjw| = 10^(Tjwdb/20)



# Ligning1: K1K2/250 = |Tjw| => K1K2/250 = 10^(10/20) # Ved middelfrekvenser
# Ligning2: K1k2w/(12500) = |Tjw| => K1k2*5/(12500) = 10^(-10/20) # For w = 5
K1, K2 = symbols("K1 K2")
eq1 = K1*K2/250 - 10**(0.5) # = 0
eq2 = (K1*K2*5)/12500 - 10**(-1/2) # = 0 
# print(solve([eq1, eq2]))
# K1 = 790.56/K2
# Hvis K2 er 1, så er K1 790.56, som vil være det samlede gain. 

T = 790.56*(s + 5)/((s + 50) * (s + 250))
# Transfer funktionerne er estimeret og rammer derfor ikke eksakt, men ud fra facit er det her rigtigt. 

db_mag = 20*np.log10(np.abs(T))
f = np.logspace(0, 4, 100)
plot(db_mag, "Estimeret transfer function i dB", f)

# Compare the straight-line gain and the actual gain at w = 100 & 500rad/s

def TdB(frekvens): 
    s = 1.0j * frekvens
    T = 790.56*(s + 5)/((s + 50) * (s + 250))
    return 20*np.log10(np.abs(T))


svar = f"""
Sammenligning af SL, straight-line diagrammet og TdB, transfer funktionen i dB.
SL(100) = 10
Tdb(100) = {TdB(100)}
SL(500) = 8ish 
TdB(500) = {TdB(500)}

En del afvigelser, da gainet i virkeligheden ikke skifter hældning ved et bestemt punkt, men gradvist skifter hældning.
"""
opgaveBesvarelse("Opgave 12.53.c", svar)

# d. Design a circuit that will realize the transfer function found in part (a)
# Dette er et båndpass som består af et high pass filter i serie med et lowpass i den nævnte rækkefølge. 

# Solution side 628 følges. 
# Bandpass gain, K er = |K1K2|/a2 = 790.56 / 250 = 3.16224
T = s/(s + 50) * 3.16224 * 250/(s + 250)
#   High pass    Gain      Low pass 

# Med et RC kredsløb kan spændingsfordeling beskrives ved 
# T(s) = ZR/(ZR+ZC) = R/(R + 1/CS)
# Med lidt omskrivningsmagi: 
# T(s) = 1/(1 + 1/CsR)
# T(s) = s/(s + 1/CR)
# Så har vi en ligning for high pass. 
C, R = symbols("C R")
eq = 1/(C*R) - 50 # = 0 

# Med en noninverting amplifier kan vi løse to formål: 
# 1. Opfører sig som en buffer, og på den måde opfylde kædereglen, så hvert kredsløb kan skrives for sig. 
# 2. Sikre gainet. 

# Noninverting amplifier: K = (R1 + R2)/R2
# Så har vi endnu en ligning
R1, R2 = symbols("R1 R2")
eq = 1/(C*R) - 50 # = 0 
eq1 = (R1 + R2)/R2 - 3.16224 


# Nu mangler der en ligning for low pass filteret
# vha. Spændingsdeler: 
# T(s) = ZR/(ZL + ZR) = R/(Ls + R)
# Med lidt omskrivningsmagi: 
# T(s) = (R/L)/(s + R/L)

# Så har vi endnu en ligning 

RC, RL = symbols("RC RL")

# High pass
eq = 1/(C*RC) - 50 # = 0 
C = solve(eq.subs(RC, 50000)) # Hvis RC = 50kOhm 
RC = 50e3
# Gain
eq1 = (R1 + R2)/R2 - 3.16224 # Hvis R2 = 60, så er R1 ca. 130
R1 = 130
R2 = 60

# Low pass
eq2 = RL/L - 50 # = 0 
RL = solve(eq2.subs(L, 330e-3)) # Hvis L = 330mH
L = 330e-3

print(C)
print(RC)
print(R1)
print(R2)
print(RL)
print(L)

# Nu kan kredsløbet tegnes, som det ser ud i Figur 12.21
# Tegningen findes i uge 19 mappen. 



# Opgave 12.55 - Consider the gain plot in Figure P12-55.
# a. Find the transfer function corresponding to the straight line gain plot.
# Nulpunkt ved 100 & 500 rad/s 
# Pol ved 10 og 5000 rad/s
# Gain i passbanden på 0, fald til -20dB 
s = Symbol("s")
f = np.logspace(0, 4, 100)
s = 1.0j*f # Normalt vil det have været 2*pi*f men siden, at det her er i rad og ikke hz, er det ikke sådan. 
T = 1*((s + 100) * (s + 500)) / ((s + 10) * (s + 5000))


db_mag = 20*np.log10(np.abs(T))
plot(db_mag, "Opgave 12.55 plot", f)

# c. Design a circuit that will realize the transfer function found in part (a).
# Med nulpunkter er der et eksempel på side 646 som deler funktionen i 2. 
# Der omskrives
# T1 = (s + 100)/ (s + 10) 
# T1 = (s/100 + 1) / (s/100 + 1) = Z2/(Z1 + Z2)
# T1 = (1/100 + 1/s) / (1/100 + 1/s) = Z2/(Z1 + Z2)
# For at 1/10 kan blive til 1, så skal Z1 være 9/10
# Z2 = 1/100Ohm  + 1/cs, hvor
# Z1 = 9/10Ohm
C1 = 1#F 
R1 = 9/10
R1_2 = 1/100 # I serie med kondensatoren mod ground.


# T2 = (s + 500) / (s + 5000) 
# T2 = (s/500 + 1) / (s/500 + 10) = Z4/(Z3 + Z4)
# Z4 = Ls + R = 1/500H*s + 1 Ohm = 2mH*s + 1 Ohm
# Z3 + Z4 = Z3 + 2mHs + 1 ohm = 2mHs + 10 Ohm. 
# Z3 = 9 Ohm 
L2 = 2e-3
R2 = 9
# Gainet blev antaget til at være 1, som var meget tæt på straight line diagrammet. En noninverting amplifier bruges da bare som buffer for, at kædereglen er opfyldt.

# Noninverting amplifier K = (R1 + R2)/R2
# Hvis R1 << R2 kan amplifierens gain approximeres til at være R2/R2 = 1 
Rg1 = 100e-3 # 100mOhm 
Rg2 = 100e3 # 100kOhm 
# Forskellen er en million. Rg1 er en mu del af Rg2, dermed må K være = R2/R2

# Diagrammet tegnes. 