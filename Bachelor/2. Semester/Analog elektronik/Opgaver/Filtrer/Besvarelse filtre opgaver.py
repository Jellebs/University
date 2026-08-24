from Formelsamling.Elektriske_Kredsløb import *
from sympy import * 
import numpy as np 
def opgave17_3():
    # Opgave 17.3
    # A filter has the transfer function 
    #   T(s) = 1/((s + 1 )(s^2 + s + 1)). 
    # Show that |T| = √(1 + w^6) and find an expression for its phase response Phi(w). 
    # Calculate the values of |T| and Phi for w = 0.1, 1 and 10 rad/s
    #    and then find the output corresponding to each of the following input signals 
    #       10sin(0.1t) (volts)
    #       10sin(t)    (volts)
    #       10sin(10t)  (volts)

    count = 20
    s = symbols("s")
    f = np.logspace(-1, 1, count)
    w = f # rad/s, ikke Hz

    s = 1.0j*w
    T = 1/((s + 1)*(s**2 + s + 1)) # Transfer funktion

    def Opgave_17_3_isEqual(T, w): 
        
        T_abs = np.sqrt(1 + w**6) # |T| 
        print(f"T = 1/((s + 1 )(s^2 + s + 1)), |T| funktion = √(1 + w^6)")
        for i in range(0, len(T)): 
            print(f"T = {np.abs(T[i])}, |T| funktion = {T_abs[i]}")

    # Opgave_17_3_isEqual(T, w) 

    # Lad mig finde Phi(w)
    # Der bliver godt nok skrevet Phi(w), men vinklen for noget reelt vil være 0, da Phi(w) = Tan^-1(w.imag/w.reel) = Tan^-1(0/w.reel)
    # Der må være tale om en fejl. 
    # Phi(s) findes, hvor s = jw. 

    # T = 1/((s + 1)*(s**2 + s + 1))
    """s = Symbol("s")
    T = apart(1/((s + 1)* (s**2 + s + 1))) # normal form til ratinal fraction brøkopsplitning


    print(T)
    """
    # T = 1/(s**3 + 2*s**2 + 2*s + 1)
    # (jw)^3 = (-1*w^3)*1j
    # 2(jw)^2 = -1*2*w**2 
    # 2(jw) = 2*w*1j
    # 1 = 1
    # Phi = 0 - np.arctan( imag/real )

    # Phi = 0 - np.arctan((np.sqrt((w.real**3)**2 + (w.imag**3)**2) + 2*w) / (2*w**2 - 1))

    Phi = 0 - np.arctan2(s.imag, s.real + 1) - np.arctan2((s**2 + s).imag, (s**2+s).real + 1)
    angle = np.angle(T)
    db_mag = 20*np.log10(np.abs(T))
    # filter_bodePlot(db_mag, "db_mag", f, save=True)
    # filter_bodePlot(Phi, "Phi", f, save=True)

    svar = """
    T in [0: 1]
    |T| funktion in [1: ∞] 
    Så jeg ser ikke, hvordan funktionerne kan være ens

    phi(s) = 0 - tan^-1((√{(w.real**3)**2 + (w.imag**3)**2 + 2*w} / (2*w**2 - 1))
    """



# Opgave 17.4 - For the filter whose magnitude response is sketched ( as the blue curve ) in Fig. 17.3,
#   find |T| at w = 0, w = w_p and w = w_s. A_max = 0.2dB, and A_min = 60dB
#  
# Dette er et lavpass filter. 
# Til w = 0 er gainet i 0. 
# Så |T|(w = 0) = 0
# til w = w_p er gainet i den største mulige variation i passbåndet som er A_max.
# Så |T|(w = w_p) = 0 - A_max = 0 - 0.2dB = -0.2dB 
# Til w = w_s er gainet i den mindst mulige flytning fra gaintoppen som er 0 - A_min. 
# Så |T|(w = w_s) = 0 - A_min = 0 - 60dB = -60dB

