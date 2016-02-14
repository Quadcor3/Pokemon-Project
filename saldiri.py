import random


saldirilar={'flame': 'fire', 'recovery': 'normal', 'bubble': 'water', 'stomp': 'earth', 'psychic': 'psychic'}
types=['water', 'fire', 'psychic']




def flame():
    global damage, fail, dam, burn
    damage=random.randint(20, 28)
    fail=random.randint(1, 5)
    burn=random.randint(1, 5)  #???
    dam=1
    print("fonksiyon calisti")

def recovery():
    global heal, fail, statusheal, dam
    heal=random.randint(20, 50)
    fail=random.randint(1, 3)
    statusheal=random.randint(1, 5) ## Karşındaki pokemona göre farklı heal seçtirilebilir ya da direk allheal olur
    dam=0
    print("fonksiyon calisti")

def bubble():
    global damage, fail, dam
    damage=random.randint(15, 25)
    fail=random.randint(1, 8)
    dam=1
    print("fonksiyon calisti")

def stomp():
    global paralyze, damage, fail, dam
    damage=random.randint(10, 25)
    fail=random.randint(1, 5)
    dam=1
    paralyze=random.randint(1, 4)

def psychic():
    global damage, fail, dam
    damage=random.randint(30, 35)
    fail=random.randint(1, 4)
    dam=1