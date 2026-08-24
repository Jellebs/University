import numpy as np
import matplotlib.pyplot as plt 
def plot(ax, x, y , T, funktionLabel, xlabel = "", ylabel = "", colors = ""): 
    ax.set_xlabel = xlabel
    ax.set_ylabel = ylabel
    c = next(colors)["color"] if type(colors) != str else "blue"
    ax.plot(x, y, label = funktionLabel, color = c)
    ax.grid(True)

def opgave1(): 
    # Generate and plot the following signals in Section 2.1 for -20 ≤ n ≤ 40
    T = (-20, 40)
    n = np.linspace(T[0], T[1], (T[1] - T[0]) + 1) # ex 40 - -20 + 1 = 61, en sample pr enhed. 
    fig = plt.figure(figsize=(16,8))
    ax = fig.subplots(nrows=4, sharex= True)
    

    # a b c & e 
    def foersteDel(): 
        
        # a. as a unit sample 
        gamma = (n == 0).astype(float)
        ax[0].stem(n, gamma, label="gamma[n]")
        
        # b. as a unit step
        u = (n == 0).astype(float) + (n > 0).astype(float)
        plot(ax[1], n, u, T, "u[n]",)

        # c. real exponential signal 
        rexp = 0.8**n
        plot(ax[2], n, rexp, T, "0,80^n")
        
        # e. sinusoidal sequence 
        sinus = 2*np.cos(2*np.pi*0.3*n + np.pi/3)
        plot(ax[3], n, sinus, T, "harmonisk[n]")
        
        fig.text(0.5, 0.04, 'n', ha='center', va='center')
        fig.text(0.06, 0.5, 'y[n]', ha='center', va='center', rotation='vertical')
        fig.legend()
        fig.savefig("Opgave 2.1.(a, b, c, e).pdf")
    
    
    def andenDel(): 
        colors = plt.rcParams["axes.prop_cycle"]() # Liste med de næste farver som matplotlib har klar til en
        fig.text(0.5, 0.925, "Opgave d", ha= "center", va= "center", size = 30)
        fig.text(0.5, 0.04, 'n', ha='center', va='center')
        # d. complext exponential signal
        cexp = (0.9*np.exp(1j*np.pi / 10))**n
        # plot cexp.a 
        plot(ax[0], n, cexp.real, T, "a", colors = colors)

        # plot cexp.b 
        plot(ax[1], n, cexp.imag, T, "b", colors = colors)

        # plot |cexp| 
        plot(ax[2], n, abs(cexp), T, "|cexp|", colors = colors)

        # plot vinklen(cexp)
        # vinkel = np.arctan(cexp.imag/cexp.real) # trigonometri tan(A) = y/x
        plot(ax[3], n, np.angle(cexp), T, "‹cexp")
        # plot(fig, ax, n, cexp, T, "(0.9 * e^(jπ/10))^n ")
        fig.legend()
        fig.savefig("Opgave 2.1.d.pdf")
    andenDel()
    plt.show()

def opgave2(): 
    # Opgaven
    xtiln = [5, 4, 3, 2, 1] # For relativt x[0], x[1], ... x[4]
    # Consider a sequence x[2 - n] = x[-(n-2)]
    step = lambda amp, t, condition: amp * (condition).astype(float) * t

    # a. Let y1[n] be obtained by folding x[n] and then shifting the result to the right by two samples. Determine and plot y1[n]
    rampSignal = lambda t, x0 : (t > 0).astype(float) * (4 - 5)/(1 - 0) * t + step(5, t, t >= 0)  # 5*u[t] - 1*r[t]
    # Så kan jeg konstruere x[n] igen
    t = np.arange(-6, 6, 0.01)
    xtiln = rampSignal(t, 5)
    print(xtiln)
    # Hvis jeg så skal "folde den", som jeg har fundet ud af, er deres måde at sige vende tiden på, så får jeg at
    ts = -t 
    ytiln = rampSignal(ts,  5)
    # Som var svaret hvis jeg kun skulle spejle signalet, men her skal jeg også shifte den. 
    tsm = ts + 2 # Shiftet og spejlet
    
    # ytiln = rampSignal(tsm, 5)
    # print(tsm, ytiln)
    # print(xtiln, ytiln)
    fig = plt.figure()
    ax = fig.subplots(1)
    ax.set_xlim(-4, 4)
    ax.set_ylim(-1, 6)
    ax.vlines(0, -1, 6, "black")
    ax.plot(t, xtiln, label = "x[n]")
    # ax.plot(tsm, ytiln, label = "y[n]")
    fig.legend()
    plt.show()

    """
    T = (-6, 4)
    
    ax.hlines(y=0, xmin = T[0], xmax = T[1], linewidth=2, color='black')
    ax.vlines(x=0, ymin = 0, ymax = 5, linewidth=2, color='black')
    colors = plt.rcParams["axes.prop_cycle"]() # Liste med de næste farver som matplotlib har klar til en    
    
    n = np.linspace(T[0], T[1], T[1] - T[0] + 1)
    ytiln = [1, 2, 3, 4, 5]
    plot(ax, n[6:11], xtiln, T, "x[n]", colors = colors)
    plot(ax, n[0:5], ytiln, T, "y[n]", colors = colors)
    fig.legend()
    fig.savefig("Opgave 2.2.a.pdf")
    
    # b. 
    """


opgave2()