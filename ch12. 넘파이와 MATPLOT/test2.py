import numpy as np

a = np.array([1, 2, 3, 4, 5])
a.shape
b = np.array([[1, 2, 3], [4, 5, 6]])
b.shape
b.dtype
b.astype('float64')

np.zeros((2, 10))
np.ones((2, 10))
np.eye(3, dtype=int)
