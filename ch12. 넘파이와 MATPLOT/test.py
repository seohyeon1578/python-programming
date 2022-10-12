import numpy as np

heights = [1.83, 1.76, 1.69, 1.86, 1.77, 1.73]
weights = [86, 74, 59, 95, 80, 68]
height = np.array(heights)
weight = np.array(weights)
bmi = weight / (height ** 2)
print(bmi)