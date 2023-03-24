# Dokumentet startes med importsne
import numpy as np
import matplotlib.pyplot as plt

# a. Vælg nogle rimelige værdier for indgangerne i a, b, c og ⁡d, og brug derefter matplotlib til at lave en tegningen af robotarmen som ovenfor.
O = np.array([0,0])
A = np.array([2,5])
B = np.array([2.5, 5.5])
C = np.array([3, 4])
P = np.array([2.75, 3.75])

a = A - O 
b = B - A
c = C - B
d = P - C 

def rotation(vinkel: int): 
    theta = np.radians(vinkel)
    return np.array([[np.cos(theta), -np.sin(theta)], 
                    [np.sin(theta),  np.cos(theta)]])

#En funktion til at plotte vektorerne ud fra en startposition: 
def lavArm(vectors: list[list[float]], startkoordinat: list[float], rotationsVinkel: int = None, rotation_index = None, text = None):
    x = [startkoordinat[0]]
    y = [startkoordinat[1]]
    v = vectors.copy()
    if rotationsVinkel != None and rotation_index != None: 
        for i in range(len(v)): 
            if i >= rotation_index: 
                v[i, :] = np.array(rotation(rotationsVinkel) @ v[i])

                continue

    for i in range(len(v)): 
        x.append(v[i][0] + x[i])
        y.append(v[i][1] + y[i])
    if text == None: 
        ax.plot(x,y, label= f"x: {x[-1]}, y: {y[-1]}")
    else: 
        ax.plot(x,y, label= text)
    

vectors = np.array([a, b, c, d])
fig, ax = plt.subplots()

lavArm(vectors, O, text = "Startposition")
# d. Giv en opskrift for bøjA(S), hvor robotarmen bøjes kun i ledet A. Vis dette i en tegning
lavArm(vectors, O, -20, 1, text = "-20 graders rotation") 

# e. 

ax.legend()