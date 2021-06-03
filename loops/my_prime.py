num =11
x= num % 2
if x == 0 :
    print("not prime")
else:
    for i in range (3,num,2):
     if(num % i == 0):
        print("not prime")
        break
    else:
        print("prime")

print("bye")

