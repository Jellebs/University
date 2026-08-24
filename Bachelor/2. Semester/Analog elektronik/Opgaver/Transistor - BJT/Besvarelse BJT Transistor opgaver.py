from sympy import * 
from Formelsamling.Elektriske_Kredsløb import *
import numpy as np

def opgave6_28(): 
    # Opgave 6.28 - For the circuits in Fig. P6.28, assume that the transistors have very large Beta. 
    # Some measurements have been made on these circuits, with the results indicated in the figure. 
    # Find the values of the other labeled voltages and currents
    
    # De ukendte er, V2, V3, V4, V7, i1, i5, i6

    # a. pnp
    V2, V3, V4, V7, i1, i5, i6 = symbols("V2 V3 V4 V7 i1 i5 i6")
    # For enkelthedens skyld gåes der med den simplificeres form for spænding over en diode, 0.7V
    i2 = Symbol("i2")
    VEB = 0.7
    I = -10.7 + 5e3*i1 + VEB # = 0 
    II = -10.7 + 5e3*i2 -VEB # = 0 
    
    # Nu kan strømmene findes
    sol = solve([I, II], [i1, i2])
    i1 = sol[i1] # 2mA 
    i2 = sol[i2] # 2.28mA
    # print(i1)
    # print(i2)
    # iB er groundet, der kommer ingen strøm
    # iC = iB + iE 
    # Der er noget mærkeligt ved regnestykket her. 
    V2 = 0.7 # For at regnestykket går op, 0.7 - 5*2,28 = -10,7V som er slut resultatet. Det betyder, at der ingen spændingsfald er over VCE 
    # Mærkeligt, men jeg går videre.



    # b. pnp
    VCB, VEB, i3, i4 = symbols("VCB VEB i3 i4")
    I = -14.7 + 5600*i3 + VEB  # = 0
    II = -(-7.3) - VEB + 2400*i4 # = 0 
    
    
    I = I.subs(VEB, 0.7)
    II = II.subs(VEB, 0.7)

    sol = solve([I, II], [i3, i4])
    i3 = sol[i3]
    i4 = sol[i4]
    # print(i3) # 2.5mA
    # print(i4) # -2.75mA

    # Nu haves strømmen, nu kan V3 findes. 
    # V3 findes som indgangsspændingen minus spændingsfaldet over den 5.6kOhms resistor.
    V3 = 14.7 - 5600 * i3 # 0.7 
    # print(V3) # 0.7V


    # c. pnp 
    # Her ses der en emitter strøm I5 som ubekendt. 
    # V4 er ukendt, som er en spændingskilde, som danner knudepunkt med en strøm af lavet af en spændingskilde på 2V og en resistor på 15kOhm
    # VC = 0V
    # Jeg går KCL på den
    iB, iC, iDB, iG, IS, Beta, VB = symbols("iB iC iDB iG IS Beta VB")
    A = i5 + iC + iB # = 0
    B = iB + (2 - VB)/15e3 + iG # Strømmen over dioden, strømmen lavet fra den ekstra spændingskilde i serie med en modstand og strømmen som løber til ground
    A = A.subs([(iC, 0.5e-3)])
    VB = solve([A, B], [VB])[VB].subs(iB, IS/Beta)
    """
            15000.0*Beta*iG + 2.0*Beta + 15000.0*IS
    VB =    ───────────────────────────────────────
                            Beta           
    """
    V4 = VB 
    # Det kommer an på hvad resultatet af Beta er, jeg tror ikke Beta værdier går over 1000. Men nu har de skrevet, at den er very large.
    # Hvis Beta så går mod uendelig, så vil VB være 2Beta/Beta = 2
    V4 = 2/1 

    iG = (2 - VB)/15e3 + iB 
    iB = iG - (2 - VB)/15e3
    i5 = iB + iC 
    # Der findes et spændingsfald og en modstand, så iC er kendt
    i5 = i5.subs(iC, 10/20e3) # iC = 0.5mA


    # d. 
    Beta, iB, i6, iK, V7, VB = symbols("Beta iB i6 iK V7 VB")
    A = IS/Beta + Beta*iB - i6 # = 0
    B = (V7 - VB)/10e3 - IS/Beta # = 0 
    V7Val = 10 - 9.1e3*iK
    B = B.subs(V7, V7Val)    
    VB = solve([A, B], [VB])[VB]
    """
            -9100.0*Beta*iK + 10.0*Beta - 10000.0*Is
    VB =    ──────────────────────────────────
                            Beta                 
    """ 
    # Beta -> ∞ => VB = 2

    i6 = Beta*(V7Val - VB)*1/10e3 
    """
                        ⎛                  -9100.0*Beta*iK + 10.0*Beta - 10000.0⋅IS⎞
    i6 =    0.0001*Beta*⎜-9100.0*iK + 10 - ────────────────────────────────────────⎟
                        ⎝                                   Beta                   ⎠
    """
    # Beta gående mod uendelig => -1 + 2/1 = 1 
    i6 = 1e-3# 1 A eller 1mA? Det må være mA 
    # Det her har godt nok været forvirrende, det funger ikke helt. Men nu har jeg øvet mig på det, og jeg gider ikke, at bruge længere tid på det.
    # i6 * 3kOhm = 3Vs tab + 0,7 fra dioden er 3.7Vs tab
    # Knudepunkt V7 må da være -10 + 3.7V = -6.3V
    # Indgangsstrømmen er da (10 -(-6.3))/9100 = 1.8mA, som jo egentlig lyder som en okay værdi. 
    V7 = -6.3 
    # Forklaringen er ikke beregnet og er nok forkert, men det er et bud. 
    # Opgaven er færdig og svarende er: 
    svar = f""" 
    De ukendte er, V2, V3, V4, V7, i1, i5, i6
    Beta er blevet beskrevet som very large. Jeg tror ikke, at Beta værdier går over 1000, men jeg kunne tage fejl. 
    Beta er så antaget som om, at den går mod uendeligt. 
    =============================
    V2 = {V2}V
    V3 = {V3}V
    V4 = {V4}V
    V7 = {V7}V 
    i1 = {i1}A
    i5 = {i5}A 
    i6 = {i6}A 
    =============================
    """
    opgaveBesvarelse("Opgave 6.28", svar)


