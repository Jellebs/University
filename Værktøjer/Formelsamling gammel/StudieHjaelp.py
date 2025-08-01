from sympy import * 

class Opgave: 
    # ? Erstatning 
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)  # Create instance
        if "beskrivelse" in cls.__dict__.keys(): pprint(cls.__dict__["beskrivelse"])  
        cls.__sorterResultater__(cls, cls.__dict__)
        return instance  # Return the created instance
    
    # ! Erstattet
    """
    def __init_subclass__(self):
        if "beskrivelse" in self.__dict__.keys(): pprint(self.__dict__["beskrivelse"])  
        self.__sorterResultater(self, self.__dict__)"""
    
    def __sorterResultater__(self, variabler): 
        resultater = {k.split("_")[1] : v for k, v in variabler.items() if k.startswith('res')}
        if resultater == {}: return
        self.__printResultater__(self, resultater)
    
    def __printResultater__(self, resultater): 
        pprint("\n"); pprint("="*80)
        for noegle in resultater.keys():
            vaerdi = resultater[noegle]
            pprint(f"{noegle:^80}")
            #pprint("\n ||\n\n") 
            pprint(f"{vaerdi:^80}")
        pprint(""); pprint("="*80) 
        
class Ligning(): 
    """
    En class lavet, så jeg hurtigere kan løse simplifering af lignings udtryk. 
    Den er sat op, så jeg kan bruge den i python notebook. Og dermed ikke skal køre et helt script pr. beregning.
    Forklar hvilken transformation sympy skal bruge.
    
    Start med at indsætte ligning og symboler som argumenter.
    """
    __ligning = None 
    
    def __init__(self, *args):
        super().__init__()
        for arg in args: 
            navn = str(arg)
            setattr(Ligning, navn, arg)
        self.__ligning = None
    
    def ligning(self, funktion = None, *args, **kwargs): 
        if "get" in kwargs.keys():                                         # Get
            return self.__ligning
        if "ligning" in kwargs.keys():                                     # Set 
            self.__ligning = kwargs["ligning"]
            pprint(self.__ligning)
            return 
        if funktion is None:                                    # Print
            pprint(self.__ligning)
            return
        if type(funktion) is str:
            # Tilfældet hvor operationen ikke er en funktion
            # Men en metode i variablen.
            # f.eks rewrite, replace og subs
            # eq.rewrite() ikke rewrite(eq)
            operation = self.__ligning.__getattribute__(funktion)
            self.__ligning = operation(*args)
            pprint(self.__ligning)
            return 
        self.__ligning = funktion(self.__ligning, *args) # Juster
        pprint(self.__ligning)
        
def partialFraction(b, a, *args):
    """
    Funktion til at simplificere min brug af partial fraction, diskrete eller ej. 
    b, a er koefficienter tilhørende graderne af frekvens i henholdsvis tæller og nævner. 
    Kontinuer tid:
    1s^2 + 1s + 3
    -------------
    3s^2 + 2s + 5
    b = [1, 1, 3]  |  a = [3, 2, 5]
    
    s = jw
    
    Diskrete tid: 
    1z^2 + 1z + 3
    -------------
    3z^2 + 2z + 5
    b = [1, 1, 3]
    a = [3, 2, 5]

    z = e^-jw
    
    Argumenter: 
    "DT" -> Diskrete tid
    "CT" -> Kontinuert tid   
    """
    
    if "DT" in args: 
        z, w = symbols("z w") # exp(-jw)
        taeller = Poly(b, z).args[0]
        naevner = Poly(a, z).args[0]
        ligning = taeller/naevner
        return apart(ligning, z)
    if "CT" in args: 
        s = symbols("s")
        taeller = Poly(b, s).args[0]
        naevner = Poly(a, s).args[0]
        ligning = taeller/naevner
        return apart(ligning, s)