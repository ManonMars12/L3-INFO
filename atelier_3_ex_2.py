#Mars Manon L3 ST 
#Atelier de programmation 3 
#exercice 2 

def mots_Nlettres(lst_mots:list, n:int)->list:
    res=[]
    for i in range(len(lst_mots)):
        liste_detail=list(lst_mots[i])
        if len(liste_detail)==n:
            res.append(lst_mots[i])
    return(res)
        
def commence_par(prefixe:str, mot:str)->bool:
    liste_mot=list(mot)
    liste_prefixe=list(prefixe)
    for i in range(len(prefixe)):
        if liste_mot[i] != liste_prefixe[i]:
            return(False)
    return (True)
    
def finit_par(suffixe:str, mot:str)->bool:
    liste_mot=list(mot)
    liste_suffixe=list(suffixe)
    for i in range(len(suffixe)):
        if liste_mot[-(i+1)] != liste_suffixe[-(i+1)]: #On commence par -1 (la fin)
            return(False)
    return (True)

def finissent_par(suffixe:str, lst_mots:list,)->list:
    res=[]
    for i in range(len(lst_mots)):
        if finit_par(suffixe, lst_mots[i]):
            res.append(lst_mots[i])
    return(res)

def commencent_par(prefixe:str, lst_mots:list,)->list:
    res=[]
    for i in range(len(lst_mots)):
        if commence_par(prefixe, lst_mots[i]):
            res.append(lst_mots[i])
    return(res)

def liste_mots(lst_mots:list,prefixe:str, suffixe:str, n:int):
    mots_prefixes_ok=commencent_par(lst_mots, prefixe)
    mots_pre_et_suf_ok=finissent_par(suffixe, mots_prefixes_ok)
    mots_tout_ok=mots_Nlettres(mots_pre_et_suf_ok, n)
    return(mots_tout_ok)

def dictionnaire(fichier:str)->list:
    f=open(fichier,"r")  # ouverture du fichier en lecture (r=read) 
    liste=[]
    c=f.readline() #lecture d'une ligne dans une chaine de caractères
    while c!="" :
        liste.append(c)
        c=f.readline() 
    liste_res=[]
    for i in range(len(liste)):
        liste_element = list(liste[i])
        liste_element.pop(len(liste_element)-1)
        element="".join(liste_element)
        liste_res.append(element)   
    return(liste_res)
    
    
def test()->None: 
    lst_mots=[]
    n=int(input("Veuillez entrer un nombre de lettres"))
    for i in range(0,4):
        un_mot=str(input("Veuillez entrer un mot"))
        lst_mots.append(un_mot)  
    mots_Nlettres(lst_mots,n)
    
    prefixe=str(input("Veuillez entrer un préfixe"))
    mot=str(input("Veuillez entrer un mot"))
    commence_par(prefixe, mot)
    
    mot=str(input("Veuillez entrer un mot"))
    suffixe=str(input("Veuillez entrer un suffixe"))
    finit_par(suffixe, mot)
    
    suffixe=str(input("Veuillez entrer un suffixe"))
    for i in range(0,4):
        un_mot=str(input("Veuillez entrer un mot"))
        lst_mots.append(un_mot)
    finissent_par(suffixe, lst_mots)
    
    prefixe=str(input("Veuillez entrer un préfixe"))
    for i in range(0,4):
        un_mot=str(input("Veuillez entrer un mot"))
        lst_mots.append(un_mot)
    commencent_par(prefixe, lst_mots)
    
    prefixe=str(input("Veuillez entrer un préfixe"))
    suffixe=str(input("Veuillez entrer un suffixe"))
    n=int(input("Veuillez entrer un nombre de lettres"))
    for i in range(0,4):
        un_mot=str(input("Veuillez entrer un mot"))
        lst_mots.append(un_mot)  
    liste_mots(lst_mots,prefixe, suffixe, n)
    
    dictionnaire("mots.txt")

