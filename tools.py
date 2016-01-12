from time import sleep

def waitdot(howmanydot):
    for i in range(howmanydot):
        sleep(0.5)
        print(".")
    sleep(1)

class saldirilistesi():
    
    def __init__(self, Sismi):
        self.Sismi=Sismi
        self.saldiril=[]
        self.ekleme()

    def ekleme(self):
        self.saldiril.append(self.Sismi)