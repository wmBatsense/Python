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
    print(len(f.readlines()))
    
compte_ligne_fichier("test.txt")