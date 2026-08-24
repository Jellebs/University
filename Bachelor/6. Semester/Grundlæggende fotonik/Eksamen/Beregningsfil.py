import matplotlib.pyplot as plt 
import numpy as np

class diffractionEfficiency(): 
    def __init__(self):
        fig, ax = plt.subplots()
        ax.grid()
        x = np.linspace(-3 * np.pi, 3 * np.pi, 1000)
        y = (np.tanh(x))**2
        ax.plot(x, y)

        # Set ticks in terms of π
        xticks = np.arange(-3 * np.pi, 3.25 * np.pi, np.pi)
        xtick_labels = [r"-$3\pi$", r"$-2\pi$", r"$-\pi$", r"$0$", r"$\pi$", r"$2\pi$", r"$3\pi$"]
        ax.set_xticks(xticks)
        ax.set_xticklabels(xtick_labels)
        plt.show()



    xtick_labels = [
        r"$0$" if i == 0 else 
        rf"$-\frac{{{abs(i)}}}{{4}}\pi$" if i < 0 and abs(i) != 4 else
        rf"$-{int(abs(i)//4)}\pi$" if i < 0 else
        rf"$\frac{{{i}}}{{4}}\pi$" if i != 4 and i % 4 != 0 else
        rf"${int(i//4)}\pi$" for i in range(-4, 5)
        ]

class Simulering(): 
    def refraktativIndeksPlot(self): 
        I = np.logspace(-4, 4, 30)                      # Watt/(cm)^2
        deltan = (9.28e-12)*I
        fig, ax = plt.subplots()
        ax.set_ylabel(r"$ \Delta n$", fontsize = 30)
        ax.set_xlabel(r"$I \quad [\frac{W}{(cm)^2}]$", fontsize = 30)
        ax.tick_params("both", labelsize = "20")
       

        ax.grid(True)
        ax.plot(I, deltan, label = r"$ \Delta n(I)$")
        fig.legend(fontsize = 30)
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_xticks([1e-4, 1e-2, 1e0, 1e2, 1e4])
        ax.set_yticks([1e-7, 1e-11, 1e-15])
        # ax.set_yticklabels([r"$10^{-7}$", r"$10^{-12}$", r"$10^{-15}$"])
        # plt.xscale('log')
        # plt.yscale('log')
        plt.show()
    
    
    def __init__(self):
        self.refraktativIndeksPlot()
    

Simulering()
        