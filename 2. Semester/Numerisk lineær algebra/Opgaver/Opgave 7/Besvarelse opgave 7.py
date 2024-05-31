import numpy as np 
from sympy import * 

init_printing(use_unicode=True)
# Find konditionstal for følgende funktioner

# Konditionstal = (|x||f'(x)|)/|f(x)|

# a = f(x) = 1/(1+x**2)
#     f(x) = 1/1 + 1*x**(-2)
#     f(x) = 1   +   x**(-2)
#       f'(x) = -2x**(-3)

x, y, z = symbols('x y z')

def expression(f): 
    return (x * diff(f)) / f

f = 1/(1 + x**(2)) 
print(simplify(expression(f)))

# b = f(x) = sin(x) 
f = sin(x) 
print(simplify(expression(f)))





# Opgave 7.3. Omskriv de følgende udtryk til formen x + iy med x, y \in reel
a = (3 + 2j) + (-1+1j)
print(a)
b = (3 + 2j) * (-1+1j)
print(b)

c = (3 + 2j) / (-1 + 1j) 
print(c)


# Løs ligningssystemerne

# d = (1+i)z = 2-i 
#   = z = (2-i)/(1+i) 
#       = (2-i)(1-i) /(1+i)(1-i)  
#       = (2-2i-i-i^2) /(1 - 1i +1i - 1i^2)  
#       = (2-3i-1) /(1 + 1)  
#       = (1-3i) / (2) 
#       = 1/2 - 1.5 * i 
#   = z = 0.5 - 1.5i


a = np.array([
    [1.0-1.0j,        1.0j,     -1.0 - 1.0j],
    [    1.0,   2.0 + 1.0j,            1.0j],
    [    1.0j,  1.0 - 1.0j,     1.0 -  1.0j]])

b = np.array([5, 2, 0]) [:, np.newaxis]

print(np.linalg.solve(a, b)) # Det er fandme smart

