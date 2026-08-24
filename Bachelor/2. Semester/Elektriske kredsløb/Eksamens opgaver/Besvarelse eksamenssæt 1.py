from sympy import * 
import numpy as np
from Formelsamling.Elektriske_Kredsløb import *
# Opgave 1 ( 25 % )
# Kredsløbet til venstre kan omskrives til ækvivalentkredsløbet til højre

# Hvor V01, V02 & V03 er initialspændingerne på kondensator C1, C2 & C3
# Lad C1 = 1uF, C2 = 2uF, V01 = 2V, V02 = 3V & R = 3MOhm
# 1. Bestem C3 & V03

# Kapitel 6.4 - Equivalent capacitence and inductance.
# Kondensatorer i series er det samme som modstande i parallel. 
# C3 = 1/(1/C1 + 1/C2)
C1 = 1e-6 # 1uF 
C2 = 2e-6 # 2uF
R = 3e6

C3 = 1/(1/C1 + 1/C2)
print(C3) # (2/3)uF 

# Jeg laver maske ligning 
# I. -V01 - V02 + R*I = 0 
# RI = V01 + V02 = 5V 
# R = 3M
# I = 5V/3M
I = 5/3e6 # 2/3uA 
# Plus, at jeg har fundet kredsløbsspændingen = 5V, da der ingen andre spændingskilder er

V03 = 5
svar = f"""Ved hjælp af kondensator ækvivalens & maskeligninger fåes
C3 = {C3}F 
V03 = {V03}V"""
opgaveBesvarelse("Opgave 1.1", svar)

# 2. Angiv kredsløbets tidskonstant og differentialligning (dvs. v(t) udtrykt ved R, C3 & V03)
# For RC kredsløb er tidskonstanten Tc = Req*Ceq
# Dette udføres i tidsdomænet
t = Symbol("t")
Tc = R*C3
# For RC kredsløb er v(t) = Zero input + Zero state
# Der findes kun zero input i dette kredsløb
# v(t) = Zero input = V0e^(-t/(R_T*C)) 

v = V03 * exp(-t/(Tc))
svar = f"""For et RC kredsløb i tidsdomænet er tidskonstanten,
TC = ReqCeq
Og for zero input kredsløb er spændingen
V0*e^(-t/Tc)
For dette kredsløb er 
TC = R*C3 = {Tc}
v(t) = V03*e^(-t/(R*C3) = {v}
"""
opgaveBesvarelse("Opgave 1.2", svar)


# 3. Bestem til hvilket tidspunkt v(t) = 1V
tid = solve(v - 1)[0] # = 0

svar = f"""v(t) = 1V, v(t) - 1V = 0. Løst for tiden fåes: 
tid = {tid} tidsenheder"""
opgaveBesvarelse("Opgave 1.3", svar)



# Opgave 2 ( 25% )

# 1. Find Thévenin ækvivalenten til kredsløbet: 
# dvs VT, ZT ved V1, R1 & L

# Der ses en spændingsdeler 
# Kapitel 6.4 - Equivalent capacitence and inductance.
s, L, R1, V1 = symbols("s L R1 V1")
VT = V1 *(R1 / (L*s + R1))

# Kortslutningsstrømmen: 
isc = (V1)/(L*s)

ZT = VT/isc
pprint(ZT)

# Kredsløbet belastes nu af et RC-Kredsløb
# 2. Find udgangsspændingen V2(s) udtrykt ved VT, R1, R2, C & L 

# Der ses stadigvæk en spændingsdeler. 
# ZC / (Zeq + ZC)
C, R2, VT = symbols("C R2 VT")
ZC = 1/(C*s)
Zeq = ZT + R2

V2 = VT * (ZC/(Zeq + ZC))
svar = f"V2 = {V2}"
opgaveBesvarelse("Opgave 2.2", svar)

# Find overføringsfunktionen V2(s)/V1(s) udtrykt ved R1, R2, C & L
V2 = V2.subs(VT, V1 *(R1 / (L*s + R1)))
K = V2/V1
pprint(cancel(K)) # Korrekt √



# Opgave 3 ( 25 % )
# Et signal har følgende Laplace transform 
s = Symbol("s")

