
from threading import *


class Helloi(Thread):
    def run(self):
        for i in range ( 5 ):
            print ( "Hello" )
            # sleep(1)


class Hai ( Thread ):
    def run(self):
        for i in range ( 5 ):
            print ( "Hi" )
            # sleep(1)


t1 = Helloi ()
t2 = Hai ()
t1.run ()
t2.run ()
