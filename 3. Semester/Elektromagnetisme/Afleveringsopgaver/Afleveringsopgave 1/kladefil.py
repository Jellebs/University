from sympy import * 

Q, a, b, k = symbols("Q a b k")
Fe1x = (-(Q**2))/(a**2) - ((Q**2)*a)/((b**2+a**2)**1.5) 
Fe1y = (Q**2)/(b**2) + ((Q**2)*b)/((b**2 + a**2)**1.5)

Fe1 = k*Matrix([Fe1x, Fe1y])

Fe2x = (-(Q**2))/(a**2) + (-(Q**2)*a)/((b**2 + a**2)**1.5)
Fe2y = (-(Q**2))/(b**2) + (-(Q**2)*b)/((b**2 + a**2)**1.5)

Fe2 = k*Matrix([Fe2x, Fe2y])

Fe1 = N(Fe1.subs(zip([Q, a, b, k], [-1*1e-9, 4*1e-2, 2*1e-2, 8.99*1e9])), 4)
Fe2 = N(Fe2.subs(zip([Q, a, b, k], [-1*1e-9, 4*1e-2, 2*1e-2, 8.99*1e9])), 4)

print(Fe1, Fe2, sep="\n\n")
