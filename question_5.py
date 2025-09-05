import matplotlib.pyplot as plt
import numpy as np
from numpy import random
random_normal = np.random.normal(loc=0, scale=1, size=1000)
plt.scatter(range(1000), random_normal, alpha=0.4)

plt.xlabel("Numbers(1-1000)")
plt.ylabel("Random Values")
plt.title("Scatter Plot of 1000 Random Numbers from Normal Distribution")

plt.show()