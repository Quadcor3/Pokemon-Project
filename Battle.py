import random
from tools import *
import saldiri
import os
from os import path
import shutil
import pokemonpick

block=0

class battle():
    
    def __init__(self, health, saldiri, status, typadv=1):
        self.battlehealth = pokemonpick.health
        self.saldiri = saldiri
        self.status = status
        self.typemod = typadv


    def attmove(self, yapan, karsi):     # For player and now for com too
        moves = open("player_moves.txt" ,"r")
        moves = read.moves
        while True:
            if yapan=="user":
                att=input("What is your move?:\n{}\n".format(moves))
            if yapan=="com":
                att=random.choice(self.saldiri)
            if att in moves:
                getattr(saldiri, att)()   #saldiri.(kullanıcı inputu)  yapmaya yarıyo
                break
            else:
                print("Select a valid move!")
                sleep(1)
        self.checkstatus()
        self.checkblock()
        if block==0:
            print("{} used {}!".format(self.pokename, att))
            if saldiri.dam==1:
                self.attdamage(karsi, att)
            elif saldiri.dam==0:
                self.attheal()
            elif saldiri.dam==2:
                karsi.statuseff()

    def typadv(self,karsi, att):
        if "fire" == karsi.poketype:
            if 'water' == saldiri.saldirilar[att]:
                print("It was super effective!")
                self.typemod = 2
            elif 'grass' == saldiri.saldirilar[att] or 'fire' == saldiri.saldirilar[att]:
                self.typemod = 0.5
                print("It was not very effective...")
            else:
                self.typemod = 1
        elif "water" == karsi.poketype:
            if 'grass' == saldiri.saldirilar[att]:
                self.typemod = 2
                print("It was super effective!")
            elif 'fire' == saldiri.saldirilar[att]:
                self.typemod = 0.5
                print("It was not very effective...")
            else:
                self.typemod = 1
        elif "grass" == karsi.poketype:
            if 'fire' == saldiri.saldirilar[att]:
                self.typemod = 2
                print("It was super effective!")
            elif 'water' == saldiri.saldirilar[att]:
                self.typemod = 0.5
                print("It was not very effective...")
            else:
                self.typemod = 1   
                        
    def attdamage(self, karsi, att):   #for both
        waitdot(3)
        if saldiri.damage > 0:
            self.typadv(karsi, att)
            damagedealt=int(saldiri.damage * self.typemod)
            karsi.health-=damagedealt
            print("{} is hit for {} damage!".format(karsi.pokename, damagedealt))
            karsi.statuseff()
        else:
            print("{} missed it's attack!".format(self.pokename))

    def attheal(self):
        waitdot(3)
        if saldiri.fail==1:
            print("But it failed!")
        else:
            self.health+=saldiri.heal
            print("{} have been healed for {} health".format(self.pokename, saldiri.heal))
            if saldiri.statusheal==1:
                self.status.clear()
                print("All status effects has been healed!")      #status heal pek mantikli degil?
            
    
    


    def statuseff(self):         ### Statusler yaptıkça buraya da ekle!!
        if saldiri.burn==1:
            self.status.clear()
            self.status.append('burn')
            print("{} is burnt!".format(self.pokename))
            saldiri.reseteffs()
        if saldiri.paralyze==1:
            self.status.clear()
            self.status.append('paralyze')
            print("{} is paralyzed! It may be unable to move!".format(self.pokename))
            saldiri.reseteffs()
        if saldiri.sleep==1:
            self.status.clear()
            self.status.append('sleep')
            print("{} fell asleep!".format(self.pokename))
            saldiri.reseteffs()
        if saldiri.freeze==1:
            self.status.clear()
            self.status.append('freeze')
            print("{} is frozen solid! It can't move!".format(self.pokename))
            saldiri.reseteffs()

    def checkstatus(self):
        if "burn" in self.status:
            burnbreak=random.randint(1, 100)               # 1 de 5 kurtulma olasiligi fazla mi?  Kurtulma olasılığı ayarla azaltıldı!
            if burnbreak==1:
                print("{} is no longer burnt!".format(self.pokename))
                self.status.clear()
                sleep(1)
            else:
                burndamage=random.randint(5, 15)
                self.health-=burndamage
                print("{} is hurt by its burn!\nTook {} damage!".format(self.pokename, burndamage))
        if "paralyze" in self.status:
            paralyzebreak=random.randint(1, 5)                  #paralyze den kurtulma sansi 1 de 5
            if paralyzebreak==1:
                print("{} is no longer paralyzed!".format(self.pokename))
                self.status.clear()
                sleep(1)
            else:
                print("{} is still paralyzed!".format(self.pokename))
                sleep(1)
        if "sleep" in self.status:
            sleepbreak=random.randint(1, 5)
            if sleepbreak==1:
                print("{} is awake!".format(self.pokename))
                self.status.clear()
                sleep(1)
        if "freeze" in self.status:
            thawout=random.randint(1, 5)
            if thawout==1:
                print("{} is thawed out of frozen!".format(self.pokename))
                self.status.clear()
                sleep(1)
            else:
                print("{} is still frozen solid.".format(self.pokename))
                sleep(1)
    
    def checkblock(self):                        #1 de 3 olasiliginda paralyze ken saldirabilir degistirilebilir
        abletoatt=0
        if self.status is "paralyze":
            abletoatt=random.randint(1, 3)
            print("{} is paralyzed!".format(self.pokename))
        elif self.status is "sleep":
            print("{} is fast asleep.\n'ZZZZZZZZZ'".format(self.pokename))
            block=1
        elif self.status is "freeze":
            print("It can't move.")
            block=1
        else:
            block=0
        if abletoatt==1 or abletoatt==2:
            print("{} is paralyzed!\nIt can't move!".format(self. pokename))
            block=1

def checkdead(self):
    if user.health <=0:
        print("{} you has been defeated!".format(user.pokename))
        return True

    if com.health <=0:
        print("{} you has been defeated!".format(com.pokename))
        return True

#           -------------Yapılacaklar!!!-------
#
#
#
#
#
#
#
#
#---------------------------------------------------------------------

def battle(user ,com , pokemonismi, enemy_pokemon):
    while user.health >0 or com.health >0:          #checkstatus u saldırının icine saldırıdan hemen önceye koydum

        f = open ("saldiri_kaydi.txt","a+")
        f.write ("Your " + pokemonismi + " has fought against " + enemy_pokemon + ".\r\n")

        moves = open("player_moves.txt" ,"r+")
        moves.read
        save_poke = open("save.txt","a+")
        save_poke.write (pokemonismi + " " + user.poketype + " " + str(moves))
        print(str(moves))
        print("Your turn! \n")
        user.attmove("user", com)
        if checkdead():
            print("You won!")
            f.write ("Your " + pokemonismi + " has won! \r\n")
            break

        if com.health >0:
            print("Opponent's turn! \n")
            waitdot(2)
            com.attmove('com', user)
            sleep(2)
            if checkdead():
                print("You lost...")   
                f.write ("Your " + pokemonismi + " has lost... \r\n")
                break



#Oyun sonunu yapmaya basla hareket addk ve test var.......