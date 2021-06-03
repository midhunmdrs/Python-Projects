class Laptop:

    def __init__(self,cpu,ram):
        self.cpu =cpu
        self.ram =ram
        print("in init")


    def config(self):  #com1 is the obj passed to self

        print("i5,16gb,1TB")
        print('config is' , self.cpu , self.ram)



com1 = Laptop('i5',16)
com2 = Laptop('Ryzen',8)

com1.config()
com2.config()
