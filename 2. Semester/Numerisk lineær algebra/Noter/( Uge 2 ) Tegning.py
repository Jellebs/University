import numpy as np
import matplotlib.pyplot as plt



class Hus(): 
    __Hus = np.array(
        [
        [7, 0], # Fundament
        [0, 0], 
        [0, 5], 
        [3.5, 7], # Tag
        [7, 5],
        [7, 0]
        ]
    )
    __dør = np.array( 
        [ 
        [2.5, 0], 
        [2,5, 3],
        [4.5, 3], 
        [4.5, 0]
        ]
    )
    def lavFigur(withApplication: tuple(np.array(list))):
        fig, ax = plt.subplots()
        ax.set_aspect('equal')

    