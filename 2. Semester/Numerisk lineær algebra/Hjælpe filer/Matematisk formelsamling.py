""" 

Matematiske

"""
 
# Fejl
#   x' - x 
#   Gamma = (x'-x)/x - Den relative fejl.
#
#
# Længde af vektorer = Pythagoras
# Vinkel af vektorer: cos(\theta) = x/√(x^2+y^2) , sin(\theta) = y/(√(x^2 +y^2)) - Typisk er cos(\theta) mere præcis, derfor bruger vi denne. 


# Numpy funktioner
# Længden af en vektorer: np.linalg.norm("vektor")
# inverse trigonometriske funktioner: 
#   arc kommer foran.
#   arccos(), arcsin(), arctan()
#   theta kommer som radianer



#                   Vektor beregning
"""
                        Rotation 
Rotationsvektor: 
    [[cos(\theta), -sin(\theta)], 
     [sin(\theta), cos(\theta)]]
"""

#                   Ortogonalitet
#                       Projektion til linje 
"""
    ||u - pr_v(u)|| = √(||u||_2**2 - ||pr_v(u)||_2**2) # Afstand fra linjestykke til punkt u.
        pr_v(u) = <u,v>/||v||_2**2 * v
        
"""


#                       Parsevals identitet
"""
    ||u||_2 ** 2 = x_0^2 * ||v_0||_2**2 + x_1**2*||v_1||_2**2 + ... + x_k-1**2||v_k-1||_2**2
    Af det kan vi bruge at: 
        u = x_0_v0 + x_1v_1 + ... x_k-1v_k-1                                                                                    (8.8)
        og deraf også 
        x_n = <u,v_n>/||v_n||_2**2 hvor n er et vilkårligt punkt.                                                               (8.9)
"""




