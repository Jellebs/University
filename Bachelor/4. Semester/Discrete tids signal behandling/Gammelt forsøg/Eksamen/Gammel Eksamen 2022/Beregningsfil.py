from Uni.Formelsamling.Opgaver import * 
from sympy import * 
import matplotlib.pyplot as plt
import scipy.signal as sig
np.set_printoptions(suppress=True, precision = 2)

class Opgave1(Opgave): 
    hn = np.array([1, 4, -3])
    xn = np.array([2, 3])
    resultat_xnhn = xn[:, np.newaxis] * hn
    resultat_yn = sig.fftconvolve(xn, hn)

class Opgave2(Opgave): 
    w = Symbol("omega", real = True)
    z = Symbol("zeta", real = True)
    # w, z= symbols("omega, zeta", real = True)
    p = Symbol("p")
    eq1 = Eq(2*z*w + p, -0.914214)
    eq2 = Eq(w**2 + 2*z*w*p, 0.292893)
    eq3 = Eq(p*w**2, 0.5)
    omega = solve(eq1, w)[0]
    zeta = solve(eq3.subs(w, omega), z)[0]
    pol = solve(eq2.subs([(w, omega), (z, zeta)]))[0]
    pol = pol.subs(p, pol) # Jeg antager, at systemet er domineret af 2. orden, så nu ønsker jeg kun at finde for p er reel.
    zeta = zeta.subs(p, pol)
    omega = omega.subs([(z,zeta), (p, pol)])
    # zeta = zeta.subs(p, pol)
    # omega = omega.subs(z, zeta)
    resultat_sol3 = solve([eq1, eq2, eq3])
    resultat_symboler = f"\n{w} = {omega}\n{z} = {zeta}\n{p} = {pol}"

class Opgave3(Opgave): 
    b = [2, 1]
    a = [1, -1/2]
    A, p, C = sig.residuez(b, a)
    print(f"""
    A = {A}
    p = {p}
    C = {C}
    """)


reconstruction = lambda t, Ts, n, xn : np.dot(  np.sinc((t[:, None] - n*Ts)/Ts)    ,  xn   )  # Matrix vektor multiplikation,  A = (1000,  100),   xn = (100, 1),   så for hver tid(0, 1000) bliver xn vægtet med sin funktionerne, og summen findes. 
# Resultat bliver en (1000, 1) vektor. 

class Opgave4(Opgave): 
    nmax = 50
    Fs = 1000
    Ts = 1/Fs
    n_periods = 1
    t = np.linspace(-0.15, 0.15, 1000*n_periods)
    n = np.arange(-nmax*n_periods, (nmax + 1)*n_periods)
    
    xn = np.cos(1200*np.pi*Ts*n)
    xt_reconstrueret = reconstruction(t, Ts, n, xn)
    fig, ax = plt.subplots(figsize = (10, 6))
    xt = np.cos(1200*np.pi*t)
    ax.plot(t, xt, label ="Original funktion")
    ax.plot(t, xt_reconstrueret, label = "Reconstrueret funktion")
    ax.stem(n * Ts, xn, linefmt='r--', markerfmt='ro', basefmt='r-', label='Samples', use_line_collection=True)
    fig.legend()
    # plt.show()
    
WN = lambda N, inverse: np.exp(  
    (1 if inverse else -1)*2j*np.pi/N * (
        np.reshape(np.arange(N), (N, 1)) * np.arange(N) # k^N x 1 & n^1 x N, så får jeg kn som r^N x N 
    ))

class Opgave5(Opgave): 
    N = 4
    n = np.arange(N)
    k = np.reshape(n, (N, 1))
    resultat_W = np.exp((-2j*np.pi/N) * (k * n)) # k.N sørger for matrixen.
    xn = np.arange(3, -1, -1)
    resultat_Xk = WN(len(xn), False).dot(xn) # resultat_Xk = resultat_W.dot(xn)
    Yk = np.array([1, 1, 1, 1])
    resultat_yn = (1/len(Yk))*(WN(len(Yk), True).dot(Yk))
    resultat_ynNumpy = np.fft.ifft(Yk)

    

    
    
    




opg1 = Opgave1()
opg2 = Opgave2()
opg3 = Opgave3()
# opg4 = Opgave4()
opg5 = Opgave5()


