from Formelsamling.StudieHjaelp import Beregning
from sympy import * 
from scipy import constants 
class Opgave(Beregning): 
    konstanter = {
        "a" : 20, 
        "b" : 10
    }
    
    H = lambda z : (symbols("a") + symbols("a") * z**(-1))/(1 - symbols("b") * symbols("h") * z**(-1))
    res_w = H(1)

Opgave()



import inspect

class Beregninger(Opgave): 
    """
    Printer metoder symbolsk ud ved initializing. Efter print erstatter den værdierne, så udtrykket bliver numerisk. \\
    Lad en class egenskab være \\
    Konstanter = { \\
        "a" : b, \\
        "b" : c \\
    } \\
    For at disse skal blive erstattet efter print
    """
    

    def __udskiftSymboler__(self, *args, **kwargs): 
        """
        Udskifter symboler            
        
        ARGS
        ----- 
        fysisk : Bool <- Udskifter symboler med fysiske konstanter
        
        KWARGS
        ----- 
        y           : ax + ?       <- Ligningen som skal have sine symboler udskiftet
        """
        
        # ? Fysiske konstanter
        konstanter = {
            "h" : constants.h
        }       
        
        
        # Udskift symboler med givne konstanter.
        y = kwargs["y"]
        if len(kwargs) != 1: 
            try :
                symboler = self.konstanter 
                y = y.subs(symboler)
            except : 
                print("Kunne ikke ændre symboler til konstanter")
                
        # Udskift sidste symboler med fysiske konstanter
        if "fysisk" in args:     
            y = y.subs(konstanter)
        return y
    
    def __sorterResultater__(self, variabler): 
        """
        Overridet funktion som også tager in mente, at værdierne er symbolske og skal substitueres. 
        """
        resultater = {}
        for k, v in variabler.items(): 
            if k.startswith('res') == False: continue
            resultat = k.split("_")[1] 
            res_num = self.__udskiftSymboler__(self, "fysisk", y = v)
            resultater[resultat] = res_num
            
        if resultater == {}: return
        self.__printResultater__(self, resultater) 
         
    def __new__(cls, *args, **kwargs):
        print("Brugte metoder")
        print("Metoder med mere end en parameter er ikke tilgængelig for nu, måske senere. For nu vil det blive uberørte.")
        
        # ? Print funktionerne ud 
        liste = cls.__dict__.copy()
        for name, method in liste.items():
            if name.startswith("_") or not callable(method):
                continue
            # Få parametre 
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

        # ? Print resultaterne.
        cls.__sorterResultater__(cls, cls.__dict__)  
    
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
            
    