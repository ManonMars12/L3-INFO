#Mars Manon L3 ST 
#Atelier de programmation 3 
#Exercice 4 

def mot_correspond(mot:str, motif:str)->bool:
    """
    Renvoie si un motif correspond à un mot (ou inversement)
    Args : mot->str
           motif->str
    Return : res->bool
    """

    liste_mot=list(mot)
    liste_motif=list(motif)
    res=True
    if len(liste_mot) != len(liste_motif):
        return(False) #OK
    else :
        for i in range(len(liste_mot)):
            if liste_motif[i] != "." :
                if (liste_mot[i]!=liste_motif[i]):
                    res=False
                    
    return(res)

def presente(lettre:str, mot:str)->int: 
    """
    Renvoie la position d'une lettre dans un mot'
    Args : mot->str
           lettre->str
    Return : ->int
    """
    liste_mot=list(mot)
    for i in range(len(liste_mot)):
        if liste_mot[i]==lettre:
            return(i)
    return(-1)

def dictionnaire(fichier:str)->list:
    """
    Créer une liste avec les mots d'un fichier texte
    Arg : fichier->str
    Return liste_res-> liste
    """
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
    

def mots_Nlettres(lst_mots:list, n:int)->list:
    """
    Créer une liste avec les mots de n lettres présents dans la liste placée en argument
    Arg : lst_mots->list
          n:int
    Return res-> list
    """
    res=[]
    for i in range(len(lst_mots)):
        liste_detail=list(lst_mots[i])
        if len(liste_detail)==n:
            res.append(lst_mots[i])
    return(res)

def mot_possible(mot:str, lettres:str)->bool:
    liste_mot=list(mot)
    liste_lettres=list(lettres)
    for e in liste_mot:
        if e not in liste_lettres :
            return(False)
        else : 
            liste_lettres.remove(e) 
    return(True)

def mot_optimaux(dico:list, lettres:str)->list:
    """
    Créer une liste avec les mots optimaux qui pourraient être joués
    Arg : dico->list
    lettres:list
    Return res-> list
    """
    
    res_total=[]
    liste_lettres=list(lettres)
    len_max=0
    
    for i in range(len(liste_lettres)):
        liste_mot_n_lettres=mots_Nlettres(dico, len(liste_lettres)-i)
        for e in liste_mot_n_lettres : 
            if mot_possible(e,lettres):
                res_total.append(e)
                
    for e in res_total : 
        mot_courant=list(e)
        if len(mot_courant)>len_max:
            len_max=len(mot_courant)
            
    res_opti=[mot for mot in res_total if len(mot)==len_max] #Liste en compréhension : on rajoute l'élément de res_total si sa len est maximale et cela boucle sur tout les mots de res_total
    return(res_opti)
        
dico=dictionnaire("littre.txt")
print(mot_optimaux(dico, "aftezdhgsjqbknl"))




