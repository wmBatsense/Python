#! /usr/bin/env python3

def ajout_commentaire(file):
    f = open(file, "r")
    content=""
    for x in f:
        content += "#ma ligne de commentaire\n"
        content +=x
    file = open(file,"w+")
    file.write(content)
    
ajout_commentaire("test.txt")

def compte_ligne_fichier(file):
    f = open(file, "r")
    nb_ligne=0
    nb_mots=0
    nb_caractere=0
    for x in f:
        liste_de_mot= x.split(" ")
        nb_ligne=nb_ligne+1
        nb_mots = nb_mots+len(liste_de_mot)
        nb_caractere = nb_caractere+len(x)
    print(f'nombre de lignes : {nb_ligne}')
    print(f'nombre de mots : {nb_mots}')
    print(f'nombre de caractères : {nb_caractere}')
compte_ligne_fichier("test.txt")