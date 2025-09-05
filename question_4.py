import numpy as np
from numpy import random

matrix = np.random.randint(100, size=(5,5))

for row in matrix:
    for num in row:
        print(round(num, 2), end=" ")
    print()

print(matrix[0:3, 0:3])

A = matrix[0]
B = matrix[:, 2]
dot_product = np.dot(A, B)
print("The dot product of the first row and last column is: ", dot_product)