import random
from tools import *
import saldiri



class oyuncu():

    def __init__(self, isim, health=100):
        self.health=health
        self.pokename=isim
        poketypebelirle()
        self.saldiril=[]
        self.status=[]                        # Bu da denemede
        print("oyuncu eklendi")            #En son silinecek

    def poketypebelirle(self):      # For player and com
        if self=='player':
            self.poketype=input("Which of the following type is your Pokémon's?\n{} \n".format(saldiri.types))   ## Typeları devam ettir ekledikçe!!
        elif self=='com':
            self.poketype=random.choice(saldiri.types)
            print("Your opponent is a {} type pokemon.".format(self.poketype))


    def attmove(self, karsi):     # For player -- com icin ekleme çalışması!! --
        while True:
            if self=="player":
                att=input("What is your move?: ")
            elif self=="com":
                att=random.choice     ##raastgele nasi saldiri eklenecek düsün! --- Simdilik belli basli olsun sonra eklicem!!
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
            self.statuseff()
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
                if x in saldiri.saldirilar and (saldiri.saldirilar[x] in self.poketype or 'normal'):
                    self.saldiril.append(x)
                    break
                else:
                    print("You can't select that move")


    def statuseff(self):         ### Statusler yaptıkça buraya da ekle!!
        if saldiri.burn==1:
            self.status.append('burn')
            del saldiri.burn
        if saldiri.paralyze==1:
            self.status.append('paralyze')
            del saldiri.paralyze







#pokemonismi=input("Pokemonunuzun ismi:\n")
#player=oyuncu(pokemonismi)
#rakip_pokemon=input("rakip poke isim: ")
#com=oyuncu(rakip_pokemon)
#player.ekleme()
#checkstatus()  ##??
#player.attmove(com)

def start():
    pokemonismi=input("Pokemonunuzun ismi:\n")
    player=oyuncu(pokemonismi)
    player.poketypebelirle()
    rakip_pokemon=input("Rakip poke isim: ")
    com=oyuncu(rakip_pokemon)
    com.poketypebelirle()

def turns():
    d






#En son type halloldu yukardaki yeşil parça silinebilir(?) estetik hala sıfır, son commandleri bir core() ya da game() gibi function a atılabilir
#Statusler çalışıyor gibi damage ya da ne olacakları eklenmeli