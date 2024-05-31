import numpy as np
from sympy import * 

# Opgave 12.1 - A transfer function has a passband gain of 500. At a particular frequency in its stopband, the gain of the transfer functions is only 0,00025.
# By how many decibels does the gain of the passband exceed that of that frequency in the stopband.

# Formel 12.3 

#|T(j_omega|_dB = 20log10|T(j_omega|))

T_DB0 = 20*np.log10(500) 

T_DB1 = 20*np.log10(0.00025)
T_DBDelta = 20*np.log10(500/0.00025)

delta = T_DB0-T_DB1

print(delta)
print(T_DB0)
print(T_DB1)

# Opgave 12.3 - A certain low-pass filter has the Bode diagram shown in Figure P12-3. 

# a. How many dB down is the filter at 5000 rad/s. 
print(20*np.log10(20))

# Estimate where the cutoff frequency occurs, then determine how many dB down is the filter at one decade after the cutoff frequency? 
# Cutoff frequency ses til at være ved omega = 10 rad/s

# Gain 17 -> 0.3 efter en decade(10^3)
T_DBDelta = 20*np.log10(17/0.3)
print(T_DBDelta) # 35 DB down one decade after the cutoff frequency.
