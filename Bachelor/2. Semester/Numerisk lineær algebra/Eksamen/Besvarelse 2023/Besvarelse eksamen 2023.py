from Formelsamling.Numerisk_Lineær_Algebra import * 
import numpy as np 
import sympy as sp 
import matplotlib.pyplot as plt

def opgave_6(): 
    s = np.array([-3.0, -2.0, -1.0, 0.0, 1.0, 1.1, 2.0, 3.0])
    h = np.array([-3.1, 2.9, 5.1, 3.5, 4.0, 3.2, 5.0, 5.8])[:, np.newaxis]
    cols = 4
    A = np.vander(s, cols)
    svar = f""" 
    Ved hjælp af datapunkterne og funktionen vander fik jeg følgende ligninger: 
    Av = b
    {A}
    
    * v 

    =
    {h}
    v = manglende koefficienter i R^8x1
    b = h i R^8x1
    A = er vander Matricen som er R^8x4, så matricen er ukvadratisk. 
    Der findes 4 ligninger, men 8 ubekendte. Det vil altså sige, at vi ikke har ligninger nok til at finde alle koefficienterne, 
    og da kan vi ikke forvente en eksakt løsning.
    """
    opgaveBesvarelse("Opgave 6.a", svar)

    q, r = gramSchmidt(forbedretGramSchmidt=True, a=A)
    løsning = np.linalg.inv(r) @ q.T @ h
    svar = f"""Rx = Q.T@B, da må
              x = R^-1@Q.T@b  
              løsningen = {løsning[:, 0]}          
            """
    opgaveBesvarelse("Opgave 6.b", svar)
    def opgave_c(): 
        fig, ax = plt.subplots()
        ax.plot(s, h, 'o')
        x = np.linspace(-2.9, 3.1, 100)
        ax.plot(x, np.vander(x, cols) @ løsning, label = "Gram Schmidt approksimation")
        fig.savefig("Gram Schmidt approksimation")
    def opgave_d(): 
        u, s, vt = np.linalg.svd(A)
        svar = f"""
        De singulærer værdier findes som: 
        s = {s}
        Den øvregrænse for konditionstallet til A er blevet udledt i noterne til at være. 
        sigma0 / sigma_k-1 
        kappa = {s[0]/s[-1]}
        """
        opgaveBesvarelse("Opgave 6.d", svar)
    opgave_d()

def opgave_5(): 
    w0 = np.array([1,  0,  1,  0, 1,  1], dtype= float) [:, np.newaxis]
    w1 = np.array([0,  1,  0, -1, 1, -1], dtype= float) [:, np.newaxis]
    w2 = np.array([1, -1, -1, -1, 0,  0], dtype= float) [:, np.newaxis]
    w = np.hstack([w0, w1, w2])
    gramma = w.T @ w
    def opgave_a(): 
        print(
            np.vdot(w0, w1),
            np.vdot(w0, w2), 
            np.vdot(w1, w0), 
            np.vdot(w1, w2), 
            np.vdot(w2, w0), 
            np.vdot(w2, w1))
    # opgave_a()
    u = np.array([3, 4, -3, 4, 0, 0], dtype= float)[:, np.newaxis]
    def opgave_b(): 
        projektion = np.empty_like(u)
        projektion += projektionPå(w0, u)
        projektion += projektionPå(w1, u)
        projektion += projektionPå(w2, u)
        opgaveBesvarelse("Opgave 5.b", f"Projektion_u = {projektion}")
    # opgave_b()

    def opgave_d(): 
        v0 = 1/np.linalg.norm(w0) * w0
        v1 = 1/np.linalg.norm(w1) * w1      
        v2 = 1/np.linalg.norm(w2) * w2
        v = np.hstack([v0, v1, v2])
        opgaveBesvarelse("Opgave 5.d", f"v =\n {v}")
    opgave_d()

opgave_5()
