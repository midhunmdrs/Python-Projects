
class Student:

    school = "Mdrs School"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def info(cls):
        return cls.school

    @staticmethod
    def meta():
        print("BULLS EYE")

    def get_m1(self):
        return self.m1

    def set_m1(self,value):
         self.m1 = value
         return value


s1 = Student(52,48,78)
s2 = Student(50,63,74)
Student.meta()


print(Student.info())
print(s1.avg())
print(s2.avg())
print(s1.m1)
n = s1.get_m1()
print(n)
p = s2.set_m1(56)
print(p)
