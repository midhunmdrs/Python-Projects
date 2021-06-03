import math

x = 5.0
y = 8.0
z = x + y
print(z)
c=math.modf(z)
if(c[0]==0.0):
  print(c)

#a = int(input(sys.argv[0]))
#b = int(input(sys.argv[0]))
#d = a + b
#print(d)