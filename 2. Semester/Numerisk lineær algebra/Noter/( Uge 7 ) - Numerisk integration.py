import numpy as np 
import matplotlib.pyplot as plt

# Indre produkt 

# Kompleks konjugeret : z = x + iy => z.konj = x-iy

u = np.array([0, 1, 1j])
v = np.array([1, 1j, 2])

print(np.vdot(v, u)) # Omvendt konvention, vdot(v, u), ellers fåes den konjugerede. 

# Kan beregnes via række søjle produkt, men husk konjugering på vektor som ganges på.
# <u, v>
print(np.conjugate(v.T) @ u)

print(np.vdot(v, v))




# Numerisk integration 

# f(x) = x**3 
n = 100
x = np.linspace(0, 2, n)
x, h = np.linspace(0, 2, n, retstep=True) # retstep er mellemrummet mellem vær punkter
print(h, x[11] - x[10]) # h er mere præcis, da h er b - a / 99, n - 1, hvor vi regner med b - a / 100

# Rektangulær approksimation fra venstre endepunkter.
f = x**3 
print(h * np.sum(f[:-1])) # n - 1 ( Approksimation af funktion fra 0 -> 2 ved hjælp af integration )

# Rektangulær approksimation fra højre side
print(h * np.sum(f[:1]))


# Trapez reglen 

print( h * (f[0]+ 2*np.sum(f[1:-1])+ f[-1])/2) 
print(np.trapz(f, dx= h)) # numpy funktion

# Fordobling af h medfører en forbedring af approksimation på 8 ( 2 ** 3 )

n = 100

x, h = np.linspace(0, 2, n, retstep=True)
f = x**3
print(np.trapz(f, dx= h))

# Eksempel med cosinus Fourier række

x, h = np.linspace(0, np.pi, n, retstep=True)
f = x**3

def indre_produkt(f, g, h): 
    return np.trapz(f*g, dx=h)

# 1 er vinkelret på alle funktioner. 
konstant = np.ones_like(x)
print(indre_produkt(konstant, np.cos(5*x), h)) # Meget tæt på 0 => vinkelrette på hinanden. 
print(indre_produkt(np.cos(2*x), np.cos(5*x), h)) # Det samme resultat.
print(indre_produkt(np.cos(3*x), np.cos(5*x), h)) # Lidt anderledes med basically også 0. 

# P(f) = <f_1v_0>/ ||v_0||2

def norm_sq(f, h): 
    return indre_produkt(f, f, h) 

print(f" Konstant^2: {norm_sq(konstant, h)}")
print(norm_sq(np.cos(5*x), h)) # == 1/2 pi
print(norm_sq(np.cos(5*x), h) - np.pi/2) # == 0 
print(np.allclose(f, f * konstant))
f_k = indre_produkt(f, konstant, h)
print(f_k)
#print(np.allclose(f, indre_produkt(f, konstant, h)))

def proj(f, k, x, h): 
    out = (indre_produkt(f, konstant, h)/norm_sq(konstant, h)
           * konstant)
    for m in range(1, k): 
        out += (indre_produkt(f, np.cos(m*x), h) 
                / norm_sq(np.cos(m*x), h)
                * np.cos(m*x))
    return out
    

print(f * np.ones_like(x))
print(proj(f, 1, x, h))
print(proj(f, 2, x, h))
plt.rcParams['figure.dpi']=100
fig, ax = plt.subplots()
#ax.set_aspect("equal")
ax.set_xlim(0, 4)
ax.plot(x, f)
ax.plot(x, proj(f, 1, x, h), label = "1")
ax.plot(x, proj(f, 2, x, h), label = "2")
ax.plot(x, proj(f, 4, x, h), label = "4") # Den bedste fourier approksimation.
ax.plot(x, proj(f, 8, x, h), label = "8") # Den bedste fourier approksimation.
ax.plot(x, proj(f, 100, x, h), label = "100") # Den bedste fourier approksimation.
# Konklusion 
# Jo højere frekvens, jo bedre approksimation 

ax.legend()
print(np.trapz(np.cos(x), dx = h))