from numpy import *

arr = array([[1, 2, 3], [4, 5, 6]])
m = matrix(arr)
print(m)

m2 = matrix('1,2,3;3,4,5;1,8,6')
print(m2.dtype)
print(m2)
print(diagonal(m2))
print(m2*m2)