import numpy as np
import random as rd

n = int(input("Enter the dimension (n): "))
m = int(input("Enter the dimension (m): "))

A = [[int(rd.randint(1,100)) for x in range (m)]  for y in range(n)]
A= np.array(A)
print(A)

A_inverse = np.linalg.pinv(A)

print("Pseudoinverse Using Numpy Function: \n",A_inverse)
U, D, VT = np.linalg.svd(A)
print("D = \n",D)
D_plus = np.zeros((A.shape[0], A.shape[1])).T
print("D plus= \n",D_plus)
D_plus[:D.shape[0], :D.shape[0]] = np.linalg.inv(np.diag(D))
print("D plus++= \n",D_plus)
A_plus = VT.T.dot(D_plus).dot(U.T)

print("Pseudoinverse Using Equation:\n",A_plus)

if np.allclose(A_inverse,A_plus):
    print("Two inverses are equal")
else:
    print("Two inverses aren't equal")