import saldiri
from tools import *


sozluk={'flame': 'fire', 'recovery': 'normal'}


class oyuncu():

    def __init__(self, isim, health=100):
        self.health=health
        self.pokename=isim
        self.poketype=input("Which of the following type is your Pokemon's?\nwater, fire, \n")   ## Typelar� devam ettir ekledik�e!!
        self.saldiril=[]
        self.status=[]                        ## Bu da denemede
        print("oyuncu eklendi")

player=oyuncu("sarp")
x=input("deneme")
if sozluk[x] in player.poketype and x in sozluk:
    print("dafuq")
else:
    print("sorun buymus")