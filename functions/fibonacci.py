def fib(n):
    a,b =0,1

    if n < 1:
        print("error")
    elif n==1:
        print(a)
    elif n > 1:
        print(a)
        print(b)


        for i in range(2, n):
            c = a + b
            a = b
            b = a
            print(c)








n= int(input("enter the no" ))
fib(n)
