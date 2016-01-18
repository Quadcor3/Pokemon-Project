import random


saldirilar={'flame': 'fire', 'recovery': 'normal'}




def flame():
    global damage, fail, dam, burn
    damage=random.randint(20, 38)
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