def opgave17_14(): 
    # Opgave 17.14 - Analyze the RLC network of Fig. P17.14 to determine its transfer function V_O(s)/V_i(s) and hence its poles and zeros.
    #   Hint: Begin the analysis at the output and work your way back to the input, eller som jeg vil have kaldt det, lookback metoden.
    R, ZR1sym, C, Vo, Vi, VA, VB, s = symbols("R ZR1 C Vo Vi VA VB s")
    Zeq = 1/(1 + ZR1sym + C*s)
    ZR1 = 2*s + 1/(1/1 + 1*s) # 2H i serie med 1 Ohm parallelt med 1F 
    ZRTH = Zeq.subs(ZR1sym, ZR1)
    # Så er thevenin modstanden fundet 

    # For at finde VTH bruges knudepunktsanalyse.
    ZC1, ZC2, ZL1, R1, R2 = symbols("ZC1 ZC2 ZL1 R1 R2")
    A = Eq(Vi/R1 - VA/ZC1 - (VA - VB)/ZL1, 0) # Vi/(1 Ohm) - VA/1F - (VA - VB)/2H = 0 
    B = Eq((VA - VB)/ZL1 - VB/ZC2 - VB/R2, 0) # (VA - VB)/ZL1 - VB/ZC2 - VB/R2 = 0 

    """
    ZC1 = 1/(1*s)
    ZC2 = ZC1 
    ZL1 = 2*s 
    R1 = 1
    R2 = R1
    """
    A = A.subs([(R1, 1),(ZC1, 1/(1*s)), (ZL1, 2*s)])
    B = B.subs([(ZL1, 2*s), (ZC2, 1/(1*s)), (R2, 1)])

    sol = solve([A, B], [VA, VB], dict = True)  
    VA = sol[0][VA]
    VB = sol[0][VB]
    # VB er knudepunktet som outputtet ser som det høje potentiale. 
    VTH = VB 
    Vo = VTH
    T = Vo/Vi
    """
            1          
    ─────────────────────
    3      2          
    2⋅s  + 2⋅s  + 2⋅s + 1
    """
    # Hvor skal jeg forvente, at polerne findes? 
    f = np.logspace(-1, 1, 50)
    w = f
    s = 1.0j*w

    T = 1/(2*s**3 + 2*s**2 + 2*s + 1)
    # Der er kun 1 pol her, det er når
    # 2*s**3 + 2*s**2 + 2*s == 1
    Tdb = 20*np.log10(np.abs(T))

    # filter_bodePlot(Tdb, "3 ordens filter", f)

    dmp = filter_daempelsesRatio(1, 2*Symbol("s"))
    Tdb = 20*np.log10(np.abs(T))

    svar = f"""
    Transfer funktionen er fundet til at være: 
    T = 1/(2*s**3 + 2*s**2 + 2*s + 1)
    og en pol ved 2*s**3 + 2*s**2 + 2*s = 1 

    Som lidt ekstra har jeg prøvet at finde dæmpelsesratioen, da dette er et komplekst filter
    dmp = {dmp}, hvilket ikke er helt korrekt, det ligner mere end dmp på 0.2.
    dmp'en er fundet ud fra et eksempel fra en anden ordens filter, men det her er et 3 ordens filter. 
    Det kan være, at det er derfor den afviger.
    """
    opgaveBesvarelse("Opgave 17.14", svar)


def opgave17_27(): 
    # Opgave 17.27 - Derive an expression for the transfer function of the op amp-RC circuit that is shown in Fig 17.13(c). 
    #                Give expressions for the frequency of the transmission zero w_z, the frequency of the pole w_p,
    #                the dc gain, and the high-frequency gain.
    ZR1, ZR2 = symbols("ZR1 ZR2")
    T = - ZR2/ZR1

    C1, C2, R1, R2, s = symbols("C1 C2 R1 R2 s")
    T = T.subs([(ZR1, 1/(1/R1 + C1*s)), (ZR2, 1/(1/R2 + C2*s))])
    """
    ⎛       1 ⎞ 
    -⎜C₁⋅s + ──⎟ 
    ⎝       R₁⎠ 
    ─────────────
            1   
    C₂⋅s + ──  
            R₂  
    """                                                                                                                  
    T = -(C1*s + 1/R1)/(C2*s + 1/R2)
    # Lidt omskrivning:
    T = -(C1/C2*s + 1/(R1*C2))/(s + 1/(R2*C2))
    T = (-C1/C2*s + (-1)/(R1*C2))/(s + 1/(R2*C2))
    # Så ligner det den generalle formel: 
    # T(s)= (a1s + a0)/(s + w0)
    # Hvor 
    # a1 = (-C1/C2)
    # a0 = (-1)/(R1*C2))
    # & w0 = 1/(R2+C2)
    def T(frequency): 
        s = Symbol("s")
        T = (-C1/C2*s + (-1)/(R1*C2))/(s + 1/(R2*C2))
        gain = T.subs(s, frequency)
        pprint(gain)

    T(0) # = T(wz) = -R2/R1 = DC Gain
    # Dette er et første ordens filter, wp må kunne findes ved DC gain -3dB

    eq = (20*log(-R2/R1, 10) - 3, (-C1/C2*s + (-1)/(R1*C2))/(s + 1/(R2*C2)))
    # pprint(solve(eq, Symbol("s")))
    """
    cutoff frekvensen findes ved
        -1  
    s: ─────
    C₁⋅R₁
    """
    wp = -1/C1*R1

    svar = """
    Overførsels funktionen udledes til at være: 
    ===================================================
    
        C₁⋅s     1  
        - ──── - ─────
        C₂    C₂⋅R₁
    T = ──────────────
                1     
        s + ─────   
            C₂⋅R₂ 

    # Som følger den generalle lignings form.

    wz mangler       

    TdB(wp) = DC Gain dB - 3dB = 20*log(-R2/R1, 10) - 3
    => 
        -1  
    wp = ─────
        C₁⋅R₁

            -R₂ 
    DC Gain = ────
            R₁ 

            -C₁ 
    HF Gain = ────
            C₂
    ===================================================
    """
    opgaveBesvarelse("Opgave 17.27", svar)

