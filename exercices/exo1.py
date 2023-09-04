#! /usr/bin/env Python3 
t=0
print("######### boucle fwhile ###########")
while t <= 9:
    t+=1
    print(t)
print("#########boucle for ###########")

for t in range(11):
    if t == 11: break
    print(t)
    
print("#########Fonction affiche mots ###########")
entier=[0,1,2,3,4,5,6,7,8,9,10]
mots=["salut","j'apprend","python","en","formation","c'est","pas","mal","merci","Docapost","A bientot :)"]
def affichemots():
    for k in entier:
        print(f'func: {mots[k]}')

affichemots()