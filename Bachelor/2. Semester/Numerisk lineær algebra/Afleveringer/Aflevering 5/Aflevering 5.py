from numpy import *
from matplotlib.pyplot import * 
n = 1000
t = linspace(0, 2*pi, n)

x = 3*cos(t)
y = sin(2*t)

fig, ax = subplots()
ax.plot(x, y, label="A")
ax.set_aspect('equal')

A = vstack([x, y])
rng = random.default_rng()
# Tilfældig mellem pi / 5 & 4pi/5
theta = rng.uniform(pi / 5, 4*pi / 5)

def rotation(theta, A): 
    return array([[cos(theta), -sin(theta)], 
                  [sin(theta), cos(theta)]]) @ A

B = rotation(theta, A)

#ax.plot(*B, label = "Roteret figur")


# ------------------------------ Opgave c --------------------------# 

t_tilfældig = random.uniform(0, 2*pi, n); print(n) # n = 1000 

x_tilfældig = 3*cos(t_tilfældig) 
y_tilfældig = sin(2*t_tilfældig)

C = rotation(theta, vstack([x_tilfældig, y_tilfældig]))

# ax.plot(*C, 'o', label = "Tilfældig plukkede elementer") # Find ud af, hvordan jeg fjerner linjen i mellem dem.

støj = rng.normal(0.0, 0.1, (2, n))

A = C + støj

#ax.plot(*A, 'o', label = "Tilfældige punkter med støj")

# ------------------------------ Opgave d ------------------------------ # 

B = vstack([A[0] - mean(A[0]), A[1] - mean(A[1])])

print(mean(B[0]))
print(mean(B[1]))


ax.plot(*B, 'o', label="B - mean")

# ------------------------------ Opgave e ------------------------------ # 

u, s, vt = linalg.svd(B, full_matrices=False)
print(u)
print(s)
print(u.shape, s.shape, vt.shape)

# ------------------------------ Opgave f ------------------------------ #

rotation_matrix = array([[cos(theta), -sin(theta)], 
                  [sin(theta), cos(theta)]])

print(rotation_matrix)
print(u)


# ------------------------------ Opgave g ------------------------------ #

# ax.plot(*(u @ B), 'o', label = "u @ B ")
C = rotation(theta, A)
ax.plot(*C,'o', label = "r @ A")

v = u @ rotation_matrix

ax.plot(*(v @ vstack([x, y])), 'o', label = "v @ A")

ax.legend(loc = 'upper right')

# fig.savefig("A, B, C.pdf")