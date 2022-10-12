import numpy as np
import matplotlib.pyplot as plt

temp = [63, 73, 80, 86, 84, 78, 66, 54, 45, 63]

F = np.array(temp)
(F-32)* 5 / 9
print(F)

plt.plot(F)
plt.show()

A = np.array([1, 2, 3, 4])
B = np.array([5, 6, 7, 8])
result = A + B
print(result)

a = np.array([0, 9, 21, 3])
a < 10
print(a)

b = np.array([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(b)