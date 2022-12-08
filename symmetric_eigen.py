import numpy as np
import random as rd



def createRandomInvertibleSymmetricMatrix():
    A = [[int(rd.randint(1,10)) for x in range (n)]  for y in range(n)]
    A = np.array(A)
    S = np.matmul(A,A.T)
    if (np.linalg.det(S) == 0):
        createRandomInvertibleSymmetricMatrix()
    return S

n = int(input("Enter the dimension: "))

S = createRandomInvertibleSymmetricMatrix()
print("Random Invertible Symmetric Matrix:\n",S)

e_values, e_vectors = np.linalg.eig(S)
print("Eigen Values:\n",e_values)
print("Eigen Vectors:\n",e_vectors)

A2 = np.dot(e_vectors,np.dot(np.diag(e_values),np.linalg.inv(e_vectors)))
print("Random Reconstructed Invertible Symmetric Matrix:\n",A2)

if np.allclose(S,A2):
    print("Reconstruction is perfect")
else:
    print("Reconstruction isn't perfect")
