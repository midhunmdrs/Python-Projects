i=23

print(id(i))
def loc():
    i = 36
   # global i
    g = globals()['i']

    print(id(g))
    print(i)

    globals()['i']=32

loc()
print("out",i)
