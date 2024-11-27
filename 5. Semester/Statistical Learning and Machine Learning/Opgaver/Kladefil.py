import numpy as np 
from sympy import * 
init_printing()

j = 4
x = MatrixSymbol('x', j, 1)
w = MatrixSymbol('w', j, 1)
pprint(Matrix(x)); pprint(Matrix(w))


y = Matrix(x).dot(Matrix(w))

pprint(y)

