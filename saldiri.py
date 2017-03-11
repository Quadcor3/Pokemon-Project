import random


saldirilar={'leafage': 'grass', 'synthesis': 'grass', 'ingrain': 'grass', 'spore': 'grass', 'absorb': 'grass', 'incinerate': 'fire','eruption': 'fire','flamethrower': 'fire','ember': 'fire','overheat': 'fire', 'recovery': 'normal','clamp': 'water', 'brine': 'water', 'surf': 'water','scald': 'water', 'dive': 'water','bubble': 'water', 'stomp': 'ground', 'psychic': 'psychic', 'ember': 'fire', 'inferno': 'fire', 'hypnosis': 'psychic', 'psybeam': 'psychic', 'stunspore': 'normal', 'blizzard': 'water'}
types=['water', 'fire', 'psychic', 'ground', 'grass']

                                                     ##Perish Song???
paralyze=0
burn=0
sleep=0
heal=0
statusheal=0
freeze=0

def reseteffs():
    global paralyze, burn, sleep, heal, statusheal, freeze
    paralyze=0
    burn=0
    sleep=0
    heal=0
    statusheal=0
    freeze=0
            
            #   Fire-Type Moves

def incinerate():

    global damage, fail, dam, burn
    damage=random.randint(20, 28)
    fail=random.randint(1, 5)
    burn=random.randint(1, 6)  #???
    dam=1

def eruption():
    global damage, fail, dam, burn
    damage=random.randint(20, 28)
    fail=random.randint(1, 5)
    burn=random.randint(1, 6)  #???
    dam=1

def flamethrower():
    global damage, fail, dam, burn
    damage=random.randint(20, 28)
    fail=random.randint(1, 5)
    burn=random.randint(1, 6)
    dam=1

def overheat():
    global damage, fail, dam, burn
    damage=random.randint(20, 28)
    fail=random.randint(1, 5)
    burn=random.randint(1, 6)
    dam=1

def ember():
    global damage, fail, dam, burn
    damage=random.randint(20, 28)
    fail=random.randint(1, 5)
    burn=random.randint(1, 6)
    dam=1

def inferno():
    global damage, fail, dam, burn
    damage=random.randint(15, 25)
    fail=random.randint(1, 3)             # 1/2 X 2/3 den 1/3 olasılık oldu
    if fail==2 or fail==3:
        fail=random.randint(1, 2)
    burn=1
    dam=1

            #   Water-Type Moves

def bubble():
    global damage, fail, dam
    fail=random.randint(1, 100)
    if fail < 81: 
        damage=40
    else:
        damage=0
    dam=1

def dive():
    global damage, fail, dam
    fail=random.randint(1, 100)
    if fail < 51: 
        damage= 80
    else:
        damage=0
    dam=1

def surf():
    fail=random.randint(1, 100)
    if fail < 41: 
        damage=90
    else:
        damage=0
    dam=1

def brine():
    fail=random.randint(1, 100)
    if fail < 81: 
        damage=40
    else:
        damage=0
    dam=1

def clamp():
    fail=random.randint(1, 100)
    if fail < 81: 
        damage=50
    else:
        damage=0
    dam=1

def scald():
    fail=random.randint(1, 100)
    if fail < 71: 
        damage=60
    else:
        damage=0
    dam=1

            # Grass

def absorb():
    global damage, fail, dam
    damage=random.randint(15, 25)
    fail=random.randint(1, 8)
    dam=1
def ingrain():
    global damage, fail, dam
    damage=random.randint(15, 25)
    fail=random.randint(1, 8)
    dam=1
def spore():
    global damage, fail, dam
    damage=random.randint(15, 25)
    fail=random.randint(1, 8)
    dam=1
def synthesis():
    global damage, fail, dam
    damage=random.randint(15, 25)
    fail=random.randint(1, 8)
    dam=1
def leafage():
    global damage, fail, dam
    damage=random.randint(15, 25)
    fail=random.randint(1, 8)
    dam=1


def recovery():
    global heal, fail, statusheal, dam
    heal=random.randint(20, 50)
    fail=random.randint(1, 3)
    statusheal=random.randint(1, 5) ## Karşındaki pokemona göre farklı heal seçtirilebilir ya da direk allheal olur
    dam=0



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