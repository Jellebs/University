import numpy as np
import matplotlib.pyplot as plt 
import os 
from scipy.io import wavfile
import soundcard as sc

parentFolders = ["Opgaver", "( Uge 6 ) - Praktiske opgaver", "Stemmeregulering", "Signals"]
def makePath(folders, filnavn): 
    dir = os.getcwd()
    for folder in folders: 
        dir += f"/{folder}" 
    dir += f"/{filnavn}"
    return dir

# Lyd -> værdier
path = makePath(parentFolders, "speech_mal_1.wav")
sampleRate, data = wavfile.read(path)


# Værdier -> lyd
'''
os.system("afplay " + f"'{path}'")
wavfile.write('Stemme reguleret.wav', sampleRate, data)
'''

# Saml 3 stemmer i en 
filer = ["speech_mal_1.wav", "speech_mal_5.wav", "speech_mal_1.wav", "speech_fem_4.wav"]
paths =[makePath(parentFolders, filer[i]) for i in range(len(filer))]
sampleRates = [0]
data = [0]
for i in range(0, len(filer)): 
    print(i)
    sampleRate, dat = wavfile.read(paths[i])
    data = np.hstack([data, dat]) 
    sampleRates.append(sampleRate) 
print(data.shape)


# Problemer, når der er forskellig form. <- Læg 0 til de sidste samples? 


