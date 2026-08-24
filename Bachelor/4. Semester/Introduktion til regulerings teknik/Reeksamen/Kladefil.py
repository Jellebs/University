import scipy.signal as sig
import numpy as np 
from sympy import * 
import matplotlib.pyplot as plt
from Formelsamling.KontrolSystemer import AndenOrdensSystemer 



def ekstra(): 
    b, a = ([177830, 0, 0], [1, 170, 6000, 0])
    r, p, k = sig.residue(b, a)
    print(r, p, k)
    s = symbols("s")
    eq = sum([r[i]/(s - p[i]) for i in range(max(len(r), len(p)))])
    pprint(eq)

def opgave1(): 
    fig, ax = plt.subplots()
    zet = np.arange(0, 1, 0.10)
    omega = 170/zet
    OS = lambda zet : np.exp(-np.pi*zet/(np.sqrt(1-zet**2)))
    graense = 20*np.ones_like(zet)
    ax.plot(zet, 100 * OS(zet), label= "OS")
    ax.plot(zet, graense, label = "Graense valgt")
    ax.grid(True)
    ax.set_ylabel("Oversving Mp i %")
    ax.set_xlabel("Daempningskoefficient zeta")
    plt.legend()
    plt.show()

def ekstra2(): 
    fig, ax = plt.subplots()
    phi = np.arange(0, np.pi + np.pi/16, np.pi/16)
    phaseStoerrelse = (1 - np.sin(phi))/(1 + np.sin(phi))
    ax.plot(phi, phaseStoerrelse)



def ekstraOpgave6(): 
    fig, ax = plt.subplots()
    zet = np.arange(0, 1, 0.10)
    OS = lambda zet : np.exp(-np.pi*zet/(np.sqrt(1-zet**2)))
    graense = 15*np.ones_like(zet)
    ax.plot(zet, OS(zet), label= "OS")
    ax.plot(zet, graense, label = "Graense valgt")
    ax.grid(True)
    G = lambda s: 7.943282*3000/((s+5)*(s+10)*(s+50))
    pprint(G(19.4j))

# ekstraOpgave6()
system = AndenOrdensSystemer()
# system.OSPMPlot(15)
# system.lead().alphaPlot()

s, A = symbols("s A")
G = (5 * 1/(s + 5))
H = 1/(s+10)
GH = G/(1 + G*H)
pprint(simplify(GH))
pprint((A - 0.01)/(0.01))
