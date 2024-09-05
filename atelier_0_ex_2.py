#Mars Manon L3 ST 
#Atelier de programmation 0 
#Exercice 2


poids=int(input("Entrez le poids d'envoi en grammes"))

if poids > 250 : 
    type_envoi=input("Entrez votre type d'envoi : verte/prioritaire (votre colis est trop lourd pour un ecopli)")
else :
    type_envoi=input("Entrez votre type d'envoi : verte/prioritaire/ecopli")


if type_envoi=='verte' : 
    if poids < 20 :
        prix=1.16
    elif poids < 100 : 
        prix = 2.32
    elif poids < 250:
        prix = 4 
    elif poids < 500 :
        prix = 6
    elif poids < 1000:
        prix = 7.50
    elif poids < 3000 :
        prix = 10.50
        
elif type_envoi=='prioritaire' : #Mettre des elif car exclusif 
    if poids < 20 :
        prix=1.43
    elif poids < 100 : 
        prix = 2.86
    elif poids < 250:
        prix = 5.26
    elif poids < 500 :
        prix = 7.89
    elif poids < 3000 :
        prix = 11.44

    
elif type_envoi=='ecopli' : 
    if poids < 20 :
        prix=1.14
    elif poids < 100 : 
        prix = 2.28
    elif poids < 250:
        prix = 3.92
        
sticker_suivi=input("Voulez-vous un sticker suivi o/n")

if sticker_suivi=='o':
    prix=prix+0.50
        
print ("Le prix de votre envoi est de", prix , "€")

