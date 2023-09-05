#! /usr/bin/env python3

def saisie_nombre():
    while True:
        try:
           nombre = input("Veuillez saisir un nombre :")
        except KeyboardInterrupt:
          print('KeyboardInterrupt ')
          
saisie_nombre()