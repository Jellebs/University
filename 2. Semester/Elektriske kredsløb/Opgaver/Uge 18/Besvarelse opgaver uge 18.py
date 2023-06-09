import numpy as np 
from sympy import * 
from Formelsamling.Elektriske_Kredsløb import * 


def printOpgave(tekst, opgave): 
    print(f"""

---------------------------- {opgave} -------------------------
{tekst}

""")

# Opgave 11.11. Find the voltage transfer function Tv(s) = V_2(s) / V_1(s) of SS the cascade connection in Figure P11-11. 
# Locate the poles and zeros of the transfer function

# Kædereglen er opfyldt, derfor kan de to inverterende forstærkere beregnes hver for sig, og bagefter ganges sammen. 
# Z_out af første forstærker = 0. 

# Kredsløb. 
C1 = 10e-9 # 10nF
C2 = 15e-9 # 15nF
R1 = 10e3 # 10kOhm
R2 = 10e3 # 10kOhm
R21 = 100e3 # 100kOhm 

s = symbols("s")
Zeq1 = 1/(
    1/(R1) 
    + 1/(1 / (C1*s))
) # Zc || ZR1

A1 = -Zeq1/R1
print(A1)

Zeq2 = 1/(
    1/(R21) 
    + 1/(1 / (C2*s))
) # Zc || ZR1

A2 = -Zeq2/R2

Aeq = A1*A2
pol = expand((1.0e-8*s + 0.0001)*(1.5e-8*s + 1.0e-5))
print(pol)
p1, p2 = solve(pol, s)

tekst = f"Da nævneren ikke er afhængig af s, så findes der ingen nulpunkter / zeros.\nPolerne løses til at være\np1 = {p1}, \np2 = {p2}"
printOpgave(tekst, "Opgave 11.11")

# Find the voltage transfer function Tv(s) = V2(s)/V1(s) in Figure P11-12. Select values of R1, R2 and C so that Tv(s) has a pole at s = -250krad/s and R2/R1 = 100

# Inverting amplifier, K = -R2/R1 
# ZR2 = Req for R2 & ZC i parallel
# ZR2 = 1/((1/R2) + (1/1/Cs)) 
# ZR2 = 1/((1/R2) + Cs) 

# K = V2(s)/V1(s) 
# K = -(1/((1/R2) + Cs)) / R1

R1, R2, C, s = symbols("R1 R2 C s")
eq = -(1/(1/R2 + C*s))/R1 
eq = -1/(C*R1*s + R1/R2)
eq = (-1/C*R1)/(s + R1/(R1*C*R2))
eq = (-1/C*R1)/(s + 1/(C*R2))
# 1/(C * R2) = 250k
C = 4e-6 # 4uF 

eq1 = 1/(C * R2) - 250e3
R2 = 1 # 1 Ohm  
R1 = R2/100 # 100m Ohm 
pol = solve(s + 1/(C*R2)) # = -250kRad/s

svar = f""" 
For kredsløbet i figur P11-12, så kan
R1 = {R1}
R2 = {R2}
C = {C}
Hvis R2/R1 = 100 & 
s = -250kRads for en pol.
Transfer funktionen er: 
eq = (-1/C*R1)/(s + 1/(C*R2)"""

opgaveBesvarelse("Opgave 11.12", svar)



# Opgave 12.18 - The transfer function of a first-order circuit is
#   T(s) = 10000/(s + 2000)
# a. Identify the type of gain response. Find the cutoff frequency and the passband gain
#   Low pass = K / (s + alpha )
#   Det ligner derfor en lowpass filter
# pol ved 2000rad/s = cutoff frequency 
# Da det er et lowpass filter, så må passband gainet være før w = alpha 
# 10000/2000 = 5, for w = 0

# så 
# wc = 2000rad/s & 
# Gain = 5
f = np.logspace(2, 4, 100)
s = 1.0j * f 
Ts = 10000/(s + 2000)
db_mag = 20*np.log10(np.abs(Ts))
filter_bodePlot(Ts, "Low pass filter", f)

# c. Design a circuit to realize the transfer function

# T(s) = 10000/(s + 2000)
# K sættes lige med alpha, og vha. en amplifier så fåes gainet senere. 
# T(s) = 4 * (2000/s)/(1 + 2000/s) = Z2/(Z1 + Z2)
# T(s) = 4 * (1/(5e-4s))/(1 + 1/(5e-4s)) = (1/(Cs))/(1 + 1/(Cs))
C = 5e-4 # 0.5mF
Rf = 1 # 1 Ohm

# En noninverting amplifier har gain K = (R1 + R2)/R2 
# K = 4, 4R2 = R2 + R1 
# R2 = 1/4(R2 + R1)

R2 = 100 # 100 Ohm
# R1 = 4R2 - R2
R1 = 300 # 300 Ohms
# Kredsløbet er tegnet og ligger i uge 18 mappen i opgaver. 
