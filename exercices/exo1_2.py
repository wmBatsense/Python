#! /usr/bin/env python3

def chiffre_parfait(nombre):
    resultat=[]
    for diviseur in range(1,(nombre)+1):
        somme_diviseur=[]
        if nombre%diviseur == 0:
            somme_diviseur.append(diviseur)
            print(somme_diviseur)


chiffre_parfait(28)    