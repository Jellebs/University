from sympy import *


class DynamiskeSystemer(): 
    K = symbols("K")
    
    class andenOrdensSystemer(): 
        parameter_zeta = lambda self, overshoot : -ln(overshoot) / sqrt(pi**2 + (ln(overshoot))**2)
        design_gainFraOvershoot = lambda self, overshoot, toZetaOmega : (toZetaOmega/(2*self.parameter_zeta(overshoot)))**2 # Brugt til at designe gain controller på et andenordens karakteriske system ud fra overshoot. 
            

    
    
system = DynamiskeSystemer().andenOrdensSystemer()
pprint(N(system.design_gainFraOvershoot(0.1, 5), 10))



