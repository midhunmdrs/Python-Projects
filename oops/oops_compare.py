class C:
    def __init__(self):
        self.name = "midhun"
        self.age = 28

    def update(self):
        self.age = 29

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = C()
c1.age =40
c2 = C()

if c1.compare(c2) :
    print("same")
else:
    print("different")


c1.name = "MDRS"
c1.age =100

c1.update()


print(c1.name,c1.age)
print(c2.name ,c2.age)
