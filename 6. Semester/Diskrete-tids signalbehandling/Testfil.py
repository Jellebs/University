import matplotlib.pyplot as plt
import numpy as np
import itertools

"""
enkeltPlot = np.ndim(ax) <= 1 or frekvensFunktioner is None

enkeltMetode = len(metoder) == 1
colormap = plt.cm.viridis if "colormap" not in kwargs.keys() else args["colormap"]
N = len(frekvensFunktioner) if frekvensFunktioner is not None else 1
colors = colormap(np.linspace(0, 1, N)) 

"""
args = ["Magnitude", "Fase", "Unwrapped", "Gruppedelay"]
metoder = itertools.cycle(iter([funktion for funktion in args if funktion in ["Magnitude", "Fase", "Unwrapped", "Gruppedelay"]])) # Samler ønskede funktioner ud af argumentsne
def plotMetode(ax, w, H, metoder): 
    match next(metoder): 
        case "Magnitude": 
            print("Her")
        case "Fase": 
            print("Der")
        case "Unwrapped": 
            print("Vi")
        case "Gruppedelay": 
            print("I")
        case default: 
            print("Ski")

plotMetode("", "", "", metoder)
plotMetode("", "", "", metoder)
plotMetode("", "", "", metoder)
plotMetode("", "", "", metoder)
plotMetode("", "", "", metoder)
plotMetode("", "", "", metoder)
plotMetode("", "", "", metoder)
plotMetode("", "", "", metoder)
plotMetode("", "", "", metoder)

print(2 and 1)
print(1 and 1)