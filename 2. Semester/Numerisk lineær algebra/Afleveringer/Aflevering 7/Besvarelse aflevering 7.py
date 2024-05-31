import numpy as np 
import matplotlib.pyplot as plt
from sympy import * 
from Formelsamling.Numerisk_Lineær_Algebra import *
# Belysning på parkeringsplads opgave

# a. Angiv hvordan belysningsniveauet y = (y0, ..., y599) og styrkeren x = (x0, ... x11) 
#    er relateret via et lineært løsningssystem. 
#    Opstil koefficientmatricen for systemet i python. 

lamper = np.array([
    [ 2,  3, 3.0],
    [ 4, 13, 3.6], 
    [ 4, 19, 3.0], 
    [11,  5, 3.5], 
    [12, 12, 4.0], 
    [13, 18, 3.6], 
    [15,  2, 4.5], 
    [16, 16, 3.0], 
    [20,  4, 2.8], 
    [23, 12, 4.0], 
    [25, 16, 3.8], 
    [28,  9, 3.4]
    ]) # x y z

# A = 1/d_i_j 

def danKoefficientMatrice(lamper): # Lav en 600 x 12, søjle 1, række 3 = 1*20 + 3
    A = np.empty((600, 12), dtype= float)
    for k in range(lamper.shape[0]): 
        for j in range(20): # Rækker
            for i in range(30): # Søjler 
                deltax = (lamper[k, 0] + 0.5) - i 
                deltay = (lamper[k, 1] + 0.5) - j
                pyth = np.linalg.norm([deltax, deltay, lamper[k, 2]]) # √(x**2 + y**2 + z**2)
                A[i*20 + j, k] = 1/(pyth**2)
    return A

def aflevering(opgave):
    A = danKoefficientMatrice(lamper)
    x = np.ones(12) * 20 
    if opgave == 'a' or opgave == 'b': 
        b = A @ x
    else: 
        b = np.ones(600)
    # Til opgave c og op efter 
    # Forbedret Gram Schmidt
    q, r = gramSchmidt(forbedretGramSchmidt=True, a=A)
    c =  q.T @ b 
    x_gs = back_substitution(r, c)
    # SVD  
    u, s, vt = np.linalg.svd(A, full_matrices=False)
    sigma = np.diag(s)
    x_svd = vt.T@(np.linalg.inv(sigma)@(u.T@b)) 
    match opgave: 
        case 'a': 
            print('''
----------------------- Opgave a -----------------------
            ''')
        case 'b': 
            print('''
----------------------- Opgave b -----------------------
                  ''')
            b = np.reshape(b, (20, 30), 'F')
            fig, ax = plt.subplots()
            ax.imshow(b, cmap='hot', interpolation='nearest')
            # fig.savefig('Heatmap.pdf')
        case 'c': 
            # Mindste kvadratters metode:
            print(f'''
----------------------- Opgave c -----------------------
Løsning fundet ved hjælp af den forbedrede Gram Schmidt metode: 
{x_gs[:, 0]}

Løsning fundet ved hjælp af den Singulære værdi dekomponering: 
{x_svd}

Som ved disse antal decimaler ser ens ud. 
                  ''')
        case 'd': 
            # Mindste kvadratters metode:   
            
            b = A @ x_gs 
            b = np.reshape(b, (20, 30), 'F')
            b_fra_1 = b - np.ones((20, 30))
            plt.imshow(b_fra_1, cmap='hot', interpolation='nearest')
            plt.colorbar()
            # plt.savefig('Heatmap_optimeret_GS.pdf')
            '''
            b = A @ x_svd 
            b = np.reshape(b, (20, 30), 'F')
            b_fra_1 = b - np.ones((20, 30))
            plt.imshow(b_fra_1, cmap='hot', interpolation='nearest')
            plt.colorbar()
            # plt.savefig('Heatmap_optimeret_SVD.pdf')
            '''
            print(f'''
----------------------- Opgave d -----------------------
Gram Schmidt løsning 
''')
        case 'e': 
            Pb = A @ x_gs
            cosTheta = np.linalg.norm(Pb) / np.linalg.norm(b)
            kappa_A = s[0]/s[-1]
            græsk_n = np.linalg.norm(A)*(np.linalg.norm(x_gs) / np.linalg.norm(A @ x_gs))
            kappa = kappa_A/(græsk_n * cosTheta)   

            kappa_max = kappa_A + (kappa_A**2 * np.tan(np.arccos(cosTheta))/græsk_n)    

            korrekthed = x_gs * (1.3*10**1 * np.finfo(float).eps)

            print(f'''
----------------------- Opgave e -----------------------
kappa_A = {kappa_A}
græsk_n = {græsk_n}
cosTheta = {cosTheta}

Sammen danner de med formlen fra notesæt 17 konditionstallet: 
kappa = {kappa}

Den størst mulige værdi findes for uligheden opfyldt af vores beregning, vist i formel 17.3
kappa_max = {kappa_max}

Vi kan da sige er svaret er korrekt indenfor +- {korrekthed}
''')


aflevering('e')






