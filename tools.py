from time import sleep

def waitdot(howmanydot):
    for i in range(howmanydot):
        sleep(0.5)
        print(".")
    sleep(1)

