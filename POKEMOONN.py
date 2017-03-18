import random
from tools import *
import saldiri
import os
from os import path
import shutil

block=0

class player():

    def __init__(self, isim, health=1000, typadv=1 ):
        self.health=health
        self.pokename=isim
        self.saldiri=[]
        self.status=[]
        self.typemod=typadv
        print("player added!")            #En son silinecek

    def player_type_pokemon(self):      # Type Decleration For player Pokemon
        while True:
            x=str.lower(input("Which of the following type is your Pokémon's?\n{} \n".format(saldiri.types)))  #Hata var if le seçmeyi sınırla  -  lowercase yapıldı
            if x in saldiri.types:
                print("Type accepted.")
                self.poketype = x
                break
            else:
                print("Pokemon type unknown.")
                
    def com_type_pokemon(self):         # Type Decleration For Computer Pokemon
        self.poketype=random.choice(saldiri.types)
        print("Your opponent is a {} type pokemon.".format(self.poketype))


    def attmove(self, yapan, karsi):     # For player and now for com too
        while True:
            if yapan=="player":
                att=input("What is your move?:\n{}".format(self.saldiri))
            if yapan=="com":
                att=random.choice(self.saldiri)
            if att in self.saldiri:
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
            
    
    def add(self):           # For player ----- ENSON ->ayni saldiriyi iki kere secememe yap---- Yapıldı!!
        for i in range(1, 5):
            while True:
                x=str.lower(input("{} icin {}. saldiriyi girin\n".format(self.pokename, i)))
                if x in saldiri.saldirilar:
                    if x in self.saldiri:
                        print("You can't select the same move.")
                    elif saldiri.saldirilar[x] in self.poketype or saldiri.saldirilar[x] is 'normal':
                        self.saldiri.append(x)
                        break
                    else:
                        print("You can't select that type of move!")
                else:
                    print("There is no such move!")

    def comadd(self):
        for i in range(1, 5):
            while True:
                k=random.choice(list(saldiri.saldirilar.keys()))
                if k not in self.saldiri and saldiri.saldirilar[k] in self.poketype or saldiri.saldirilar[k] is 'normal':
                    self.saldiri.append(k)
                    break


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
   
def checkdead():
    if player.health <=0:
        print("{} you has been defeated!".format(player.pokename))
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


pokemonismi=input("What is your Pokêmon's nickname? \n")
user=player(pokemonismi)
user.player_type_pokemon()
user.add()
enemy_pokemon=input("Who is your enemy? \n")                #aldigi tipe gore onceden belirlenmis isimler alabilir
com=player(enemy_pokemon)
com.com_type_pokemon()
com.comadd()

while user.health >0 or com.health >0:          #checkstatus u saldırının icine saldırıdan hemen önceye koydum

    f = open ("saldiri_kaydi.txt","a+")
    f.write ("Your" + pokemonismi + " has fought against " + enemy_pokemon + ".\r\n")

    save_poke = open("save.txt","a+")
    save_poke.write (pokemonismi )

    print("Your turn! \n")
    user.attmove('user', com)
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

        

sleep(10)




#Oyun sonunu yapmaya basla hareket addk ve test var.......