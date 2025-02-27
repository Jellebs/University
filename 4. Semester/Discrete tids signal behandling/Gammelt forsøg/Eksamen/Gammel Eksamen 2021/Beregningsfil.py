from Uni.Formelsamling.Opgaver import *
import scipy.signal as sig


class Opgave1(Opgave):
    xn = np.array([1, 3, 2])
    hn = np.array([4, -5])
    resultat_xnThn = xn[:, np.newaxis] * hn
    resultat_yn = sig.convolve(xn, hn)
    



opg1 = Opgave1()