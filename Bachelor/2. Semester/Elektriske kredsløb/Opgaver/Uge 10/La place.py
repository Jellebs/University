from sympy import *

#init_printing(use_printing=True)
t, s = symbols('t s')
f = 2 - 5*exp(-2*t) + 3*cos(2*t)+ 3*sin(2*t) 
F = laplace_transform(f, t, s)
print(F)

f = (exp(-2*t)) + 4*t - 1
print(laplace_transform(f, t, s))

f = (2+2*sin(2*t)- 2*cos(2*t))
print(laplace_transform(f, t, s))