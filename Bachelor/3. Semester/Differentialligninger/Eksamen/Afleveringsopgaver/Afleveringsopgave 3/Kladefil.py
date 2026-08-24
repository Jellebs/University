from sympy import *
import numpy as np
from Formelsamling.Differentialligninger import plots
def printSvar(listeAfTing, listeNavne):
    print("="*80)
    max = len(listeAfTing)
    for i in range(max): 
        print(f"{listeNavne[i]}")
        for ting in listeAfTing[i]: 
            pprint(ting)
        if i == max - 1: 
            continue
        print("\n\n")
    print("="*80)

def opgave1(): 
    x, t = symbols("x t", positive = True)
    ft = symbols("ft")

    eq = x - x**3 
    sol = roots(eq, x)
    printSvar([factor(sol)], ["roedder"])

opgave1()
def opgave2(): 
    t = symbols("t")
    A = Matrix([[1,  2], 
                [2, -2]])
    ft = Matrix([[10*t],
                [   5]])
    x0 = Matrix([[0], 
                 [0]])
    # Exponetial af en matrix 
    def delopgaveA(): 
        def approksimer(A, t, n): 
            approksimation = Matrix([[1, 0],
                                    [0, 1]])
            for i in range(1, n): 
                approksimation += 1/(factorial(n)) * (A**n * t**2)
            return approksimation

        
        approksimation = approksimer(A, t, 4)
        pprint(approksimation)
        print("Approksimationen af e^(At)\n \n")

        eAt = exp(A*t)
        pprint(eAt)
        print("Pythons eksponentiel til matrix funktion")
    
    fundMatrix = Matrix([[ 1 * exp(-3*t),   1 * exp(2*t)], 
                         [-2 * exp(-3*t), 1/2 * exp(2*t)]])
    
    def delopgaveB():
        mat = fundMatrix
        matInv = mat.inv()
        loesning = mat @ matInv@x0 + (mat @ (integrate(matInv @ ft, (t))))
        pprint(mat @ matInv@x0)
        return loesning
    xt = delopgaveB()
    pprint(xt)


def opgave3():
    A = np.array([[ 1,  0,  0], 
                  [ 1,  3,  1],
                  [-2, -4, -1]], dtype= float)
    def delopgaveA(): 
        lamb, v = np.linalg.eig(A)
        v = [v[:, i] for i in range(0, 3)]
        printSvar([lamb, v], ["Egenværdier", "Egenvektorer"])
        
        lamb = symbols("lambda")
        # pprint(roots(det(A - lamb*eye(3))))

        Alam = A - 1*np.eye(3)
        nul = np.array([0, 0, 0], dtype= float)[:, np.newaxis]
        # v = np.linalg.solve(Alam, nul)
        pprint([A, nul])

    def delopgaveB(): 
        t = symbols("t")
        Asym = Matrix(A)
        Asym.rref()
        x0 = Matrix([[1], 
                     [0],
                     [0]])
        fundMatrix = Matrix([[0.2672*exp(t), 0.2672*exp(t)*t, 0.2672*exp(t)*(t**2)],
                             [0.5345*exp(t), 0.5345*exp(t)*t, 0.5345*exp(t)*(t**2)],
                             [0.8018*exp(t), 0.8018*exp(t)*t, 0.8018*exp(t)*(t**2)]])
        eAt = (Asym*t).exp()
        xt = eAt @ x0
        pprint(xt)

def opgave4(): 
    def delopgave2():
        def JacobianEigs(x, y): 
            J = np.array([[-4 + 30,        -y], 
                        [    2*y, -8*y + 20]])
            eig = np.linalg.eig(J)
            return eig
        kritiskePunkter = np.array([[10, 10],
                                    [15,  0], 
                                    [ 0,  0]])
        egenvaerdier = []
        egenvektor = []
        for punkt in kritiskePunkter: 
            lamb, v = JacobianEigs(punkt[0], punkt[1])
            v = [v[:,i] for i in range(len(v))]
            egenvaerdier += [f"x, y = {punkt} => {lamb}"]
            
            egenvektor +=  [f"x, y = {punkt} => {v}"]

        printSvar([egenvaerdier, egenvektor], ["Egenværdier", "Egenvektor"])
        
    def delopgave4(): 
        def dxdt(x, t): 
            return [30*x[0]-2*(x[0]**2)-x[0]*x[1],   20*x[1]-4*(x[1]**2)+2*x[0]*x[1]]
        x1 = np.linspace(-1, 11, 50)
        x2 = np.linspace(-1, 11, 50)
        initialState = (0.1, 0.1)
        t = np.linspace(0, 50, 1000) # Lad mig på et linjestykke med startværdien (x1_0, x2_0) fra tiden 0 til tiden 50.
        plots.phasePortraitPython(dxdt, x1, x2, t, initialState)
    delopgave4()
    
# opgave4()