import sympy as sp 

# ----------------------------- Helper function ----------------------------- #

def printOpgave(str, opgave): 
    print(f"""
----------------------------- {opgave} -----------------------------
{str}
    """)




# Opgave 2.9

# Op amp 
# 2x 10kohm resistors. 
# What closed loop gain would you expect? 
R1 = 10e3
R2 = 10e3

A = -R2/R1 # Gain på 1

# if a dc voltage of +1.00V is applied at the input, what outputs result? 
vIn = 1.00 #1V 
vOut = vIn*A #1V

# if the 10kOhm resistors are said to be 1% resistors, what range of outputs would you expect to have with precisely 1.00V?
vMin = vIn - vIn*0.01 # -1%
vMax = vIn + vIn*0.01 # +1%
svar = f"A = {A}, \nvOut = {vOut}V, \nInterval = ]{vMin}:{vMax}[ V"

printOpgave(svar, "Opgave 2.9")




# Opgave 2.13 
# Design an inverting op-amp circuit for which the gain is -10 and the total resistance used is 100kOhm 

# A = -R2/R1 # Gain for inverting amplifier. 

# -10 = -100kOhm/R1
# -10 = -100kOhm/10kOhm == Sandt

R1 = 10e3
R2 = 100e3
A = -R2/R1

svar = f"A = -R2/R1.\n-10 = -100kOhm/10kOhm, \nA = {A}"

printOpgave(svar, "Opgave 2.13")





# Opgave 2.18 
# 5kOhm & 15kOhm 
# vOut = 5V
# vIn =-15V

# v5kOhm? 
# A = 
# with 1% resistors what are the limits of the ouput voltages
# with 15V +- 1% too, what is the range of the output voltages that might be found? 





# Opgave 2.85

# differentiator 
# Tc = 10^(-5)
# C = 1nF

# Tc = RC 
# Tc/C = R

C = 1e-9
R = 10e-5/C 
print(R)


# Sketch magnitude & phase response of the circuit, indicating the frequency at which the magnitude response equals 0 dB. 
# |vO/v_i| = -j*Omega*C*R, hvor omega er x^-1
# Hældningen er da -1/C*R * x

# A series input resistor is added to limit gain magnitude high frequencies to 100. 
# Sketch the modified on the same axes as the ideal differentiator. 




# Opgave 2.103
# The circuit shown in Fig. P2.103 uses an op amp having a +- 3mv offset. What is its output offset voltage? 

# What does the output offset become with the input ac coupled through a capacitor C?
# If instead a large capacitor is placed in series with a 1kOhm resistor what does the output offset become? 

# KVL 
vIn, i = sp.symbols("vIn i")
I = -vIn + i*1e3 + i*1e6 + i*1e6
i = sp.solve(I, i)
vIn = sp.solve()
print(i)





# Opgave 2.113

# Opgave 2.115








