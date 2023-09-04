#! /usr/bin/env python3

import random
import time

chiffre_secret = random.randint(1,100)
compteur_tentative=0
now = time.time()

print("Bienvenue dans chiffre secret !")
print("essaye de trouver le nombre secret en peu de tentative")

while True:
    nombre = input("Entrez un chiffre:")
    if type(nombre) != int:
      print("Petit malin c'est un nombre qui faut :)")  
      continue
    compteur_tentative +=1
    if int(nombre) == chiffre_secret :
        print(f'Super tu as trouvé en {compteur_tentative} tentative et {int(now % 60)} seconde')  
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