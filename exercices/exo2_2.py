#! /usr/bin/env python3
def calcul_moyenne(fichier):
    data = format_csv(fichier)
    age=[]
    note=[]
    key=[]
    for x, v in data.items():
        key.append(x)
        age.append(int(v[1]))
        note.append(float(v[2]))
    resultat=sum(age)/len(data)
    nom= key[note.index(max(note))]
    mnote = data[nom]
    with open("resultat.txt","w") as f:
        f.write(f"Moyenne d'âge des étudiants : {resultat} ans\n")
        f.write(f"Étudiant avec la meilleure moyenne :\n")
        f.write(f"Nom : {nom}\n")
        f.write(f"Prénom : {mnote[0]}\n")
        f.write(f"Âge : {mnote[1]}\n")
        f.write(f"Moyenne : {mnote[2]}\n")
        

def format_csv(fichier):
    resultat={}
    header=0
    with open(fichier,"r") as f:
        for i,x in enumerate(f):
            if i == 0:
                continue
            x = x.replace('\n', '')
            x = x.split(',')
            key, values = x[0], (x[1], x[2], x[3])
            resultat[key] = values
    return resultat
        
        
calcul_moyenne("etudiants.csv")