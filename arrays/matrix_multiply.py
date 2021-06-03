from numpy import *

m1 = array([
    [1, 2, 3],
    [4, 5, 6]
])
m2 = array([
    [7, 8, 9],
    [6, 5, 4],
    [1, 5, 6]

])
r = zeros((2,3))
print(m1.shape)
print(m2.shape)

for i in range(2):
    for j in range(3):
       for k in range(3):
           r[i][j] = r[i][j] + m1[i][k] * m2[k][j]
for d in r:
    print(r)
    break


def add(x,y) :
    c = x+y
    print(c)

add(5,6)
res =add(7,3)
print(type(res))
print(res)
