import numpy as np
covMat = np.array([[1, 0],
                   [0, 2]])
lamb = np.linalg.eig(covMat)
lamb, v = np.linalg.eig(covMat)
print((covMat - lamb[0]*np.eye(2)))

print((covMat - lamb[1]*np.eye(2)))
print(lamb)
print(v)