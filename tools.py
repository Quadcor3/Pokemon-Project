from time import sleep
import saldiri

def waitdot(howmanydot):
    for i in range(howmanydot):
        sleep(0.5)
        print(".")
    sleep(1)

class saldirilistesi():

    def __init__(self):
        self.saldiril=[]

    def ekleme(self, y):
        x=input("{} icin 1. saldiriyi girin".format(y))
        if x in saldiri.saldirilar:
            self.saldiril.append(x)
        x=input("{} icin 2. saldiriyi girin".format(y))
        if x in saldiri.saldirilar:
            self.saldiril.append(x)
        x=input("{} icin 3. saldiriyi girin".format(y))
        if x in saldiri.saldirilar:
            self.saldiril.append(x)
        x=input("{} icin 4. saldiriyi girin".format(y))
        if x in saldiri.saldirilar:
            self.saldiril.append(x)