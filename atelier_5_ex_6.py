#Mars Manon L3 ST
#Atelier de programmation 5 
#Exercice 7 

import random as rd 


def tri_stupide(liste:list)->list:
    
    """
    Trie une liste de manière aléatoire jusqu'à ce qu'elle soit triée.

    Args:
        liste (list): La liste à trier.

    Returns:
        list: La liste triée.
    """
    
    lst=liste.copy()
    while(lst != sorted(lst)):
        rd.shuffle(lst)
    return(lst) 

def tri_insertion(lst, n:int)->list:
    
    """
    Trie une liste en utilisant l'algorithme de tri par insertion.

    Args:
        lst (list): La liste à trier.
        n (int): La taille de la liste. Ce paramètre est redondant ici, car 
                  il est possible de déterminer la taille directement à partir 
                  de la liste. 

    Returns:
        list: La liste triée.
    """


    tab=lst.copy()
    for i in range(1, n-1):
        x=tab[i]
        j=i
        while j>0  and tab[j-1]>x:
            tab[j]=tab[j-1]
            j=j-1
        tab[j]=x
        
    return(tab)

def tri_selection(lst, n:int)->list:
    
    """
   Trie une liste en utilisant l'algorithme de tri par sélection.

   Args:
       lst (list): La liste à trier.
       n (int): La taille de la liste. Ce paramètre est redondant ici, car 
                 il est possible de déterminer la taille directement à partir 
                 de la liste.

   Returns:
       list: La liste triée.
   """
   
    tab=lst.copy()
    for i in range(len(tab)): #changement
        min=i
        for j in range(i+1, len(tab)): #changement
            if tab[j] < tab[min]:
                min =j
        if  min != i : 
            tab_i=tab[i]
            tab_min=tab[min]
            tab[i]=tab_min
            tab[min]=tab_i
    return(tab)
            
def tri_bulle(lst:list):
    
    """
   Trie une liste en utilisant l'algorithme de tri à bulles.

   Args:
       lst (list): La liste à trier.

   Returns:
       list: La liste triée.
   """
   
    tab=lst.copy()
    for i in range(len(tab)):
        for j in range(0, len(tab)-1):
            if tab[j+1] < tab[j]:
                val_tab_t_j1=tab[j+1]  
                val_tab_j=tab[j]
                tab[j+1]=val_tab_j
                tab[j]=val_tab_t_j1
    return(tab)

def tri_fusion(tab:list)->list:
    if len(tab)<= 1 : 
       return(tab)

    else : 
        return fusion(tri_fusion(tab[:(len(tab)//2)]), tri_fusion(tab[(len(tab)//2):]))
          


def fusion(A:list, B:list)->list:
    if A==[]:
        return(B)
    if B==[]:
        return(A)
    if A[0]<=B[0]:
        return [A[0]] + fusion(A[1:], B)
    else : 
        return [B[0]] + fusion(A, B[1:])
        

def merge_sort(liste:list)->list:
    tab=liste.copy()
    if len(tab)<= 1 : 
        return(tab)
    else : 
        return fusion(tri_fusion(tab[:(len(tab)//2)]), tri_fusion(tab[(len(tab)//2):]))
              


def merge(A:list, B:list)->list:
    if A==[]:
        return(B)
    if B==[]:
        return(A)
    if A[0]<=B[0]:
        return [A[0]] + fusion(A[1:], B)
    else : 
        return [B[0]] + fusion(A, B[1:])
            
    
#Je n'ai pas compris la différence entre tri_fusion() et merge_sort() mis-à-part la non modification de la liste de base 

#def tri_base(lst:list)->list: 
    
    
#Je n'arrive pas à trouver une logique pour continuer cet exercice 
    
def tri_base_ordre(ordre:int, lst:list)->list: 
    liste=lst.copy()
    int=[]
    aide=[[] for i in range(10)]
    for i in range(len(liste)):
        int.append(list(str(lst[i])))
    
    
    for i in range(len(int)):
        while len(int[i]) < ordre : 
            int[i].insert(0, "0")
        aide[[int[i][ordre]]].append(int[i])
    

    return(int, aide) 




