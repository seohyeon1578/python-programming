import numpy as np

a = np.array([[2, 3], [5, 2]])
d = np.array([[1, 2, 3, 4, 5], [2, 4, 5, 6, 7], [5, 7, 8, 9, 9]])
b = np.array([1, 2, 3, 4, 5])

print(a)
print(d)
print(a.shape)
print(d.shape)
print(b.shape)
print(a.dtype)
print(d.dtype)
print(b.dtype)

d = d.astype('float64')
print(d)
print(d.dtype)
d = d.astype('int32')
print(d)
print(d.dtype)

print(d[1][2])
print(d[1, 2])

print(d[1:, 3:])

e = np.zeros((2, 10))
print(e)
print(e.dtype)
e = e.astype('int64')
print(e)
print(e.dtype)

f = np.ones((2, 10))
print(f)
print(f.dtype)

g = np.arange(2, 10)
print(g)

h = np.ones((2, 3))
print(h)
i = np.transpose(h)
print(i)