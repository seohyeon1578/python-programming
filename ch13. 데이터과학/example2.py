import numpy as np 

arr1 = np.array([[2, 3, 4], [6, 7, 8]])
arr2 = np.array([[12, 23, 14], [36, 47, 58]])
arr3 = np.array([100, 200, 300])
arr4 = np.array([1, 2, 3, 4, 5, 6, 7, 8 , 9, 10])
arr5 = np.array([[9], [3]])

print(arr1 + arr2)
print(arr1 * arr2)
print(arr1 / arr2)

print(arr1.shape)
print(arr3.shape)
print(arr4.shape)
print(arr5.shape)

print(arr1 + arr3)
# print(arr1 + arr4) Traceback
print(arr5 + arr1)