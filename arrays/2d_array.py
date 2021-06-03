from numpy import *

arr = array([

    [1, 2, 3],
    [4, 5, 6]
])
print(arr)
print(arr.ndim)

arr1 =array([
    [1,2,3,4,5,6],[7,8,9,10,11,12]
])
print(arr.flat,id(arr))
print(arr1.flatten())
print(arr1.reshape(2,2,3), arr.ndim)