def opgave17_38(): 
    # Opgave 17.38 
    #   a.  Show that |T| of a second-order bandpass function 
    #       is geometrically symmetrical around the center frequency w0.
    #       That is, the members of each pair of frequencies w1 and w2 for which |T(jw1)| = |T(jw2) 
    #       are related by w1w2 = w0^2 
    # Med w1 og w2 bliver også kaldt wclp & wchp for cutoff frekvens ved høj og lav frekvens i en båndpass / båndstop filtre
    # På standard form for anden ordens kan polerne findes ved. 
    w0, Quality, s = symbols("w0, Q s")
    poler = s**2 + (w0/Quality)*s + w0**2
    sol = solve(poler, s)
    """
                        __________     
                       /        2      
                 ±w0*╲╱  1 - 4⋅Q   - w0 
    wp1, wp2 =  ────────────────────────
                        2⋅Q     
    hvor -w0*... ses som det højeste og +w0*... som det laveste, da kvadratroden højest sandsynligt giver noget komplekst.
    
    da er wp1 >> w0 >> wp2 
    Lad os give det et forsøg. 
    w0 = 1000
    Q = 40      
    """
    sol = solve(poler.subs([(w0, 1000), (Quality, 40)]), s)
    """
      25   225⋅(√79)j  
    - ── + ─────────,
      2        2   
    """
    print(np.abs(sol[0]))
    print(np.abs(sol[1])) # == 1000, det virker mærkeligt.
    # Lad os tage det matematisk i stedet for. 
    # Ved en pol ændres hældningen med -20dB/decade. 
    # polerne ved et båndpass fåes af et andengrads polynomie, som er symmetrisk omkring toppunktet, her er det w0 
    # Gainet vil da være det samme ved w1 som ved w2.
    # hvis w1 = w0 - h, w2 = w0 + h,
    # så w1*w2 = (w0 - h)(w0 + h) 
    #          = w0^2 + w0h - hw0 -h^2
    #          = w0^2 - h^2
    # Den eneste måde dette er muligt, er hvis w1 = w0 = w2. 
    # For løsningen fundet ovenfor, som synes mærkeligt, giver det nu mening. 
    # Et båndpass filters poler kan gå så tæt på hinanden, at de praktisk talt er w0. 
    # Min regnemetode er måske ikke helt korrekt, da venstre side h nødvendigvis ikke er det samme som højre side h, da skalaen er logaritmisk
    #
    # Rettelse wp1, wp2 er ikke det samme som w1, w2 som er cutoff frekvenserne. 


    #   b.  Find the transfer function of the second-order bandpass filter that meets specifications of the form in Fig 17.4 where 
    #       wp1 = 8100 rad/s, 
    #       wp2 = 10000 rad/s, 
    #       A_max = 3dB. If ws1 = 3000rad/s 
    #       find A_min & ws2
    a0, a1, a2 = symbols("a0 a1 a2")
    T = (a2*s**2 + a1*s + a0)/(s**2 + (w0/Quality)*s + w0**2)




# opgave17_3()
# opgave17_14()
# opgave17_27()

opgave17_38()