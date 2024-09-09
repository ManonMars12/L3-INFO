#Mars Manon L3 ST 
#Atelier de programmation 3
#Exercice 1

def full_name(str_arg:str)->str : #Paramètre = nom prénom 
    liste=str_arg.split()
    nom_maj=liste[0].upper()
    
    prenom=list(liste[1])
    prenom_maj=prenom[0].upper()
    prenom.pop(0)
    prenom ="".join(prenom) #recolle les éléments de la liste (inverse de split)
    res = nom_maj + " " + prenom_maj + prenom
    
    return(res)


def is_mail(str_arg:str)->(int,int):
    liste_mail=str_arg.split("@") #Sépare le nom de domaine + extension et le corps ATTENTION NE CONTIENT PAS LE @ 
    if len(liste_mail)<2 : 
        return ((0, 2))
       
    res_corps=validite_corps_mail(str_arg)
    res_domaine=validite_domaine_mail(str_arg)
    if res_corps==((0,0)) and res_domaine==((0,0)): 
        return((1,5))
    elif res_corps != (0,0):
        return res_corps  
    else : 
        return res_domaine
    


    
        
def validite_corps_mail(str_arg:str)->(int,int):
    liste_mail=str_arg.split("@") #Sépare le nom de domaine + extension et le corps ATTENTION NE CONTIENT PAS LE @ 
    corps=list(liste_mail[0])
    acceptables=[
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_', '@']
    if len(liste_mail)<2 : 
        return ((0,2))
    elif corps[0] == "." or corps[-1] == ".":
        return((0,1))
    for e in corps :
        if e not in acceptables : 
            return ((0,1))
        
    for i in range(len(corps)-1): #Discutable (on va rentrer dans le for quoi qu'il arrive)
        if corps[i]=="." and corps[i+1]=="." :
            return((0,1))
        
    else : 
        return(0,0) #Corps valide 
    
    
def validite_domaine_mail(str_arg:str)->(int,int):
    liste_mail=str_arg.split("@")#Sépare le nom de domaine + extension et le corps ATTENTION NE CONTIENT PAS LE @ 
    
    acceptables=[
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '.']
    if len(liste_mail)<2:
        return((0,2))
    
    domaine=list(liste_mail[1])
  
    
    if domaine[0]=="." or domaine[-1]=="." :
        return((0,3))
    
    for e in domaine :
        if e not in acceptables  :
            return ((0,3))
    
    for i in range(len(domaine)-1): #Discutable (on va rentrer dans le for quoi qu'il arrive)
        if domaine[i]=="." and domaine[i+1]=="." :
            return((0,3))
    if domaine[-3] != "." and domaine[-4] != "." :  #On part du principe que ce qu'il y a après le . est de 2 ou 3 lettres pas plus ni moins 
        return ((0,4))
    
    else :
        return(0,0) #Domaine valide 
   
    
    
def test_is_mail(str_arg:str)->str:
    if is_mail(str_arg)==((0,2)):
        return("Votre mail n'est pas valide, il doit contenir une @")
    elif is_mail(str_arg)==((0,1)):
        return("Votre mail n'est pas valide, le corps n'est pas valide")
    elif is_mail(str_arg)==((0,3)):
        return("Votre mail n'est pas valide, le domaine n'est pas valide")
    elif is_mail(str_arg)==((0,4)):
        return("Votre mail n'est pas valide, il manque le . ")
    else : 
        return("Votre mail est valide")

print(test_is_mail("mmars2ajaccio@gmail.com"))
print(test_is_mail("mmars2ajaccio#gmail.com"))
print(test_is_mail("mmars2ajaccio@gmailPOINTcom"))
print(test_is_mail("mmar+++s2ajaccio@gmail.com"))
print(test_is_mail("mmars2ajaccio@gmai++++l.com"))
