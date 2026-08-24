import numpy as np
import matplotlib.pyplot as plt 
import scipy.signal as sig 
def opgave2(): 
    b = [1.81]
    a  = [1, 0, 0.81]
    omega = np.linspace(-0.5, 2*np.pi, 512)
    H = (1 + 0.81*np.exp(-2j*omega))/(1.81)
    fig, ax = plt.subplots(2, 1)
    ax[0].plot(omega, abs(H), label= "Frequency response")

    fig, ax = plt.subplots()
    H_phase = np.angle(H)
    ax[1].plot(omega, H_phase, label = "Wrapped phase function")
    ax[1].plot(omega, np.unwrap(H_phase), label = "Unwrapped phase function")

    
    fig.legend()
    plt.show()


opgave2()