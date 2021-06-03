import math

x = ["midhun",28,'O+ve']
for i in x :
    print(i)

for r in range(10):
    print (r,end =" ")
print()

c = range(1,51)
for raw in c :
    set = {raw}
    for re in set:
        s = {math.sqrt(re)}
        for p in s:
            ki = math.modf(p)#returnsfractional and integer part of re in tuple format
            if(ki[0]==0.0):
               print(raw)





