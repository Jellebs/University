from Uni.Formelsamling.SignalerOgSystemer import diskretTid
from scipy.signal import * 
from sympy import * 
def opgave3_1(): 
    taeller = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1/(2**10)] # 1 - 1/2^n * z^-10 
    naevner = [1, -1/2]

    diskretTid.zplane(taeller, naevner, "Opg3_1_a.pdf")

def opgave3_4(): # Partial fraction expansion
    # opgave a. 
    # a = 1*1 + 1*2z^-1 -z^-1 -z^-1*2z^-1 = 1 + z^-1 -2z^-2 
    def lavLigning(A, p, om_beregning = False): 
        xn = 0  
        x, n = symbols("x n")
        indstillinger = "Afrundet til 3 decimaler" 
        for k in range(len(A)): # Formel 3.28
            xn = Eq(Function(x)(n), N(float(A[k])*(float(p[k]) ** n), 3) * Heaviside(n))
        return (xn, indstillinger) if om_beregning == True else xn
    
    xn = []
    a = [1, 1, -2]
    b = [1, 1/3]
    A, p, C = residuez(b, a) 
    #            0,444        0,555   
    # X(Z) ==  ---------- + ------------
    #          1 - 1*z^-1   1 -(-2)*z^-1
    xn.append(lavLigning(A, p)) 
    # x[n] ==  0,444u[n] + 0,555*(-2)^n*u[n]
    
    
    # Opgave b. 
    a = [1, -1/4]
    b = [1, -1]
    A, p, C = residuez(b, a)
    #              -3     
    # X(Z) ==  ----------       + 4z^-0 
    #          1 - 1/4*z^-1 
    xn.append(lavLigning(A, p)) 
    # x[n] ==  -3 * (1/4)^n * u[n] 

    # Opgave c. 
    # a = 1 * 1 - 1*1/4z^-1 - 1/2z^-1 + 1/2z^-1*1/4z^-1 
    # a = 1 - 3/4z^-1 + 1/8z^-2 
    a = [1, -3/4, 1/8]
    b = [1]
    A, p, C = residuez(b, a)
    #               -1              2   
    # X(Z) ==  ------------ + ------------
    #          1 - 1/4*z^-1   1 - 1/2*z^-1
    xn.append(lavLigning(A, p)) 
    # x[n] ==  -1 * (1/4)^n * u[n] +  2 * (1/2)^n * u[n]
    
    pprint("="*25)
    for i in range(len(xn)): pprint(xn[i])
    pprint("="*25)
    

def opgave3_6():
    print("")

    
opgave3_4()