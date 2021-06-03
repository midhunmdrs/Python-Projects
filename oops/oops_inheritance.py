

# super class
class A:
    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("feature 2 is working")

# sub class , single level inheritance
class B(A):

    def feature3(self):
        print("feature 3 is working")

    def feature4(self):
        print("feature 4 is working")

# multi level inheritance

class C(B):

    def feature5(self):
        print("feature 5 is working")



class D(C):

    def feature6(self):
        print("feature 6 is superworking")


class Z(A,D):
    super.mro()

    def feature7(self):
        print("feature 7 is supersub working")


a1 = A()
b1 = B()
c1 = C()
z1 = Z()

a1.feature1()
a1.feature2()

b1.feature1()
b1.feature4()

c1.feature5()

z1.feature2()