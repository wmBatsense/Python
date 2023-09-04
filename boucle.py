month ={1:"Janvier",2:"Février",3:"Mars",4:"Avril",5:"Mai",6:"Juin",7:"juillet",8:"Aout",9:"Septembre",10:"Octobre"}
for m in month :
    if m > 6:
        break
    print(f'le {m} est le mois {month[m]}')
    
#Items function
print("################## Function Items ################")
for k,v  in month.items() :
    if k > 6:
        break
    print(f'le {k} est le mois {v}')