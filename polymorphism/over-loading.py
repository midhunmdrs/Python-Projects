
class Student :
    def __init__(self ,a ,b):
        self.a = a
        self.b = b

    def sum(self ,a ,b,c):
        c = a+ b + c
        return c


mn = Student(5,45)
print(mn.sum(4,6,4))