import random

damage=0
fail=0


saldirilar=['flame']


def flame():
    global damage
    global fail
    damage=random.randint(20, 38)
    fail=random.randint(1, 5)
    burn=random.randint(1, 10)  #???
    print("fonksiyon calisti")

def 