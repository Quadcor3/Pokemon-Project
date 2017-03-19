import random
from tools import *
import saldiri
import os
from os import path
import shutil
import Battle

class player() :

    #Initial
    def __init__(self, isim, health=1000, typadv=1 ):
        self.health=health
        self.pokename=isim
        self.saldiri=[]
        self.status=[]
        print("Player added!")


    #Type Declaration
    def player_type_pokemon(self):     
        while True:
            x=str.lower(input("Which of the following type is your Pokemon's?\n{} \n".format(saldiri.types))) 
            if x in saldiri.types:
                print("Type accepted.")
                self.poketype = x
                break
            else:
                print("Pokemon type unknown.")               
    def com_type_pokemon(self):         
        self.poketype=random.choice(saldiri.types)
        print("Your opponent is a {} type pokemon.".format(self.poketype))

    #Adding User and Computer

    def add(self):
        for i in range(1, 5):
            while True:
                x=str.lower(input("{} icin {}. saldiriyi girin\n".format(self.pokename, i)))
                if x== "debug":
                    print("Selecting moves automatically")
                    waitdot(3)
                    self.saldiri.append("ember")
                    self.saldiri.append("flamethrower")
                    self.saldiri.append("recovery")
                    self.saldiri.append("inferno")
                    print("Saldirilar: ", self.saldiri)
                    break
                elif x in saldiri.saldirilar:
                    if x in self.saldiri:
                        print("You can't select the same move.")
                    elif saldiri.saldirilar[x] in self.poketype or saldiri.saldirilar[x] is 'normal':
                        self.saldiri.append(x)
                        break
                    else:
                        print("You can't select that type of move!")
                else:
                    print("There is no such move!")
            if x == "debug":
                break
        moves=open("player_moves.txt" , "a+")
        moves.write (str(self.saldiri))
    def comadd(self):
        for i in range(1, 5):
            while True:
                k=random.choice(list(saldiri.saldirilar.keys()))
                if k not in self.saldiri and saldiri.saldirilar[k] in self.poketype or saldiri.saldirilar[k] is 'normal':
                    self.saldiri.append(k)
                    break

                
                #Beginning

pokemonismi=input("What is your Pokemon's nickname? \n")
user=player(pokemonismi)
user.player_type_pokemon()
user.add()
enemy_pokemon=input("Who is your enemy? \n")           
com=player(enemy_pokemon)
com.com_type_pokemon()
com.comadd()
Battle.battle(user ,com , pokemonismi, enemy_pokemon)