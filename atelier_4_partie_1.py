#Manon Mars L3 ST 
#Atelier de programmation 4 
#Partie 1 

def somme(lst:list)->float:
    
    """
    Calcule la somme des éléments d'une liste de nombres en utilisant la récursivité.

    Args:
        lst (list): Une liste de nombres flottants ou entiers.

    Returns:
        float: La somme de tous les éléments de la liste.
    """
    
    if len(lst)==1:
        return(lst[0])
    else :
        return(lst[0]+somme(lst[1:]))
    
def factorielle(n:int)->int:
    
    """
   Calcule la factorielle d'un entier donné en utilisant la récursivité.

   Args:
       n (int): Un entier positif.

   Returns:
       int: La factorielle de l'entier `n` (n!).
   """
   
    if n==0:
        return(1)
    else :
        return(n*factorielle(n-1))
    
def longueur(lst:list)->int:
    
    """
    Calcule la longueur d'une liste de manière récursive.

    Args:
        lst (list): Une liste d'éléments.

    Returns:
        int: La longueur de la liste.
    """
    
    if len(lst)==0:
        return(0)
    else : 
        lst_rec=lst[1:]
        return(1+len(lst_rec))

def minimum(lst:list)->float:
    
    """
    Trouve l'élément minimum d'une liste de nombres de manière récursive.

    Args:
        lst (list): Une liste de nombres flottants ou entiers.

    Returns:
        float: Le plus petit élément de la liste, ou +inf si la liste est vide.
    """ 
    
    if lst==[]:
        mini=float('+inf')
        return(mini)
    elif len(lst)==1:
        mini=lst[0]
        return(mini)
    else : 
        mini=lst[0]
        mini_rec=minimum(lst[1:])
        if mini_rec<mini:
            mini=mini_rec
    return(mini) 

def listPair(lst:list)->list:
    
    """
    Retourne une liste contenant uniquement les éléments pairs d'une liste donnée en utilisant la récursivité.

    Args:
        lst (list): Une liste d'entiers.

    Returns:
        list: Une nouvelle liste contenant uniquement les éléments pairs de `lst`.
    """ 
    
    if lst==[]:
        return([])
    elif len(lst)==1:
        if lst[0]%2==0:
            return([lst[0]])  
        else : 
            return([])
    else : 
        if lst[0]%2==0:
            return[lst[0]] + listPair(lst[1:]) #fais une seule liste avec les 2 
        else : 
            return(listPair(lst[1:]))

def concat_liste(lst:list)->list:
    
    """
    Aplati une liste imbriquée de manière récursive.

    Args:
        lst (list): Une liste d'éléments qui peuvent être des listes.

    Returns:
        list: Une liste aplatie avec tous les éléments de `lst`.
    """
    
    if lst==[]:
        return([])
    elif type(lst[0])==list:
        return (concat_liste(lst[0]) + concat_liste(lst[1:]))
    else : 
        return ([lst[0]]+ concat_liste(lst[1:]))

def incluse(l1:list, l2:list)->bool:
    
    """
    Vérifie si tous les éléments de la liste `l1` sont inclus dans la liste `l2` dans le même ordre à l'aide de la récursivité.

    Args:
        l1 (list): Une liste d'éléments à vérifier.
        l2 (list): Une liste dans laquelle chercher les éléments de `l1`.

    Returns:
        bool: True si tous les éléments de `l1` sont présents dans `l2` dans le même ordre, False sinon.
    """
        
    if l1==[]:
        return(True)
    if l2==[] and l1 != []:
        return(False)
    
    if l1[0] in l2 : 
        for i in range(len(l2)):
            if l2[i]==l1[0]:
                place=i
        return(incluse(l1[1:], l2[place:]))
    else :  
        return(False)

