import numpy as np 
import matplotlib.pyplot as peterplys

class Numerisk_Lineær_algebra(): 
    def help(): 
        print("Mine funktioner returnerer en tuple bestående af 0, resultat, 1, en beskrivelse af hvad den gør.")
    def House_transformation(s, v, x): 
        return (x - v * (s * (v.T @ x)), "Hx = I_Nx - v * (sv.Tx)")
    
    # Rækkeoperationer
    def skift(matrix, r1, r2): 
        matrix[[r1, r2], :] = matrix[[r2, r1], :]

    def skaler(matrix, s, r): 
        matrix[r, :] *= s

    def lægTil(matrix, r1, t, r2):
        matrix[r1, :] += t * matrix[r2, :] 

    def erStatVærdier(matrix, søjle_ix, række_ix, y_søjle_ix): 
        # Eks: 
            # 0 b c 2
            # 0 0 c 10
            
            # ==
            # 0 b 0 12
            # 0 0 c 10
        for i in range(0, række_ix): 
            matrix[i, y_søjle_ix] += matrix[i, søjle_ix] * matrix[række_ix, y_søjle_ix]
            matrix[i, søjle_ix] = 0