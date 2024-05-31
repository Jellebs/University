import numpy.random as rng 
import numpy as np
from Uni.Formelsamling.Opgaver import *
from Uni.Vaerktoejer.Plots import * 
class AmplitudeShiftKeying(): # ASK for binary sequence
    threshold = 0.8 # X > 0.8 => 1
    bitSequence = 1011110001     
    def decode(self, signaler): 
        bits = np.array([1 if abs(signal) > self.threshold else 0 for signal in signaler])
        return bits
        
    def encode(self, bits: int): # 1 => vaerdi var over 0.8. 0 => vaerdi var under 0.8
        rand = lambda low, high : rng.uniform(low, high)
        def compleksTal(lower, maximum): a = rand(lower, maximum); b = rand(0, maximum - abs(a)); return complex(a, b)
        data = np.array([compleksTal(self.threshold, 1) if int(bit) == 1 else compleksTal(0, self.threshold) for bit in str(bits)])
        return data


class LabOpgave(Opgave):
    ASK = AmplitudeShiftKeying()
    bits = 11110011001100111  
    resultat_data = ASK.encode(bits)
    resultat_bits = ASK.decode(resultat_data)[:, np.newaxis]
    fc = 8000 # 8kHz 
    t = np.linspace(0, 1/fc, len(str(bits)))[:, np.newaxis]
    plots = Plots()
    plots.x = t  
    I = resultat_data.real[:, np.newaxis]
    Q = resultat_data.imag[:, np.newaxis]
    It = I*np.cos(2*np.pi*fc*t)
    Qt = Q*np.sin(2*np.pi*fc*t)
    St = It + Qt
    plots.y = np.hstack([It, Qt, St, resultat_bits])
    plots.config.legends = ["It", "Qt", "St", "Bits"]
    plots.plot()
    
    # Tilføj noise. 
    It += rng.normal(np.mean(It), np.std(It))
    Qt += rng.normal(np.mean(Qt), np.std(Qt))
    St += rng.normal(np.mean(St), np.std(St))
    plots.y = np.hstack([It, Qt, St, resultat_bits])
    
    plots.plot()

    resultat_bits = ASK.decode(I + Q)
    
    # Der er ikke noget tydeligt støj på. 

    

labOpgave = LabOpgave()
