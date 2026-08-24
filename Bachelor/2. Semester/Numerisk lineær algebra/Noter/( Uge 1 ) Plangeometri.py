import numpy as np 
import matplotlib.pyplot as plt

a = 2.0
b = 98.0
c = 1.0/4.0
print(a,b,c)

d = b**2 - 4 * a * c 

sq_d = np.sqrt(d) 

q = (-b + sq_d) / (2*a)
r = (-b - sq_d) / (2*a)

# Ny måde at skrive første rod på. 
q_ny = c/(a*r)
print(q, r)
print(q_ny)


# vektorer

x, y = 3,4 
origo_x, origo_y = 0,0
len_v = np.sqrt(x**2+y**2)
c = x / (len_v) #cos(\theta)
s = y / (len_v) #sin(\theta)

w = 1/(len_v**2) # * v vector = vector(cos\theta, sin(\theta))
v = (len_v**2)*w 


# Tegn i python 

x = np.array([-0.5, 0.0, 1.0, 2.0, 3.0, 4.0])
y = np.array([1.5, 2.0, 0.0, 1.5, 0.0, 2.0])

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.plot(x,y)

#fig.savefig("fig-rotataion.pdf")

t = np.linspace(0, 2*np.pi, 100) # laver 100 punkter mellem 0 & 2 pi

ax.plot(t, np.cos(t))
ax.set_xlim(-3, 6) # Set x interval
ax.set_ylim(-2, 4) # Set y interval
ax.plot(np.cos(t), np.sin(t))


