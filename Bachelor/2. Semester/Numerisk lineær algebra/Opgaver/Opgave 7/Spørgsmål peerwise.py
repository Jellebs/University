import numpy as np 
from Formelsamling.Numerisk_Lineær_Algebra import *

# Ligning 1: 3x + 5y + 0z = 10
# Ligning 2: 5x + 5y + 3z = 12
# Ligning 3: 10x + 6y + 4z = 10

a = np.array([
    [ 3, 5, 0],
    [ 5, 5, 3],
    [10, 6, 4]], dtype= float)

b = np.array([10, 12, 10], dtype=float)[:, np.newaxis]

aub = np.hstack([a, b])


skift(aub, 0, 2)
lægTil(aub, 1, -1/2, 0)
lægTil(aub, 2, -3/10, 0)

skaler(aub, 1/3.2, 2)
skaler(aub, 1/2, 1)
lægTil(aub, 2, -1, 1)
skaler(aub, -1/0.875, 2)
skaler(aub, 1/10, 0)
erStatVærdier(aub, 2, 2, 3)
erStatVærdier(aub, 1, 1, 3)
print(aub)


