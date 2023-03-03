import numpy as np 
import matplotlib.pyplot as peterplys

# Householder matricer. 

A = np.array([[3/5, 0, 4/5], (4/5, 0, -3/5)])
sum = 0 
def pythagoras(vektor): 
    sum = 0
    for i in vektor: 
        sum += np.sqrt(i**2)
    return sum

# Check for ortonormalitet. Længden af søjler = 1 
print(pythagoras(A[:, 0]))
print(pythagoras(A[:, 1]))
print(pythagoras(A[:, 2]))

# H = I_n - svv.T beregn Hx
def house_transformation(s, v, x): 
    return x - v * (s * (v.T @ x ))

v = np.array([0.5, 0.5, -0.5, -0.5])[:, np.newaxis] 
H = np.eye(4) - (2/np.vdot(v, v)) * v @ v.T # s = 2/||v||_2**2, I_N - svv.T
print(H)

print(house_transformation(2/np.vdot(v,v), v, v))
print(H @ v) # Skulle give det samme svar som ^. 

rng = np.random.default_rng()
x = rng.standard_normal((4, 1))
s = 2 / np.vdot(v, v)
print(f"Householder:\n{ H @ x}\nFunktion:\n{house_transformation(s, v, x)}")
# House transformationen virker.

print(x, house_transformation(s, v, house_transformation(s, v, x)))
# H**2 = I_n, I_n * x = x, derfor 2 betegnelser for det samme resultat ovenover ^.

print(H.T @ H) # I_N 



# Singulær værdi 

t = np.linspace(0, 2*np.pi, 100)
x = np.cos(t)
y = np.sin(t)

fig, ax = peterplys.subplots()
ax.set_aspect("equal")
ax.plot(x,y)

a = np.array([[2., 3.], [-1, 1]])

ny_x = a[0,0]*x + a[0,1]*y
ny_y = a[1,0]*x + a[1,1]*y
ax.plot(ny_x,ny_y)

a = rng.standard_normal((2,2))
ny_x = a[0,0]*x + a[0,1]*y
ny_y = a[1,0]*x + a[1,1]*y

ax.plot(ny_x, ny_y)

