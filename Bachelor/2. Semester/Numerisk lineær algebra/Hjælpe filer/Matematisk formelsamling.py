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



#                   Konditionstal
# 
#   kappa(x) = relativ fejl i f(x) / relativ fejl i x
#   kappa(x) = |(x*f'(x))|/|f(x)|
# 
#   x**2 => kappa(x) = 2 ( Fejlen er fordoblet )
#   x**(1/2) => kappa(x) = 1/2 ( Fejlen er halveret )
#
#   For en matrice gælder der at: 
#   kappa(x) = sigma0 / sigma_n-1, hvor sigma er singulære værdier,
#   og for vores matricer gælder der, at de sigma 0 er den største værdi, og sigma n-1 er den mindste værdi.
#   kappa(x) = største værdi / mindste værdi.


#                   Mindste kvadratters metode 
#  Indtil videre har vi 4 løsninger for mindste kvadratters metode
# 
#       Gram Schmidt
#           Opstilling: A = QR
#           Løsning   : Rx = Q.T @ b
#           Flops     : 2mn^2 
#       
#       House holder
#           Opstilling: A = QR
#           Løsning   : Rx = Q.T @ b
#           Flops     : 2mn^2 - 2/3n^3
#
#       Reduceret SVD 
#           Opstilling: A = UsigmaV.T
#           Løsning   : V @ sigma^(-1) @ (U.T @ b)
#           Flops     : 2mn^2 + 11n^3
# 
#       Normalligning
#           Opstilling: A.T @ Ax = A.T @ b
#           Løsning   : (A.T @ A)^(-1)(A.T @ b)
#           Flops     : mn^2 + 1/3n^3 
# 
#       Hvis matricen er kvadratisk så er Gram Schmidten den mest optimerede metode i forhold til flops(umiddelbart). Ulempen er dog, hvis matricen ikke er kvadratisk.
#       Hvis matricen ikke er kvadrattisk kan SVD bruges, hvor der kan findes en løsning for alle matricer.
