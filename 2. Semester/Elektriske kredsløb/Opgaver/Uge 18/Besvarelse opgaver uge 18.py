import numpy as np 
import sympy as sp

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

s = sp.symbols("s")
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
pol = sp.expand((1.0e-8*s + 0.0001)*(1.5e-8*s + 1.0e-5))
print(pol)
p1, p2 = sp.solve(pol, s)

tekst = f"Da nævneren ikke er afhængig af s, så findes der ingen nulpunkter / zeros.\nPolerne løses til at være\np1 = {p1}, \np2 = {p2}"
printOpgave(tekst, "Opgave 11.11")