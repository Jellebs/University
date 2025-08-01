import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MultipleLocator

class Fag(): 
    print("")

class AndenOrdensSystemer(): 
        class lead():
            def alphaPlot(self):
                """
                Et plot til at vise forskellige værdier af 
                alpha ud fra forskellige phaseløfts.
                """ 
                fig, ax = plt.subplots()
                phi = np.arange(-np.pi/4, np.pi + 5*np.pi/16, np.pi/16)
                phaseStoerrelse = (1 - np.sin(phi))/(1 + np.sin(phi))
                eq = r'$\frac{1 - \sin(\phi)}{1 + \sin(\phi)}$'
                ax.plot(phi, phaseStoerrelse, label=eq)
                
                labels = [r'$\frac{-\pi}{4}$', '$0$',
                          r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$',
                          r'$\frac{3\pi}{4}$', r'$\pi$',
                          r'$\frac{5\pi}{4}$']
                ax.set_xticks(np.arange(-np.pi/4, 5*np.pi/4+0.01, np.pi/4), labels, fontsize = 12) 

                fig.legend()
                ax.grid(True, alpha = 0.4)
                plt.show()
             
        def OSPMPlot(self, OSMax = 20):
            """
            Overshoot og Phase margin plottet \n
            med dæmpningskoefficienten som variabel.       
            """    
            fig, ax = plt.subplots()
            zeta = np.arange(0, 1, 0.001 )
            Os = 100*np.exp(-np.pi*zeta/(np.sqrt(1-zeta**2)))
            graense = OSMax*np.ones_like(zeta)
            Pm = np.rad2deg(np.arctan(2*zeta/np.sqrt(-2*zeta**2 + np.sqrt(1 + 4*zeta**4))))

            color = 'tab:blue'
            ax.set_ylabel("Overshoot Mp i %",color = color)
            ax.set_xlabel("Daempningskoefficient zeta")
            ax.tick_params(axis='y', labelcolor=color)
            ax.grid(True, alpha = 0.4)
            ax.plot(zeta, Os, label = "Overshoot OS")
            ax.plot(zeta, graense, color='tab:green') # Plot af graense
            ax.set_yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
            ax.set_xticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
            ax2 = ax.twinx()  # Højre akse.
            color = 'tab:orange'
            ax2.set_ylabel('Phase margin gamma m i °', color=color)  # we already handled the x-label with ax1
            ax2.set_yticks([0, 10, 20, 30, 40, 50, 60, 70, 80])
            ax2.plot(zeta, Pm, color=color, label="Phase margin Pm")
            ax2.tick_params(axis='y', labelcolor=color)
            
            fig.tight_layout()  # otherwise the right y-label is slightly clipped
            plt.show()


class Plots(): 
    """
    En klasse til at lave forskellige plots som jeg ikke har nemmere måder 
    end til selv at lave dem, når jeg støder på forskellige problemstillinger.
    """
    def bodePlot(self, omega, GdB, Gangle):
        """
        Et bode plot jeg kan bruge, når jeg ikke kan bruge matlabs bodePlot. 
        Hint: 
        Jeg kan ikke plotte for z transformationen, da matlab ikke er glad for
        vektor scalar operationer med e^(jw). Det kan jeg bruge den her til. 
        """
        fig, ax = plt.subplots(2)
        ax[0].plot(omega, GdB)
        ax[0].set_title('Magnitude Response')
        ax[0].set_ylabel('Magnitude i dB')
        ax[0].grid(True)

        ax[1].plot(omega, Gangle)
        ax[1].set_title('Phase Response')
        ax[1].set_xlabel('Frequency (rad/sample)')
        ax[1].set_ylabel('Phase (radians)')
        ax[1].grid(True)
        fig.tight_layout()
        plt.show()    
