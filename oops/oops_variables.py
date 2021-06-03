
# Class Variables
# Instance Variables

class Car:
    company = "B M W"

    def __init__(self):
        self.mil = 10
        self.color = "black"


c1 = Car()
c2 = Car()
c1.mil =9

print(c1.mil,)
print(c2.mil)
print(c1.company)
