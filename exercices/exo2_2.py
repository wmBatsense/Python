#! /usr/bin/env python3

def calcul_moyenne(fichier):
    data = format_csv(fichier)
    age,note,key=[],[],[]
    for x, v in data.items():
        key.append(x)
        age.append(int(v[1]))
        note.append(float(v[2]))
    resultat=sum(age)/len(data)
    nom= key[note.index(max(note))]
    mnote = data[nom]
    recupere_resultat(nom,resultat,mnote)
    
    
def recupere_resultat(nom,moyenne,etudiant):
    try:
      with open("resultat.txt","w") as f:
        f.write(f"Moyenne d'âge des étudiants : {moyenne} ans\n")
        f.write(f"Étudiant avec la meilleure moyenne :\n")
        f.write(f"Nom : {nom}\n")
        f.write(f"Prénom : {etudiant[0]}\n")
        f.write(f"Âge : {etudiant[1]}\n")
        f.write(f"Moyenne : {etudiant[2]}\n")
    except:
      print('Fichier de resultat introuvable !')

        

def format_csv(fichier):
    resultat={}
    try:
        with open(fichier,"r") as f:
            for i,x in enumerate(f):
                if i == 0:
                    continue
                x = x.replace('\n', '')
                x = x.split(',')
                key, values = x[0], (x[1], x[2], x[3])
                resultat[key] = values
        return resultat
    except:
      print("Fichier de d'entrée introuvable !")
        
calcul_moyenne("etudiants.csv")