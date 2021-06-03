class Master:

    def __init__(self, name, Id):
        self.name = name
        self.Id = Id
        self.lap = self.Laptop() # inside outer class object

    def show(self):
        print(self.name, self.Id)

    class Laptop:
        def __init__(self):
            self.brand = "hp"
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu,self.ram)

s1 = Master("JD", 1)
s2 = Master("Jenni", 6)

print(s1.name, s1.Id)
s2.show()
var = s1.lap.brand
print(var)
lap1 = s1.lap  # inside outer class
lap2 = s2.lap   # inside outer class
print(lap1.ram,lap2.cpu)

lap1 = Master.Laptop() # outside outer class
lap1.show()