import numpy as np
import random as rd


def createRandomInvertibleMatrix():
    A = [[int(rd.randint(1,100)) for x in range (n)]  for y in range(n)]
    A = np.array(A)
    if (np.linalg.det(A) == 0):
        createRandomInvertibleMatrix()
    return A

n = int(input("Enter the dimension: "))

A = createRandomInvertibleMatrix()
print("Random Matrix:\n",A)

e_values, e_vectors = np.linalg.eig(A)
print("Eigen Values:\n",e_values)
print("Eigen Vectors:\n",e_vectors)

A2 = np.dot(e_vectors,np.dot(np.diag(e_values),np.linalg.inv(e_vectors)))
print("Random Reconstructed Matrix:\n",A2)

if np.allclose(A,A2):
    print("Reconstruction is perfect")
else:
    print("Reconstruction isn't perfect")