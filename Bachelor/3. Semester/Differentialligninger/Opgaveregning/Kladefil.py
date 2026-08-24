from sympy import *
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np
from Formelsamling.Differentialligninger import * 
from Formelsamling.Numerisk_Lineær_Algebra import skaler, skift, lægTil

def tidligereOpgaver():
    x = Symbol("x")
    fx = x*exp(-x)
    Fx = integrate(fx, x)
    print(Fx)

    ## Differential Equations
    # Standard form fra dydx + p(x)y = q(x)

    def dydx(x, y): # Aflever funktion 
        px = 1 
        qx = 2 
        return qx - px*y

    y0: list = list()
    for i in range(0, 20):
        y0.append(i)


    x = np.linspace(0, 1, 100)

    """ Er smidt ind i formelsamlingsmodulet.
    def makeDifferentialEquationPlots(dydx, y0, x): 
        sol = solve_ivp(dydx, t_span=(min(x), max(x)), y0=y0, t_eval = x)
        fig, ax = plt.subplots()
        for i in range(0, len(sol.y)): 
            ax.plot(x, sol.y[i], label = f"y0 = {i}")
        ax.legend()
        plt.show()  
    """
    def dydx(x, y): # Aflever funktion 
        # Standard form fra dydx + p(x)y = q(x)
        px = -1/2*y 
        qx = 1*x
        return qx - px*y

    x = np.linspace(-2, 2, 100)
    y0 = [i for i in range(-2, 2)]
    # makeDifferentialEquationPlots(dydx, y0 = y0, x=x, grid = True)
    # y = Symbol("y")
    # f = 1/sqrt(y)
    # F = integrate(f)
    # print(F)

    def dydx(x, y): 
        px = -2
        qx = 0
        return qx -px*sqrt(y) # y' = 2√y
    # makeDifferentialEquationPlots(dydx, y0 = y0, x = x, grid = True)
    # Den er ikke glad for kvadratrødder



    # Eksempel på klassen
    def dydx(x, y): 
        return y*(1-y)




    """  Den virker ikke, noget med x step size. Det er mærkeligt hvorfor den ikke bare virker. Nu plotter jeg den selv. 
    sol = solve_ivp(dydx, t_span = (min(x), max(x)), y0=y0, t_eval=x, first_step=1e-1, atol=1e-1)
    print(sol)
    makeDifferentialEquationPlots(dydx, y0, x, True)
    """


    """

    def funktionTilPlotForCvaerdier(y0:list, x: list, eq = "y0"): # Funktion til når der ønskes plots til mange forskellige startbetingelser.
        toRemove = list() # Liste til hvis der ingen løsninger findes til y0 værdien. Disse gemmes så de kan fjernes bagefter. 
        C = list()
        for i in range(len(y0)): 
            sol = solve(eq - y0[i], c) 
            if (len(sol) == 0): 
                print(f"Løsning kunne ikke findes ved indeks {i}. Fjerner element i y0")
                toRemove.append(y0[i])
            C = np.append(C, sol)

        for vaerdi in toRemove: 
            y0.remove(vaerdi)

        y = np.empty((len(C), len(x)))

        for i in range(len(C)): 
            funk = 1/(1+C[i]*np.exp(-x))
            y[i] = funk

        return y

    y0 = [2, 1, 1/2, 0, -1]
    x = np.linspace(-2, 2, 20)
    c = Symbol("c")
    eq = 1/(1 + c*1) # = y0

    y = funktionTilPlotForCvaerdier(y0, x, eq)
    print(y)
    fig, ax = plt.subplots()

    for i in range(len(y)): 
        ax.plot(x, y[i], label= f"y0 = {y0[i]}")
    ax.legend()
    #ax.set_ylim(-5, 5)
    plt.show()
    """





    #                       Eulers metode. (Har ændret den i formelsamlingsmappen)
    def EulersMetode(dydx, startY, h, x): 
        y = np.empty((len(x)))
        y[0] = startY
        for i in range(0, len(x)-1): 
            y[i+1] = y[i] + h*dydx(x[i], y[i])
        return y

    x = np.linspace(-2, 2, 25)
    y = np.empty((3, len(x)))

    # Differentialligninger løst
    funktioner = np.empty((3, len(x)))
    funktioner[0] = np.exp(1/2*x)
    funktioner[1] = 0.5*x 
    funktioner[2] = 1/4 * (x**2)

    def dydx(x, y): 
        return 1/2*y
    y[0] = EulersMetode(dydx, 1, 0.0005, x)

    def dydx(x, y):
        return 1/2
    y[1] = EulersMetode(dydx, 1, 0.01, x)

    def dydx(x, y): 
        return 1/2*x
    y[2] = EulersMetode(dydx, 1, 0.01, x)

    fig, ax = plt.subplots()

    for i in range(len(y)): 
        ax.plot(x, funktioner[i], 'o', label= f"Eksakt funktion {i+1}", ) 
        ax.plot(x, y[i], label = f"Approksimation til funktion {i+1}")
    ax.legend()
    plt.show()


