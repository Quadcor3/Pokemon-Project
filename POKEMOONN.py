import random
from tools import *
import saldiri



class oyuncu():

    def __init__(self, isim, health=100):
        self.health=health
        self.pokename=isim
        self.saldiril=[]
        self.status=[]
        print("oyuncu eklendi")            #En son silinecek

    def poketypebelirle(self):      # For player
        x=str.lower(input("Which of the following type is your Pokémon's?\n{} \n".format(saldiri.types)))  #Hata var if le seçmeyi sınırla  -  lowercase yapıldı
        if x in saldiri.types:
             print("Type accepted.")
        else:
             print("Pokemon type unknown.")

    def compoketypebelirle(self):
        self.poketype=random.choice(saldiri.types)
        print("Your opponent is a {} type pokemon.".format(self.poketype))


    def attmove(self, yapan, karsi):     # For player and now for com too
        while True:
            if yapan=="player":
                att=input("What is your move?:\n{}".format(self.saldiril))
            if yapan=="com":
                att=random.choice(self.saldiril)
            if att in self.saldiril:
                getattr(saldiri, att)()   #saldiri.(kullanıcı inputu)  yapmaya yarıyo
                break
            else:
                print("Select a valid move!")
                sleep(1)
        self.checkstatus()
        self.checkblock()
        if saldiri.block==0:
            print("{} used {}!".format(self.pokename, att))
            if saldiri.dam==1:
                self.attdamage(karsi)
            elif saldiri.dam==0:
                self.attheal()
            elif saldiri.dam==2:
                karsi.statuseff()
            
    def attdamage(self, karsi):   #for both
        waitdot(3)
        if saldiri.fail==1:
            print("But it failed!")
            saldiri.reseteffs()
        else:
            karsi.health-=saldiri.damage
            print("{} is hit for {} damage!".format(karsi.pokename, saldiri.damage))
            karsi.statuseff()

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
            
    
    def ekleme(self):           # For player ----- ENSON ->ayni saldiriyi iki kere secememe yap---- Yapıldı!!
        for i in range(1, 5):
            while True:
                x=str.lower(input("{} icin {}. saldiriyi girin\n".format(self.pokename, i)))
                if x in saldiri.saldirilar:
                    if x in self.saldiril:
                        print("You can't select the same move.")
                    elif saldiri.saldirilar[x] in self.poketype or saldiri.saldirilar[x] is 'normal':
                        self.saldiril.append(x)
                        break
                    else:
                        print("You can't select that type of move!")
                else:
                    print("There is no such move!")

    def comekleme(self):
        for i in range(1, 5):
            while True:
                k=random.choice(list(saldiri.saldirilar.keys()))
                if k not in self.saldiril and saldiri.saldirilar[k] in self.poketype or saldiri.saldirilar[k] is 'normal':
                    self.saldiril.append(k)
                    break


    def statuseff(self):         ### Statusler yaptıkça buraya da ekle!!
        if saldiri.burn==1:
            self.status.clear()
            self.status.append('burn')
            print("{} is burnt!".format(self.pokename))
            saldiri.burn=0
        if saldiri.paralyze==1:
            self.status.clear()
            self.status.append('paralyze')
            print("{} is paralyzed! It may be unable to move!".format(self.pokename))
            saldiri.paralyze=0
        if saldiri.sleep==1:
            self.status.clear()
            self.status.append('sleep')
            print("{} fell asleep!".format(self.pokename))
            saldiri.sleep=0
        if saldiri.freeze==1:
            self.status.clear()
            self.status.append('freeze')
            print("{} is frozen solid! It can't move!".format(self.pokename))
            saldiri.freeze=0

    def checkstatus(self):
        if self.status is "burn":
            burnbreak=random.randint(1, 5)               # 1 de 5 kurtulma olasiligi fazla mi?
            if burnbreak==1:
                print("{} is no longer burnt!".format(self.pokename))
                self.status.clear()
                sleep(1)
            else:
                burndamage=random.randint(5, 15)
                self.health-=burndamage
                print("{} is hurt by its burn!\nTook {} damage!".format(self.pokename, burndamage))
        if self.status is "paralyze":
            paralyzebreak=random.randint(1, 3)                  #paralyze den kurtulma sansi 1 de 3
            if paralyzebreak==1:
                print("{} is no longer paralyzed!".format(self.pokename))
                self.status.clear()
                sleep(1)
            else:
                print("{} is still paralyzed!".format(self.pokename))
                sleep(1)
        if self.status is "sleep":
            sleepbreak=random.randint(1, 3)
            if sleepbreak==1:
                print("{} is awake!".format(self.pokename))
                self.status.clear()
                sleep(1)
        if self.status is "freeze":
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
            saldiri.block=1
        elif self.status is "freeze":
            print("It can't move.")
            saldiri.block=1
        else:
            saldiri.block=0
        if abletoatt==1 or abletoatt==2:
            print("{} is paralyzed!\nIt can't move!".format(self. pokename))
            saldiri.block=1

            


#pokemonismi=input("Pokemonunuzun ismi:\n")
#player=oyuncu(pokemonismi)
#rakip_pokemon=input("rakip poke isim: ")
#com=oyuncu(rakip_pokemon)
#player.ekleme()
#checkstatus()  ##??
#player.attmove(com)

pokemonismi=input("Pokemonunuzun ismi:\n")
player=oyuncu(pokemonismi)
player.poketypebelirle()
player.ekleme()
rakip_pokemon=input("Rakip poke isim: ")                #aldigi tipe gore onceden belirlenmis isimler alabilir
com=oyuncu(rakip_pokemon)
com.compoketypebelirle()
com.comekleme()

while player.health >0 or com.health >0:          #checkstatus u saldırının icine saldırıdan hemen önceye koydum
    print("Your turn!!")
    player.attmove('player', com)
    if com.health >0:
        print("Opponent's turn...")
        waitdot(2)
        com.attmove('com', player)
        sleep(2)


if player.health <=0:
    print("{} you has been defeated!".format(player.pokename))

if com.health <=0:
    print("{} you has been defeated!".format(com.pokename))



#Oyun sonunu yapmaya basla hareket eklemek ve test var.......