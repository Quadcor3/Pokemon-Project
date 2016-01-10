import random
import sys
from tools import *
import saldiri


def flamethrower(whosturn):
    sleep(1)
    print("{} used Flamethrower!".format(whosturn))
    waitdot(3)
    fail=random.randint(1,5)
    if fail==1:
        print("But it failed.")
    else:
        print("{} used Flamethrower!".format(whosturn))
        damageflame=random.randint(20, 38)
        if whosturn is not "Charizard":
            charhealth=charhealth - damageflame
            print("Charizard is hit for {} damage!".format(damageflame))
        else:
            print("Your {} is been hit for {} damage!".format(whosturn, damageflame))
            playerhealth=playerhealth - damageflame




def attmove(whosturn, whosturnpoke, comhealth, phealth):
    att=input("saldırıyı gir:")
    print("{} used {}!".format(whosturnpoke, att))    #saldırıyı ekle
    getattr(saldiri, att)()                           #fonksiyonu çağırıyor mu belli değil araştır
    waitdot(3)
    if saldiri.fail==1:
        print("But it failed!")
    elif whosturn is "computer":
        comhealth=comhealth - saldiri.damage
        print("{} is hit for {} damage!".format(whosturnpoke, saldiri.damage))
    elif whosturn is "player":
        phealth=phealth - saldiri.damage
        print("{} is hit for {} damage!".format(whosturnpoke, saldiri.damage))



def saldirideneme():
    comhealth=100
    phealth=100
    whosturnpoke=input("poke name gir:\n")
    whosturn="player"
    attmove(whosturn, whosturnpoke, comhealth, phealth)

saldirideneme()