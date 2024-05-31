from sympy import Symbol 
import numpy as np

# 8 - 39. The circuit in Figure P8-39 is operating in the sinusoidal steady state. Use superposition to find the phasor response.
# Spændingen kortsluttets. 

# Polær form:  i_s = 1 < 45° A  = V_A*e^j*\phi

ohm = Symbol("Ω")
Phi= np.array([np.radians(45)]) # Grader
I_A = 1 # A 
Phi_imag = 0.78539816j
i_S = I_A * np.e**(Phi_imag)


spole_impedans = 25j
kondensator_impedans = -50j
resistor_impedans = 25

resistor_ix_impedans = 25
# Der skal findes en equivalens for impendanser så vi kun har resistor_ix_impedansen og thevenin impendansen. 
# Spole i serie med resistor og kondensator i parallel.
# Z_T spole impedans + 1/(1/(resistor_impedans) + 1/(kondensator_impedans))
Z_N = spole_impedans + 1/(1/(resistor_impedans) + 1/(kondensator_impedans))
I_N = i_S
I_X_1 = I_N *(Z_N / (Z_N + resistor_ix_impedans)) # Strømkildens bidrag

# Nu vil thevenin impedansen findes. 
# I_N er afbrudt, så spole impedansen får ingen strøm over sig.

# Phi er blot modsat nu, så fortegnet skiftes.
V_A = 100
v_S = V_A * np.e**(-Phi_imag) # polær form. 100 < -45°
print(v_S)

Z_T = resistor_ix_impedans + 1/(1/(resistor_impedans) + 1/(kondensator_impedans)) # resistor_ix_impedansen er i serie med resistoren parallelt med kondensatoren

V_T = v_S
I_X_2 = V_T/Z_T

I_X = I_X_1 + I_X_2

print(I_X) # Det er resultatet, om det er rigtig, ved jeg ikke. 




# Opgave 8.46

spole_impedans = 1 * 10**(-3)




