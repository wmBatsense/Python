#! /usr/bin/env python3

import random
import time

chiffre_secret = random.randint(1,100)
compteur_tentative=0
now = time.time()
indice = 3

print("Bienvenue dans chiffre secret !")
print("essaye de trouver le nombre secret en peu de tentative")
print("tu peux utiliser des indices en tapant i, 3 indice maximum")

while True:
    try:
        nombre = int(input("Entrez un chiffre 1-100 ou 0 pour indice:"))
        if nombre == 0 and indice > 0:
            print(f"Le chiffre se trouve entre {chiffre_secret-5} et {chiffre_secret+10}")
            indice -=1
            continue
    except:
        print("Petit malin c'est un nombre qu'il faut :)")  
        continue
    compteur_tentative +=1
    if int(nombre) == chiffre_secret :
        print(f'Super tu as trouvé en {compteur_tentative} tentative et {int(now % 60)} seconde avec {indice} indice')  
        break    
    if int(nombre) < chiffre_secret:
        print(f'Humm chiffre trop bas')
        continue
    if int(nombre) > chiffre_secret:
        print(f'Humm chiffre trop haut')
        continue
    if int(compteur_tentative) > 10:
        print(f'Humm tu es à la {compteur_tentative} tentative')
        continue
    
print("Tu es un champion :) !")