from numpy import *
arr = array([1,2,4,5,6],'i')
print(arr.dtype)

lins = linspace(0,12,14)
print(lins)
print(1.8461-0.9230)
print(2.7692-1.8461)

logs =logspace(0,10,4)
print(logs)
print()
print('%.2f'%logs[1])

off = zeros(6)
print(off)

on = ones(6)
print(on)


jrr = array([1,2,3,4,0])
jrr1 = array([1,2,3,4,5])
jrr2 = jrr+jrr1
print(jrr2)

lis1 = [1,2,3]
lis2 = [3,2,1,4]
lis3 = lis1+lis2
print(lis3)
