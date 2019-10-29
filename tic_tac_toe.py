#!/usr/bin/python3
import random
winner = []
liste_felder = ["_","_","_","_","_","_","_","_","_"]
liste_d = [0,1,2,3,4,5,6,7,8]
def print_spielfeld(spielfeld):
    print(spielfeld[0]+"|"+spielfeld[1]+"|"+spielfeld[2])
    print(spielfeld[3]+"|"+spielfeld[4]+"|"+spielfeld[5])
    print(spielfeld[6]+"|"+spielfeld[7]+"|"+spielfeld[8])
def place_zeichen(spielfeld,zeichen,position):
    spielfeld[position] = zeichen
while True:
    print_spielfeld(liste_felder)
    try:
        position = int(input("Wahle eine Position zwischen 0 und 8."))
    except Exception as error:
        print(error)
    place_zeichen(liste_felder,"x",position)
    print_spielfeld(liste_felder)
