import random

damage=0
fail=0

def flame():
    global damage
    global fail
    x=random.randint(1, 5)
    y=random.randint(20, 38)
    damage=y
    fail=x
    burn=random.randint(1, 10)  #???
    print("fonksiyon calisti")

