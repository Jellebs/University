from sympy import * 
import scipy.signal as sig
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


class SignalerOgSystemer: 
    def periodePlot(t, funktioner): 
        for funktion in funktioner: 
            fig, ax = plt.subplots()
            ax.plot(t/np.pi, funktion)
            ax.xaxis.set_major_formatter(plt.FormatStrFormatter('%g $\pi$'))
            ax.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(base=1))
            plt.show()

    ###             Transformations             ##
    def time_shift(self, ts, shift):
        return ts - shift
    
    def time_scale(self, ts, scalar):
        return ts * scalar

    def time_rev(self, ts):
        return self.time_scale(ts, -1)
    
    def plot_transforms(self, ts, ys, transforms_dict):
        """ 
        Takes original set of times: ts and signal: ys and plots them,
        with the entries of transformed signals: ys_i in transforms_dict.
        """
        num_figs = len(transforms_dict) +1
        fig, axes = plt.subplots(num_figs, figsize=(18, 4*num_figs))
        fig.subplots_adjust(hspace=0.)
        
        # plot original
        axes[0].plot(ts, ys, label='Original signal')
        
        # plot entries in dict
        for i, key in enumerate(transforms_dict):
            axes[i+1].plot(ts, ys, label='Original signal', alpha=.3)
            axes[i+1].plot(ts, transforms_dict[key], label=key)

        # draw legends and grids
        for ax in axes:
            ax.grid(True, alpha=.2)
            ax.legend()
        plt.show()
    
    def harmoniskTilEksponentiel(f): 
        eksponentielleUdtryk = [udtryk.rewrite(exp) for udtryk in f.args]
        return eksponentielleUdtryk
    
    def fourierSerieRepræsentation(funktioner):
        """
        En funktion til at lave fourier serie repræsentation på flere funktioner af gangen. 
        For hver funktion: 
            Hav T, liste af grænser, xt deres tilsvarende værdier, klar. 
                T, grænser, xt = funktioner[i]
        returnere en formel for ak 
        
        Tips til at printe resultaterne: 
            .doit vil evaluere integralet
            nsimplify(ak) vil printe udtrykket rationelle udtryk. 
        """
        # ? Formlen bag
        ak, xt, T, k, omega0, t = symbols("ak x(t) T k omega t")
        harmSignal = lambda omega0 : exp(-1j*k * omega0 * t)
        ak = (1/T) * Integral(xt * harmSignal(omega0), (t, T))
        a_k = symbols("a_k")
        pprint("Formlen bag de ligninger jeg får sat op")
        pprint("="*30)
        pprint(Eq(a_k, ak))
        pprint("="*30)
        pprint("\n\n")
    
        # * Opstilling af ligninger i en liste.
        a_ik = list(symarray(0, 1)) # aik in R^nx1       
        for funktion in funktioner:
            i = 0
            for (T, graenser, xt) in funktion:                  # For hver grænse i et signal bliver et integrale lagt til med dens tilsvarende værdi.
                # print(graenser +)
                # pprint(Integral(xt[0], (t, graenser[0][0], graenser[0][1])))
                a_ik.append(
                    (1/T) * (sum([Integral(xt[i]*harmSignal(2*pi/T),
                                           (t, graenser[i][0], graenser[i][1]))
                                  for i in range(len(xt))]))
                    )
                i+= 1
        a_ik.pop(0)                                             # 0 element var ikke en ligning.  
        return a_ik 
    
    def pzplotZ(b, a, roc='indre', roc_interval = None):
        """
        Min fortolkning på et pole zero plot i Z domæne.
        
        Parametrer:
        b -- Koefficienterne i tælleren for en Z transformation
        a -- koefficienterne i nævneren for en Z transformation
        roc --  'indre' plotter ROC for |z| < a
                'ydre' plotter ROC for |z| > a
        """
        stil = {
            "Indstillinger" :   ["Farve", "Markør"  , "Label"               , "Linjestil"  , "Linjetykkelse"    , "Udfyldt" , "alpha"   ],
            "Titel"         :   [""     , ""        , "Pole nulpunkts plot" , ""           , ""                 , ""        , ""        ],
            "Poler"         :   ["Red"  , "x"       , "Poler"               , ""           , ""                 , ""        , ""        ],
            "Nulpunkter"    :   ["Blue" , "o"       , "Nulpunkter"          , ""           , ""                 , "False"   , ""        ],
            "ROC"           :   ["Green", ""        , "ROC"                 , ""           , 0.4                , False     , 0.4       ],
            "Enhedscirklen" :   ["Black", ""        , "Enhedscirklen"       , ""           , ""                 , False     , 1         ]
        }
        
        zeros, poles, _ = sig.tf2zpk(b, a)

        print(zeros, poles)
        # Create a fine grid in the complex plane
        max_value = max(np.abs(np.hstack([zeros, poles])))
        r = max_value + 1
        n = 400
        real_vals = np.linspace(-r, r, n)
        imag_vals = np.linspace(-r, r, n)
        X, Y = np.meshgrid(real_vals, imag_vals)
        Z = X + 1j * Y
        
        Z_mag = np.abs(Z)                                                                               # |z| 
        
        # ROC 
        pole_radius = max(np.abs(poles))                                                                # Hvilke punkter skal plottes?
        ROC = 0
        print(Z_mag.shape)
        if roc_interval is not None: 
            ROC = np.array([[1 if Z_mag[i, j] > roc_interval[0] and Z_mag[i, j] < roc_interval[1] else 0 # Definer ud fra et interval
                            for i in range(n)] for j in range(n)])    
        else : 
            ROC = Z_mag < pole_radius if roc == 'indre' else Z_mag > pole_radius                        # |z| < a || |z| > a ud fra største pol. 
        
        # ? Plot
        fig, ax = plt.subplots(figsize=(6,6))
        ax.set_xlim([-r, r])
        ax.set_ylim([-r, r])

        # * Opsætning af koordinatsystem
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.grid(True, linestyle='dotted')
        ax.set_xlabel('$\mathscr{R}\{z\}$')
        ax.set_ylabel('$\mathscr{I}\{z\}$')
        ax.legend()
        unit_circle = plt.Circle((0, 0), 1, color=stil["Enhedscirklen"][0], fill= stil["Enhedscirklen"][5], alpha = stil["Enhedscirklen"][6]) #  linestyle='dashed')  # Enhedscirklen
        ax.add_patch(unit_circle)

        # * ROC
        ax.contourf(X, Y, ROC, levels=[0.5, 1]      , colors = [stil["ROC"][0]]  , alpha = stil["ROC"][6])                 # Udfyld            
        ROCcirkel = plt.Circle((0, 0), pole_radius  , color =  stil["ROC"][0]    , alpha = stil["ROC"][6], fill = False)   # Kanten 
        ax.add_patch(ROCcirkel)
        
        ax.scatter(np.real(zeros), np.imag(zeros), color = stil["Nulpunkter"][0], marker = stil["Nulpunkter"][1]  , label = stil["Nulpunkter"][2])  
        ax.scatter(np.real(poles), np.imag(poles), color = stil["Poler"][0]     , marker = stil["Poler"][1]       , label = stil["Poler"][2])
        
        # ? Text 
        # * Tilføjelse af ROC og enhedscirklen til legends. 
        handles, labels = ax.get_legend_handles_labels()
        handles.append(plt.Line2D([0], [0], marker="o", color = stil["ROC"][0]            , linestyle = "None"))    # ROC 
        handles.append(plt.Line2D([0], [0], marker="o", color = stil["Enhedscirklen"][0]  , linestyle = "None"))    # Enhedscirklen 
        labels.append(stil["ROC"][2])
        labels.append(stil["Enhedscirklen"][2])
        ax.legend(handles = handles, labels = labels)
        plt.title(stil["Titel"][2])
        plt.show()
        return fig, ax
        
        
            
                  
    
    
