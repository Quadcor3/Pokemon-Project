import random
from tools import *
import saldiri



class oyuncu():

    def __init__(self, isim, health=100):
        self.health=health
        self.pokename=isim
        self.poketype=input("Which of the following type is your Pokémon's?\nwater, fire, \n")   ## Typeları devam ettir ekledikçe!!
        self.saldiril=[]
        self.status=[]                        ## Bu da denemede
        print("oyuncu eklendi")

    def attmove(self, karsi):     # For player
        while True:
            att=input("What is your move?: ")
            if att in player.saldiril:
                getattr(saldiri, att)()
                break
            else:
                print("You do not have that move. Try again.")
        print("{} used {}!".format(self.pokename, att))
        if saldiri.dam==1:
            self.attdamage(karsi)
        elif saldiri.dam==0:
            self.attheal()
            
    def attdamage(self, karsi):
        waitdot(3)
        if saldiri.fail==1:
            print("But it failed!")
        else:
            statuseff()
            karsi.health-=saldiri.damage
            print("{} is hit for {} damage!".format(karsi.pokename, saldiri.damage))

    def attheal(self):
        waitdot(3)
        if saldiri.fail==1:
            print("But it failed!")
        else:
            self.health+=saldiri.heal
            if saldiri.statusheal==1:
                self.status.clear()
                print("All status effects has been healed!")
            print("{} have been healed for {} health".format(self.pokename, saldiri.heal))
        

    
    def ekleme(self):           # For player
        for i in range(1, 5):
            while True:
                x=input("{} icin {}. saldiriyi girin".format(self.pokename, i))
                if x in saldiri.saldirilar and saldiri.saldirilar[x] in self.poketype:
                    self.saldiril.append(x)
                    break
                else:
                    print("You can't select that move")


    def statuseff(self):         ### Statusler yaptıkça buraya da ekle!!
        if saldiri.burn==1:
            self.status.append('burn')





#print("Introduction...")
#sleep(2)
#playerP=input("Choose your pokemon:\n")
#playersaldirilari=starting()
#comsaldirilari=choosenemy()
#print(playersaldirilari, comsaldirilari)
#att=input("Yapacağın saldırıyı gir:\n")
#if att in playersaldirilari:
    #attmove(playerP, comhealth, att)




pokemonismi=input("Pokemonunuzun ismi:\n")
player=oyuncu(pokemonismi)
rakip_pokemon=input("rakip poke isim: ")
com=oyuncu(rakip_pokemon)
player.ekleme()
#checkstatus()  ##??
player.attmove(com)


#En son type halloldu yukardaki yeşil parça silinebilir(?) estetik hala sıfır, son commandleri bir core() ya da game() gibi function a atılabilir
#Statusler çalışıyor gibi damage ya da ne olacakları eklenmeli