import numpy as np
import matplotlib.pyplot as plt
from sympy import * 
from Formelsamling.Elektriske_Kredsløb import * 

s = Symbol("s")
poler2grad = s**2 + 10*s + 34 
p2, p2stjerne = solve(poler2grad)
print(p2, p2stjerne) # -5 +- 3I 

eq = (10*s + 140)/((s+4)*(s+5+3j))
print(eq.subs(s, -5 + 3j))

F = 10/(s+4) + 10/(s+5-3j)+10/(s+5+3j)

F = (10*s+140)/((s+4)*(s**2+10*s+34))
t = Symbol("t")
# f = inverse_laplace_transform(F, s, t)
# print(f)

f = np.logspace(4, 5, 100)
s = 1.0j*f 
T = (3200*s)/((3200*s +1*s**2+400e6))

db_mag = 20*np.log10(np.abs(T))
# filter_bodePlot(db_mag, "Approximation", f, save = True)
filter_gain()

def T(gain): 
    eq = (3200*s)/((3200*s +1*s**2+400e6)) - gain
    print(solve(eq))

# T(1.778279)
filter_qualityFactor()