F = 1/((s + 1)*(s**2 + 2*s + 2))

# Opskriv Laplace domæne funktionen, ved hjælp af partialbrøksopslitning, på formen: 
# F = k1/(s-p1) + k2/(s - p2) + (k2^*)/(s - p2^*)

# og angiv værdien af k1, k2, p1 & p2.
# polerne findes for (s^2 + 2s + 2) & (s + 1)

p1 = -1 
p2, p2stjerne = solve(s**2 + 2*s + 2)
k1, k2, k2stjerne = symbols("k1 k2 k2*")
# F = k1/(s - p1) + k2/(s - p2) + k2stjerne/(s - p2stjerne)

# k1 = (s + 1)*F(s) = 0, s = -1 = 0*F(s)
Fk1 = 1/(s**2 + 2*s + 2)
k1 = Fk1.subs(s, -1)

# k2 = (s - p2stjerne) * F(s) = 0 
# k2 = (s + 1 - j) * F(s) = 0 
Fk2 = 1/((s + 1)*(s + 1 +1j))
k2 = Fk2.subs(s, -1 + 1j) # = k2stjerne
F = k1/(s-p1) + k2/(s - p2) + (k2)/(s - p2stjerne)
svar = f"""
p1 = {p1}, 
p2 = {p2}, 
p2* = {p2stjerne}, 
k1 = {k1}, 
k2 = k2* = {k2}, 
med formlen: 
F = {F}
"""
opgaveBesvarelse("Opgave 3.1", svar)
pprint(F)
# 3. Opskriv signalet i tidsdomænet ved brug af inverse Laplace transformation. 
t = Symbol("t")
# Tabel 9.2 side 458
# Funktionen ses som en exponential funktion ganget på en dæmpet rampe funktion. 

ft = (exp(-1*t))*(t*exp(-1*(-1 + 1j)*t))
svar = f"f(t) = {ft}*"
opgaveBesvarelse("Opgave 3.3", svar)



# Opgave 4 ( 25 % )
# 1. Opskriv overføringsfunktionen V0(s)/Vi(s), udtrykt ved R1, R2, R3, C1 & C2, for kredsløbet vist på figuren.
# Der ses et filter og et gain i kredsløbet. 
# Filteret kan beskrives ved en spændingsdeler: 
# Vin = Vi * (ZR/(ZC + ZR))
Vi, R1, R2, R3, C1, C2, s = symbols("Vi R1 R2 R3 C1 C2 s")
Vin = Vi * (R1/((1/(C1*s)) + R1))
Vin = Vi * ((R1*C1*s)/((R1*C1*s) + 1))
Vin = Vi* (s/(s + (1/(R1*C1))))
# Med alpha = 1/(R1*C1)
# Så filteret er en s/(s + alpha) som er et 
# høj pas filter Ks/(s + alpha), 
# med K = 1

# Vin får sig et gain 
# K = Noninverting amplifier = (R2 + R3)/R3 
# ZR2 består af C2 & R2 
ZR2 = 1/((1/(C2*s)) + 1/R2)
K = (ZR2 + R3) / R3 


vo = Vin * K # Vin ganget på gainet.
T = vo/Vi

svar = f"Overføringsfunktion = {T}"
opgaveBesvarelse("Opgave 4.1", svar)


# Lad R1 = R2 = 10kOhm, R3 = 100 Ohm, C1 = 10uF & C2 = 0.1uF
# Tegn knækkurveapproksimationen (Bode plottet) for både amplituden og fasen af overføringsfunktionen.

T = T.subs([[R1, 10e3], [R2, 10e3], [R3, 100], [C1, 10e-6], [C2, 0.1e-6]])

# Udtrykket er kompliceret på grund af kondensatoren i gainet, i stedet for at omskrive funktionen, så plotter jeg det i stedet for 
f = np.logspace(0, 2, 100)
s = 1.0j*f
T = s*(100 + 1/(0.0001 + 10000000.0/s))/(100*(s + 10.0))
Tdb = 20*np.log10(np.abs(T))

filter_bodePlot(T, "Opgave 4 overføringsfunktion", f)

