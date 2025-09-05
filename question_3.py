import numpy as np
from numpy import random

matrix = np.random.randint(100, size=(5,5))

for row in matrix:
    for num in row:
        print(round(num, 2), end=" ")
    print()
maximum = np.max(matrix)
minimum = np.min(matrix)
mean = np.mean(matrix)

print("The maximum is", maximum)
print("The minimum is", minimum)
print("The Mean of the max and min is", mean)

normalise = (matrix - minimum) / (maximum - minimum)
for row in normalise:
    for num in row:
        print(round(num, 2), end=" ")
    print()

new_matrix = matrix.reshape(-1)
print(new_matrix)