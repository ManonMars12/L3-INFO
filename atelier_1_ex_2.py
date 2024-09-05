#Mars Manon Fabbri Yohann L3 ST 
#Atelier de programmation 1 
#Exercice 2


def bissextile(annee:int)->bool:
    """Dis si une année est bissextile ou non.

   Args : 
       annee (int) : l'année à tester 
   Returns :
       booléen: résultat
       
   """
   # Une année est bissextile si elle est divisible par 4
   # mais pas divisible par 100, sauf si elle est divisible par 400.
   
    return(((annee%4==0 and annee%100!=0) or (annee%400==0))) 


def test_bissextile():
    """Teste la fonction bissextile().

   Args : 
       
   Returns :
       
   """
    annee=int(input("Veuillez entrer l'année (-1 si vous voulez arreter"))
    while annee != -1: 
        print(bissextile(annee))
        annee=int(input("Veuillez entrer l'année"))

    
    
    
    

