from Formelsamling.StudieHjaelp import Opgave
import matplotlib.pyplot as plt
import numpy as np
import nbimporter
from Algoritmer import Algoritmer 

K = 36
px = np.array([1/K, 2/K, 3/K, 4/K, 5/K])
px = np.hstack([px, 6/K, px[::-1]])

n = np.arange(len(px))
fig, ax = plt.subplots()
ax.stem(n, px)
ax.set_xticks(n)
ax.set_xticklabels(n + 1)
ax.set_xlabel('Antal øjne')
ax.set_ylabel('Sandsynlighed')
ax.set_title('Sandsynlighedsfordeling for summen af to terningekast')
plt.show()


class Øvelse1_1(Opgave): 
    # Regressions øvelse
    x_training = np.array([1, 2, 3])
    t = np.array([4, 1, 5])
    N = len(x_training)
    M = 3
    design_matrix = lambda x, m : np.vander(x, m + 1, increasing=True)[:, 1:] # Design matrix # x^1, x^2, x^3
    weights = lambda X, t : (np.linalg.inv(X.T @ X)) @ X.T @ t
    
    # Test opsætning
    resolution = 50
    x_test = np.linspace(0, 4, resolution)
    Y = np.zeros((resolution, M))
    
    for m in range(1, M + 1):                           # Jeg har ikke brug for M = 0    
        # Træning      
        X = design_matrix(x_training, m)
        w = weights(X, t)         # Vægte for m ordener. 
        
        # Test
        X = design_matrix(x_test, m)
        Y[:, m - 1] = X @ w                           
        
    # Plot
    fig, ax = plt.subplots()
    ax.plot(x_training, t, 'o')
    for m in range(M): 
        ax.plot(x_test, Y[:, m], label = f"M = {m + 1}")
    
    fig.legend()
    plt.show()
        

Øvelse1_1()




