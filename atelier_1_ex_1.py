#Fabbri Yohann Mars Manon L3 ST 
#Atelier de programmation 1 
#Exercice 1 

def message_imc(imc:float)->str:
    """Evalue notre état corporel.

   Args : 
       imc (float) : l'IMC 
   Returns :
       message (str) : l'état corporel
   """
   
    bornes=[0, 16.5, 18.5,25,30,35,40, float('inf')]
    etats=["Dénutrition", "Maigreur", "Corpulence normale", "Surpoids", "Obsésité modérée", "Obésité sévère", "Obésité morbide"]
    
    if imc>40:
        message="Obésité morbide"
    else : 
        for i in range(0, 6): 
            if imc>bornes[i] and imc<=bornes[i+1]: 
                message=etats[i]
    return(message)


def test_imc():
    """Teste la fonction message_imc().

   Args : 
       
   Returns :
       
   """
    print(message_imc(14))
    print(message_imc(18.5))
    print(message_imc(25))
    print(message_imc(30))
    print(message_imc(35))
    print(message_imc(40))
    print(message_imc(42))
    imc=int(input("Veuillez entre votre IMC"))
    print(message_imc(imc))

    
def message_imc_while(imc:float)->str:
    """Evalue notre état corporel.

   Args : 
       imc (float) : l'IMC 
   Returns :
       message (str) : l'état corporel
   """
   
    bornes=[0, 16.5, 18.5,25,30,35,40, float('inf')]
    etats=["Dénutrition", "Maigreur", "Corpulence normale", "Surpoids", "Obsésité modérée", "Obésité sévère", "Obésité morbide"]
  
    i=0
    while imc > bornes[i]: 
        message=etats[i]
        i=i+1
    return(message)


def test_imc_while():
    """Teste la fonction message_imc().

   Args : 
       
   Returns :
       
   """
    print(message_imc_while(14))
    print(message_imc_while(18.5))
    print(message_imc_while(25))
    print(message_imc_while(30))
    print(message_imc_while(35))
    print(message_imc_while(40))
    print(message_imc_while(42))
    imc=int(input("Veuillez entre votre IMC"))
    print(message_imc_while(imc))

    

def message_imc_dico(imc:float)->str:
    """Evalue notre état corporel.

   Args : 
       imc (float) : l'IMC 
   Returns :
       message (str) : l'état corporel
   """

    DICO_IMC = {
        16.5 :"Dénutrition",
        18.5 :"Maigreur",
        25 : "Corpulence normale",
        30 : "Surpoid",
        35 : "Obsésité modérée",
        40 : "Obsésité sévère",
        float('inf') : "Obsésité morbide"
        }

    bornes_dico=list(DICO_IMC.keys())
    etats_dico=list(DICO_IMC.values())

    i=0
    while i<len(bornes_dico):
        if imc <= bornes_dico[i]:
            message=etats_dico[i]
            return(message)
        i=i+1


   
def test_imc_dico():
    """Teste la fonction message_imc().

   Args : 
       
   Returns :
       
   """
   
    print(message_imc_dico(14))
    print(message_imc_dico(18.5))
    print(message_imc_dico(25))
    print(message_imc_dico(30))
    print(message_imc_dico(35))
    print(message_imc_dico(40))
    print(message_imc_dico(42))
    imc=int(input("Veuillez entre votre IMC"))
    print(message_imc_dico(imc))






    
    
    

