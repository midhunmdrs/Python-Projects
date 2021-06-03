from array import *

arr =array('i',[])
n = int(input("What is the length of array "))
for i in range(n):
    x = int(input("enter the next value: "))
    arr.append(x)

print(arr)

val = int(input("enter the search value "))

for i in range(len(arr)) :
    if arr[i] == val:
        print(i)
        continue

print(arr.index(val))
