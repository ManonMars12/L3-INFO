#Mars Manon L3 ST 
#Atelier de programmation 4 
#Partie 2 

import numpy as np

def my_searchsorted(table:object,element:int )->int:
    
    """
    Trouve l'indice de l'élément dans un tableau trié. Si l'élément n'est pas présent, l'ajoute et retourne l'indice de la nouvelle occurrence.
    
    Args:
        table (np.ndarray): Tableau NumPy d'entiers triés.
        element (int): Valeur entière à rechercher ou à ajouter.
    
    Returns:
        int: L'indice de l'élément dans le tableau après l'avoir trié.
    """
    
    table=np.sort(table)
    place=[]
    for i in range(len(table)):
        if table[i]==element:
            place=np.append(place, i)
    if len(place)==0: 
        table=np.append(table,element)
        table=np.sort(table)
        for i in range(len(table)):
            if table[i]==element:
                place=np.append(place, i)    
    place=int(place[0])
    return(place)


def my_where(table:list or object, valeur:int)->list:
    
    """
    Trouve les indices des occurrences d'une valeur dans un tableau NumPy. 
    Fonctionne pour les tableaux unidimensionnels et bidimensionnels.
    
    Args:
        table (np.ndarray): Tableau NumPy à examiner.
        valeur (int): Valeur entière à rechercher.
    
    Returns:
        list: Liste des indices où la valeur apparaît dans le tableau. 
              Pour les tableaux bidimensionnels, retourne des tuples (i, j) où i et j sont les indices.
    """


    res=[]
    if table.ndim==1: #ndim nous donne la dimension d'un tableau numpy
        for i in range(len(table)):
            if table[i]==valeur:
                res.append(i)
    else : 
        for i in range(len(table)):
            for j in range(len(table)):
                if table[i,j]==valeur:
                    res.append((i,j))
    return(res)

def somme(a:object, b:object)->object: 
    
    """
    Additionne deux tableaux NumPy de même dimension. 
    Gère les tableaux unidimensionnels et bidimensionnels.
    
    Args:
        a (np.ndarray): Premier tableau NumPy à additionner.
        b (np.ndarray): Deuxième tableau NumPy à additionner.
    
    Returns:
        np.ndarray: Tableau résultant de la somme des éléments de a et b.
        str: Message d'erreur si les dimensions des tableaux ne correspondent pas.
    """
    
    if a.ndim==2 and b.ndim==2:
        res=np.zeros((len(a), len(a)))
        if a.shape==b.shape:
            for i in range(len(a)):
                for j in range(len(a)):
                    res[i,j]=a[i,j]+b[i,j]
            return(res)
                                  
        else : 
            return("Impossible, a et b n'ont pas la même dimension")
    elif a.ndim==1 and b.ndim==1: 
        res=np.zeros(len(a))
        if a.shape==b.shape:
            for i in range(len(a)):
                res[i]=a[i]+b[i]
            return(res)
        else : 
            return("Impossible, a et b n'ont pas la même dimension")
            
        
def somme_2(a:object, b:object)->object:
    
    """
    Additionne deux tableaux NumPy de même dimension en utilisant `ndenumerate` pour itérer sur les éléments.
    
    Args:
        a (np.ndarray): Premier tableau NumPy à additionner.
        b (np.ndarray): Deuxième tableau NumPy à additionner.
    
    Returns:
        np.ndarray: Tableau résultant de la somme des éléments de a et b.
        str: Message d'erreur si les dimensions des tableaux ne correspondent pas.
    """
    
    if a.ndim==2 and b.ndim==2:
        res=np.zeros((len(a), len(a)))
        if a.shape==b.shape:
            for (i, j), val in np.ndenumerate(a):                
                res[(i,j)]=a[(i,j)]+b[(i,j)]
            return(res)
                                  
        else : 
            return("Impossible, a et b n'ont pas la même dimension")
        
    elif a.ndim==1 and b.ndim==1: 
        res=np.zeros(len(a))
        if a.shape==b.shape:
            for i in np.ndenumerate(a):
                res[i]=a[i]+b[i]
            return(res)
        else : 
            return("Impossible, a et b n'ont pas la même dimension")

