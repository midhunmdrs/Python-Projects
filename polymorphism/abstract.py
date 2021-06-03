from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
    # print("process 1 is working")


class Laptop(Computer):
    def process(self):
        print("i from lapot")


class Whiteboard(Computer): # if u call the abstract class then all abs methods need to be defined 
    def write(self):
        print("i am writing")
    def process(self):
        print(" I am from whiteboard ")


class Programming:
    def prog(self, com):
        print("its bugging")
        com.process()


# com = Computer()
com1 = Laptop()
# com.process()
com1.process()
prog1 = Programming()
com3 = Whiteboard()
prog1.prog(com3)
