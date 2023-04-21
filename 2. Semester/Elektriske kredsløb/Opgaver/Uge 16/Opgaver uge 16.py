import numpy as np
from sympy import * 

# Opgave 10.41

# a. Transform the circuit into the s domain and formulate mesh-current equations
# KVL bruges

# I: -v1(t) + i_A*Ls + (i_A - i_B)*R_1 = 0 
# II: i_B*R_2 + i_B*(1/Cs) + (i_B - i_A)*R_1 = 0 

v1, iA, iB, R1, R2, L, C, s = symbols('v1 iA iB R1 R2 L C s')


I = -v1 + iA*L*s + (iA - iB)*R1

II = iB*R2 + iB*1/(C*s) + (iB - iA)*R1
print(I)
# Isoler kilder
axI= solve(I, v1)[0] # b = v1
print(axI)
# Factoriser for iA iB
axI_fac = factor(axI, (iA, iB))


# Factoriser for iA iB
# For kondensatorer 


axII_fac = factor(II, (iA, iB), fraction = True)
print(II)
print(axII_fac)


A = Matrix([
    [0, -R1], 
    []
    ])










i_B = solve(II, iB)[0]
iA = iA.subs(iB, i_B)

