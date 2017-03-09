import random


saldirilar={'flame': 'fire','fire blast': 'fire','ember': 'fire','overheat': 'fire', 'recovery': 'normal', 'bubble': 'water', 'stomp': 'ground', 'psychic': 'psychic', 'ember': 'fire', 'inferno': 'fire', 'hypnosis': 'psychic', 'psybeam': 'psychic', 'stunspore': 'normal', 'blizzard': 'water'}
types=['water', 'fire', 'psychic', 'ground']

                                                     ##Perish Song???
paralyze=0
burn=0
sleep=0
heal=0
block=0
statusheal=0
freeze=0

def reseteffs():
    paralyze=0
    burn=0
    sleep=0
    heal=0
    block=0
    statusheal=0
    freeze=0

def flame():
    global damage, fail, dam, burn
    damage=random.randint(20, 28)
    fail=random.randint(1, 5)
    burn=random.randint(1, 6)  #???
    dam=1

def fireblast():
    global damage, fail, dam, burn
    damage=random.randint(20, 28)
    fail=random.randint(1, 5)
    burn=random.randint(1, 6)  #???
    dam=1

def overheat():
    global damage, fail, dam, burn
    damage=random.randint(20, 28)
    fail=random.randint(1, 5)
    burn=random.randint(1, 6)  #???
    dam=1

def ember():
    global damage, fail, dam, burn
    damage=random.randint(20, 28)
    fail=random.randint(1, 5)
    burn=random.randint(1, 6)  #???
    dam=1

def recovery():
    global heal, fail, statusheal, dam
    heal=random.randint(20, 50)
    fail=random.randint(1, 3)
    statusheal=random.randint(1, 5) ## Karşındaki pokemona göre farklı heal seçtirilebilir ya da direk allheal olur
    dam=0

def bubble():
    global damage, fail, dam
    damage=random.randint(15, 25)
    fail=random.randint(1, 8)
    dam=1

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

def ember():
    global damage, fail, dam, burn
    damage=random.randint(10, 20)
    fail=random.randint(1, 6)
    burn=random.randint(1, 3)
    dam=1

def inferno():
    global damage, fail, dam, burn
    damage=random.randint(15, 25)
    fail=random.randint(1, 3)             # 1/2 X 2/3 den 1/3 olasılık oldu
    if fail==2 or fail==3:
        fail=random.randint(1, 2)
    burn=1
    dam=1

def hypnosis():
    global fail, dam, sleep
    fail=random.randint(1, 2)          # 4'te 1 olasılık
    if fail==1:
        fail=random.randint(1, 2)
    sleep=1
    dam=2

def psybeam():
    global damage, fail, dam
    damage=random.randint(15, 30)
    fail=random.randint(1, 6)
    dam=1

def stunspore():
    global fail, dam, paralyze
    fail=random.randint(1, 3)
    dam=2
    paralyze=1

def blizzard():
    global fail, dam, damage, freeze
    fail=random.randint(1, 3)
    damage=random.randint(15, 25)
    dam=1
    freeze=random.randint(1, 4)