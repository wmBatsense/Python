#! /usr/bin/env Python3 
entiers=[]
mots=["salut","j'apprend","python","en","formation","c'est","pas","mal","merci","Docapost","A bientot :)"]    
#########boucle for ###########

def display_for():
    for t in range(1,11,1):
        if t == 11: break
        print(f'func for: {t}')
print("#########Fonction boucle for ###########")  
display_for()

#########boucle while ###########"  
def display_while(counter):
    t=1
    while t <= 10:
        print(f'func while: {t}')
        t+=1
        
print("#########Fonction boucle while ###########")  
display_while(9)

#########Fonction affiche entiers ###########
def affiche_entiers(tableau):
    global entiers
    for t in range(1,tableau,1):
        if t == 11: break
        print(t)
        entiers.append(t)
#########Fonction affiche mots ###########
def affichemots():
    for k in entiers:
        print(f'func: {mots[k]}')
        
#########Appel de fonction ###########
print("#########Fonction affiche entiers ###########")    
affiche_entiers(len(mots))
print("#########Fonction affiche mots ###########")
affichemots()