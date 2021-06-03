def modify(x):

    print(id(x))
    x = 12
    print(id(x))
    print('x=',x)

a=20
print(id(a))
modify(a)
print('a==',a)