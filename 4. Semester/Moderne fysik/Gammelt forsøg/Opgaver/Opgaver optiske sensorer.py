import numpy as np
import matplotlib.pyplot as plt 
from sympy import * 
from Uni.Formelsamling.Fysik import opgaver
def opgaveSpoergsmålstegn(): # Fra relativitetsteori
    L = 1000
    D = 0.25
    Lambda = 1550e-9
    n = 1.46
    P0 = 1
    c = 3e8
    omega = np.linspace(0, 3, 100)
    P = 2*(np.cos((2*np.pi/Lambda) * (D*L/(c*n)) * (omega/2) )**2) * P0 

    fig, ax = plt.subplots()
    ax.plot(omega, P)
    plt.yticks(np.arange(min(P), max(P), 0.1))
    plt.xticks(np.arange(min(omega), max(omega), 0.1))
    plt.show()
    t = 23*60*60 + 56*60 # 86160sekunder for den at dreje om jorden
    rotation_jorden = 360/t # 0.004178 rad/s

    print(rotation_jorden) 
    
