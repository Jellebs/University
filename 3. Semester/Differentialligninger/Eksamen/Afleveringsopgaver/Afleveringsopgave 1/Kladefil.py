from Formelsamling.Differentialligninger import makeDifferentialEquationPlots as diffPlot
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt 
from scipy.integrate import solve_ivp

def plot(x, y, label, flerePlots: bool = False):
    fig, ax = plt.subplots()
    ax.axvline(x=0, c="black")
    ax.axhline(y=0, c="black")
    if flerePlots: 
        for i in range(len(y)): 
            ax.plot(x, y[i], label = label[i])
        ax.legend()
        fig.savefig(f"{label}.pdf")
        plt.show()
        return

    ax.plot(x, y, label = label)
    ax.legend()
    fig.savefig(f"{label}.pdf")
    plt.show()

#                                   Eksamens opgave 1 
def problem1(): 
    # Opgave 1.2 
    x1 = np.linspace(-2, 2/3, 100)
    x2 = np.linspace(2/3, 2, 100) 
    K = -2 
    y1 = np.cbrt(1/(3*x1+K))
    y2 = np.cbrt(1/(3*x2+K))
    fig, ax = plt.subplots()
    ax.axvline(x=0, c="black")
    ax.axhline(y=0, c="black")
    ax.set_ylabel("y")
    ax.set_xlabel("x")
    ax.plot(x1, y1, label = "Løsning til y(1) = 1")
    ax.plot(x2, y2, label = "Løsning til y(1) = 1")
    ax.legend()
    fig.savefig("Løsning til y(1) = 1.pdf")
    plt.show()
    
    

def problem2(): 
    x = np.linspace(-5, 5, 40)
    def dydx(x, y): 
        return (4+y)*sp.sin(x)
    
    sol = solve_ivp(dydx, t_span=(min(x), max(x)), y0=[0], t_eval = x)
    C = 2.386294
    f = np.exp(-np.cos(x)+C) - 4
    labels = ["Løsning til y(0) = 0", "Beregnet funktion til y(0) = 0"]
    plot(x, [sol["y"][0], f], label= labels, flerePlots=True)


    y = sp.Function('y')
    x = sp.Symbol('x')
    # y' = (4+y)sin(x)
    eq = sp.Derivative(y(x), x) - ((4 + y(x))*sp.sin(x))
    result = sp.dsolve(eq, y(x))
    print(result)
    print(sp.checkodesol(eq, result))


def problem3():
    y = sp.Function('y')
    x = sp.Symbol('x')
    # y' = 2x - y
    eq = sp.exp(x)*2*x 
    sol = sp.integrate(eq)
    print(sol)
    diffEq = sp.Derivative(y(x), x) + y(x) - 2*x
    result = sp.dsolve(diffEq, y(x))
    print(result)

    # asymptomer 
    x = np.linspace(4, 6, 40)
    y = np.empty((2, len(x)))
    y[0] = 2*x -2 + 5/np.exp(x)
    # Kan funktionerne krydses? Test med y(-2)
    # y(-2) findes til at være C=4
    y[1] = 2*x -2+ 3/np.exp(x)
    plot(x, y, label = ["Problem 3 graf", "Test om grafen kan krydse"], flerePlots = True)


def problem4(): 
    x = np.linspace(-10, 10, 10)
    M = 4 
    a = 3
    ypos= M/(1+1*np.exp(-a*M*x))
    yneg= M/(1+(-0.5*np.exp(-a*M*x)))
    # plot(x, [yneg, ypos], label= ["Graf med C < 0, = -0.5", "Graf med C >= 0 = 1"], flerePlots=True)

    x = np.linspace(0, 4, 100)
    y0 = -3*x**2 + 12*x - 5
    y1 = -3*x**2 + 12*x - 15

    plot(x, [y0, y1], label=["Graf med h = 5", "Graf med h = 15"], flerePlots=True)


problem1()
