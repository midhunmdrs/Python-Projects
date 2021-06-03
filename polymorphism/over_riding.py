
class A :
    def show(self):
        print("Big B ")

class B(A) :
    def show(self):
        print("Now I am Big B")


a1 = B()
a1.show()