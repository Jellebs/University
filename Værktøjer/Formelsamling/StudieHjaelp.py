import shutil 
import inspect
from sympy import * 
from scipy import constants
from sympy.parsing.sympy_parser import parse_expr
init_printing(pretty_print = True, use_latex=True, wrap_line = True, )


class Opgave: 
    # ? Erstatning 
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)  # Create instance
        pprint("\n\n\n")
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
        columns = shutil.get_terminal_size().columns if shutil.get_terminal_size().columns < 100 else 100  # Get terminal width
        pprint("\n"); pprint("="*columns)
        for noegle in resultater.keys():
            print("\n")
            vaerdi = resultater[noegle]
            # pprint(f"{noegle:^{columns}}")
            
            formatted_expr = pretty(vaerdi)
            for line in formatted_expr.split("\n"):
                print(line.center(columns))
            print("\n")
            
        pprint(""); pprint("="*columns) 
        
class Beregning(Opgave): 
    """
    Udvidelse til Opgave klassen
    Printer funktioner ud pænt. 
    
    Opsætning 
    --------
    res_...             <- Vil blive evalueret ud fra konstanter givet til sidst\\
    Konstanter = {      <- Vil være konstanter som bliver substitueret når resultaterne printes. 
        "a" : b, \\
        "b" : c \\
    } \\
    
    
    class Opgave(Beregning): 
        konstanter = {
            "a" : 20, 
            "b" : 10
        }
        
        H = lambda z : (symbols("a") + symbols("a") * z**(-1))/(1 - symbols("b") * symbols("h") * z**(-1))
        res_w = H(1)
    
    opg = Opgave()\\
    \\
    fysiske konstanter gælder også, der er enkelte defineret, her var plancks konstant defineret. 
    """

    def __udskiftSymboler__(self, *args, **kwargs): 
        """
        Udskifter symboler            
        
        ARGS
        ----- 
        fysisk : Bool <- Udskifter symboler med fysiske konstanter
        
        KWARGS
        ----- 
        y           : ax + ?        <- Ligningen som skal have sine symboler udskiftet
        navn        : ...           <- Navn på det resultat
        """
        
        # ? Fysiske konstanter
        konstanter = {
            "h" : constants.h
        }       
        
        
        # Udskift symboler med givne konstanter.
        y = kwargs["y"]
        try :
            symboler = self.konstanter 
            y = y.subs(symboler)
        except : 
            pprint(f"Kunne ikke ændre symboler for {kwargs["navn"] if "navn" in kwargs else "Ukendt"}")
                
        # Udskift sidste symboler med fysiske konstanter
        if "fysisk" in args:     
            try: 
                y = y.subs(konstanter)
            except: 
                pprint(f"Kunne ikke ændre fysiske syboler for {kwargs["navn"] if "navn" in kwargs else "Ukendt"}")
        return y
    
    def __sorterResultater__(self, variabler): 
        """
        Overridet funktion som også tager in mente, at værdierne er symbolske og skal substitueres. 
        """
        resultater = {}
        for k, v in variabler.items(): 
            if k.startswith('res') == False: continue
            resultat = k.split("_")[1] 
            res_num = self.__udskiftSymboler__(self, "fysisk", y = v, navn = resultat)
            resultater[resultat] = Eq(symbols(resultat), res_num) # Eq(resultat, )
            
        if resultater == {}: return
        self.__printResultater__(self, resultater) 
         
    def __new__(cls, *args, **kwargs):
        # instance = super().__new__(cls)  # Create instance            # Har kommenteret det her ud, da den printede resultater ud 2 gange.
        # ? Print funktionerne ud 
        liste = cls.__dict__.copy()
        print("Brugte metoder:")
        for name, method in liste.items():
            if name.startswith("_") or not callable(method):
                continue
            try : 
                sig = inspect.signature(method)
                params = list(sig.parameters.values())
                if len(params) > 1 : continue       # Flere end en parameter 
                
                # x
                x = symbols(str(params[0]))
                
                # y(x) = ...
                y = Function(name)(x)
                rhs = method(x)
                eq = Eq(y, method(x))
                pprint(eq)
                pprint("\n")
            except :
                pprint(f"Kunne ikke beskrive {name} som en matematisk en funktion")
            # Få parametre 
            

        print("Metoder med mere end en parameter er ikke tilgængelig for nu, måske senere. For nu vil det blive uberørte.")
        # ? Print resultaterne.
        cls.__sorterResultater__(cls, cls.__dict__)  
        # return instance
    """
    def __ændreClassMetoder__():
        For at ændre metoder :
        for name, method in cls.__dict__.items():
            if name.startswith("_") or not callable(method):
                continue
            # Få parametre 
            sig = inspect.signature(method)
            params = list(sig.parameters.values())
            if len(params) > 1 : continue       # Flere end en parameter 
            
            
            x = symbols(str(params[0]))
            # print(x)
            
            # y(x) = ...
            y = Function(name)(x)
            rhs = method(x)
            eq = Eq(y, method(x))
            pprint(eq)
            try: 
                eq = instance.udskiftSymboler("fysisk", y = eq, konstanter = instance.__dict__["konstanter"])
            except: 
                eq = instance.udskiftSymboler("fysisk", y = eq)
            
            # pprint(eq.rhs)
            # pprint(x)
            instance.__setattr__(name, lambdify(x, eq.rhs))
    """
            
           
        
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
        taeller = sum([b[i]*(z**(-i)) for i in range(len(b))])  #  Poly(b, z).args[0]¨
        naevner = sum([a[i]*(z**(-i)) for i in range(len(a))])  #  Poly(a, z).args[0]
        ligning = taeller/naevner
        return apart(ligning, z)
    if "CT" in args: 
        s = symbols("s")
        taeller = Poly(b, s).args[0]
        naevner = Poly(a, s).args[0]
        ligning = taeller/naevner
        return apart(ligning, s)