def opgaver2_4(): 
    def opgave2_4_27(): 
        y0 = 0 #, hvad er y(2) ? 
        def dydx(x, y): 
            return x**2 + y**2 - 1
        x_interval = (0, 2)
        punkter = (EulersMetode(dydx=dydx, y0=y0, h=0.1, xInterval = x_interval),
                EulersMetode(dydx=dydx, y0=y0, h=0.01, xInterval = x_interval),
                EulersMetode(dydx=dydx, y0=y0, h=0.001, xInterval = x_interval))
        fig, ax = plotStandardInstillinger()
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        labels = ["Eulers approksimation til h = 0.1", "Eulers approksimation til h = 0.01", "Eulers approksimation til h = 0.001"]
        
        for i in range(len(punkter)):
            x = punkter[i][:, 0]
            y = punkter[i][:, 1]
            ax.plot(x, y, label = labels[i])
        fig.legend()
        fig.savefig("Opgave 2_4_27.pdf")
        plt.show()
        
    # opgave2_4_27()
    def opgave2_4_29():
        def dydx(x, y): 
            return -y/(7*x)
        h = 0.1501 
        xInterval = -1, 0.5 
        y0 = -1 
        punkter = EulersMetode(dydx, y0, h, xInterval)[:]
        x = punkter[:, 0] 
        y = punkter[:, 1]
        # plot(x, y, label="Opgave 2_4_29")

        def opgaveC(): 
            punkter = (EulersMetode(dydx, y0, h, xInterval), 
                       EulersMetode(dydx, y0, 0.031, xInterval),
                       EulersMetode(dydx, y0, 0.006031251199, xInterval))
            labels = ["Oprindelig approksimation", "h = 0,03 approksimation", "h = 0,006 approksimation"]
            fig, ax = plt.subplots()
            for i in range(0, len(punkter)): 
                x = punkter[i][:, 0]
                y = punkter[i][:, 1]
                ax.plot(x, y, label = labels[i])
            fig.legend()
            fig.savefig("Original approksimation + 2 forbedrede.pdf")
            plt
            # plot(x, y, labels, True)
            # print(np.shape(x))
            # y = (punkter[0][:, 1], punkter[1][:, 1])
            # plot(x, y, labels, True)
            # for i in range(0, len(punkter)): 
                

            """
            def traekPunktUd(x, h): 
                for vaerdi in x:
                    
                    if vaerdi 
                if punkter
                indekser
            """    

            
        opgaveC()
        
    opgave2_4_29()