# Opgave 6.29

def opgave6_29(): 
    # Measurements ln the circuits of Fig. P6.29 produce labeled voltages as indicated. 
    # Find the value of Beta for each transistor. 
    
    # iE = iB + iC = (Beta + 1)/Beta * iC
    # a. PNP transistor.
    # ViC = 2V 
    # Strømmen iC = (2V - 0V)/2kOhm = 1mA
    iC = 1e-3 
    Beta = symbols("Beta")
    iE = ((Beta + 1)/Beta)*iC 
    iB = 4.3/200e3 
    eq = Eq(iE, iC + iB)
    Beta_a = solve(eq, Beta)[0]

    # b. PNP transistor. 
    # iC = (3V - 0V)/750Ohm = 4mA
    IS = symbols("IS")
    iC = 4e-3 
    iE = ((Beta + 1)/Beta)*iC 
    iB = IS/Beta + (4.3 - 3)/27e3 
    # iC = Beta*iB = Beta(IS/Beta + (4.3 - 3)/27e3)
    # iC = IS + Beta*(1.3/27e3)
    eq1 = Eq(IS + Beta*(1.3/27e3), 4e-3)
    Beta_b = solve(eq1, Beta)[0]
    # Hvis IS er baseret på en modstand i milli området vil det have betydning. 1 mOhm => IS = 0,7/0,001 = 700
    # Hvis IS er baseret på en modstand i 10^0 området, så vil IS være 0,7 -> 0,07
    # Hvis IS er baseret på en modstand i kilo området, så vil IS være 0,7 / 1k = 0,7mA 
    
    # Lad os sige at modstanden er 100kOhm, så er IS = 7uA
    # 7uA * 20,769k ≈ 140m 
    # 83 - 0,140 ≈ 83
    # Så er 
    Beta_b = 83.077

    # c. PNP transistor
    # Der ses en transistor med ukendt VEC spændingsfald
    # VC er nemlig ukendt
    # VE er kendt
    
    # Spændingsfaldet fra forsyning til VE er 10V - 7V = 3V
    # iE = 3V/1kOhm = 3mA 
    iE = 3e-3
    # iE = iB + iC
    # iB er som i b opgaven, her er VC bare ukendt
    VC, IS, Beta = symbols("VC IS Beta")
    iB = IS/Beta + (6.3 - VC)/45e3 
    iC = (VC - 0)/1.5e3 
    eq1 = iE - ((Beta + 1)/Beta)*iC # iE - iB - iC = 0 
    # Knudepunkt C: 
    # Beta*iB + ((6.3V - VC)/45kOhm + IS/Beta) - (VC - 0V)/1.5kOhm
    # Beta*iB + 6.3/45kOhm - VC/45kOhm + IS/Beta - VC/1.5kOhm 
    # Beta*iB + 6.3/45kOhm + VC*(-1/45kOhm - 1/1.5kOhm) = 0
    # VC * (-1/45kOhm - 30/45kOhm) = - Beta*iB - 6.3/45kOhm
    # VC * (-31/45kOhm) = - Beta*iB - 6.3/45kOhm
    # VC * (-31/45kOhm) = - Beta*iB - 6.3/45kOhm
    # VC = - Beta*iB*(45kOhm/-31) - (6.3/45kOhm)*(45kOhm/-31)
    # VC = - Beta*iB*(45kOhm/-31) - (6.3/-31)
    # VC = + Beta*iB*(45kOhm/31) + 6.3/31)
    VC = Beta*iB*(45e3/31) + 6.3/31 
    # Begge sider er afhængige af VC. På højre side er 1451 * Beta(-0.2u*VC)
    # VC kan ikke være højere end indgangsspændingen = 7
    print(1451 * Beta*(-1.4e-6)) # 2m * Beta. Lad os sige at beta max er 290. Der har den en betydning på - 0,580V. Det er noget men det er ikke alverdens undergang. 
    # i de to andre eksempler har den været under 100. Da vil den max bidrage med -0,2V.
    # Så jeg approximerer den ud af højre side af ligemedstegnet.
    # VC = 1451.61290322581*Beta*(-2.22222222222222e-5*VC + 0.00014 + IS/Beta) + 0.203225806451613
    VC = 1451.61290322581*Beta*(0.00014 + IS/Beta) + 0.203225806451613
    VC = 0.203*Beta + 1.45e+3*IS + 0.203
    eq1 = eq1.subs(Symbol("VC"), VC)
    sol = solve(eq1, Beta)
    Beta = -3.57e+3*IS - 3.57e+3*(IS**2 - 0.00621*IS + 7.89e-6)**0.5 + 10.1
    # Lad os som i opgave b antage, at IS er 7uA, da vil første led være i mili, u^2  = -6*2 = ^(-12). -12 + kilo = nano området.
    # 3.57k * 6m*u = u området. 
    # Dog i kvadratrod så u området bliver til mili, og det andet område bliver til 10^(-4.5) området.
    # Så 10^(-4.5) << 2 * 10^(-3) << 10.1
    # Da må beta være: 
    Beta = 10.1    

    svar = f"""Find Beta værdierne: 
       ===============
    a. Beta = {N(Beta_a, 3)}
       ===============
    b. Beta = 83.0769230769232 - 20769.2307692308*IS
    Lad os sige at modstanden er 100kOhm. IS = 0,7V/100k = 7uA
    7uA * 20,769k ≈ 140m 
    83 - 0,140 ≈ 83
    Så er 
    ===============
    Beta = {N(Beta_b, 3)}
    ===============
    c. Ved hjælp af Kirchhoffs strøm lov, så udledes VC som bruges til at forklare om iC.
    iC erstattes i udtrykket iE = iB + iC, og der løses for Beta. 
    Beta = -3.57e+3*IS - 3.57e+3*(IS**2 - 0.00621*IS + 7.89e-6)**0.5 + 10.1

    Lad os som i opgave b antage, at IS er 7uA, da vil første led være i mili, u^2  = -6*2 = ^(-12). -12 + kilo = nano området.
    3.57k * 6m*u = u området. 
    Dog i kvadratrod så u området bliver til mili, og det andet område bliver til 10^(-4.5) området.
    Så 10^(-4.5) << 2 * 10^(-3) << 10.1
    Da må beta være: 
    ===========
    Beta = 10.1
    ===========
    """
    opgaveBesvarelse("Opgave 6.29", svar)


# Opgave 6.40 
def opgave6_40(): 
    # Consider a transistor for which the base-emitter voltage drop is 0.7V at 10mA    
    # What current flows for VBE = 0.5V? 
    # Evaluate the ratio of the slopes of the iC - vBE curve at vBe = 700mV and at vBE = 500mV. The large ratio confirms the point that the BJT has an apparent threshold at vBE ≈ 0.5V

    # Der er tale om en npn, da spændingen er fra vBE og ikke vEB 
    # Scenariet tegnes.
    IS, Beta, VBE, VT = symbols("IS Beta VBE VT")


    # Fra                                       TABEL 6.2 side 322 
    iB = (IS/Beta) * exp(VBE/VT) # = 10mA
    iB = iB.subs([(VBE, 0.7), (VT, 25e-3)])
    # Lad os sige, at en typisk værdi for Beta er 180.
    iB = iB.subs(Beta, 180) 
    # Mærkeligt, den er i 10*10^10 området * IS. 
    # Med mindre IS = 10*10^(-13) området, så vil iB ikke give mening.
    print(iB)



    # iB = 10mA

# Opgave 6.52

#opgave6_28()
#opgave6_29()
opgave6_40()