def opgaver3_3():
    def printRoedder(roedder): 
        for loesning in roedder: 
            pprint(N(loesning))
    r = symbols("r")
    def opgave12():
        eq = r**3 -3*(r**2) + r - 1
        pprint(factor(eq))
        print("\n")
        roedder = roots(eq)
        for loesning in roedder: 
            pprint(N(loesning))
    def opgave23(): 
        eq = r**2 -6*r + + 25
        printRoedder(roots(eq))

    def opgave24(): 
        eq = r**2 - (3/2)*r - 1
        printRoedder(roots(eq))
        # koefficienter. 

        ligning = np.array([
            [1,    1, 1,  1], 
            [0, -1/2, 2, -1], 
            [0, -1/4, 4,  3]
            ])
        skaler(ligning, -2, 1)
        lægTil(ligning, 2, 1/4, 1)
        skaler(ligning, 1/3, 2)
        lægTil(ligning, 1, 4, 2)
        lægTil(ligning, 0, -1, 2)
        lægTil(ligning, 0, -1, 1)
        print(ligning)
        




    opgave24()

def opgaver3_6(): 
    def plotAfOscFunktioner(funktioner, t, labels):
        fig, ax = plt.subplots()
        ax.axhline()
        ax.axvline() 
        ax.set_ylabel("x")
        ax.set_xlabel("t")      
        for i in range(len(funktioner)): 
            ax.plot(t, funktioner[i], label = labels[i])
        ax.legend()
        plt.show()
    t = np.linspace(-np.pi, np.pi, 100)
    x_c = -10/13 * np.cos(3*t)
    x_p = 10/13 * np.cos(2*t)
    labels = ["x_c", "x_p"]
    plotAfOscFunktioner([x_c, x_p], t, labels)

    
# opgaver3_6() 
def opgaveNoget(): 

    A = np.array([
        [ 1,  0,  0], 
        [-2, -2, -3], 
        [ 2,  3,  4]])

    v = np.linalg.eig(A).eigenvectors


    A = np.array([
        [3, -1], 
        [1,  1]])

    egenvaerdier = np.linalg.eig(A)
    Lambda = egenvaerdier.eigenvalues
    v = egenvaerdier.eigenvectors
    print(Lambda)

    LambdaI = np.eye(2)*Lambda
    print(A - LambdaI)
    LambdaIiAnden = (A - LambdaI) @ (A - LambdaI)
    print(LambdaIiAnden)
    print(v[0])


    # print(v[1].dot(LambdaIiAnden))


    # for i in range(len(v)): 
    #   print(f"v{i} = {v[i]}\n")




# Øvelse på klassen 
# Partikulær løsning ud fra koefficient matrix.
def koefficient(): 
    A = Matrix([[-2,  1], 
                [ 2, -3]])
    c1, c2, c3, c4, t = symbols("c1 c2 c3 c4 t")

    y_partikulær = Matrix([
        [c1*exp(4*t) + c2*exp(t)], 
        [c3*exp(4*t) + c4*exp(t)]])
    diff_y_partikulær = diff(y_partikulær, (t, 1))
    #pprint(diff_y_partikulær)
    f_t = Matrix([2*exp(4*t), exp(t)])
    # pprint(A @ y_partikulær)

    

    hoejreSide = A @ y_partikulær + f_t
    venstreSide = diff_y_partikulær
    eq = hoejreSide - venstreSide
    pprint(eq)
    pprint(solve(eq, [c1, c2, c3, c4])) # = 0 


# koefficient()
def opgave5_2(): 
    # Opgave 3
    A = np.array([[3, 4],
                [3, 2]])
    def findX(A):
        eig = np.linalg.eig(A)
        vaerdier = eig.eigenvalues
        vektor = eig.eigenvectors
        c1, c2, t = symbols("c1 c2 t")
        x = Matrix([
            [c1 * vektor[0] * exp(vaerdier[0]*t)],
            [c2 * vektor[1] * exp(vaerdier[1]*t)]])
        # pprint(vaerdier)
        x1 = c1 * vektor[0] * exp(vaerdier[0]*t)
        pprint(vektor)
        pprint(x1)
        # pprint(vektor[1])
        # pprint(x.shape)
        # pprint(x)
        return x
    # x = findX(A)
    # pprint(x)

    # Opgave 11
    A = np.array([[1, -2], 
                  [2,  1]])
    x = findX(A)
    
    
    # pprint(x)


    


opgave5_2()
