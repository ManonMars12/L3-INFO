#Mars Manon L3 ST 
#Atelier de programmation 2 
#Exercice 2 

def position_for(lst:list,elt:int)->int:
    if elt not in lst :
        res=-1
    for i in range (len(lst)):
        if lst[i]==elt:
            res=i
    return(res)
        

def position_while(lst:list,elt:int)->int:
    i=0
    e_liste=float('inf')
    while i !=len(lst) and e_liste != elt : 
        if lst[i]==elt:
            res=i
            return(res)
        i=i+1
    if elt not in lst :
        res=-1
    return(res)


def nb_occurrences(lst:list,e:int)->int:
    cpt=0
    for e_liste in lst:
        if e_liste==e:
            cpt=cpt+1
    return(cpt)

def est_triee_for(lst:list)->bool:
    for i in range(len(lst)-1): #Pour ne pas avoir de out of range (à retenir)
        if lst[i]>lst[i+1]:
            return(False)
    else : 
        return(True)

            
def est_triee_while(lst:list)->bool:
    i=0
    while lst[i+1]>lst[i]:
        i=i+1
        if i==len(lst)-1: #Pour ne pas avoir de out of range (à retenir)
            return(True)
    return(False)
 
#Je pense que la meilleure version est celle avec le while car elle s'arrête dès que la liste n'est pas triée. 

def position_tri(lst:list, e:int)->int: #lst est supposée triée 
    debut=0
    fin=len(lst)-1
    while debut<=fin : 
        milieu=(debut+fin)//2
        if lst[milieu] == e : 
            return(milieu)
        elif lst[milieu] < e : 
            debut=milieu+1
        else :
            fin=milieu-1
    return(-1)
        

def a_repetition(lst:list)->bool:
    T=[]
    i=0
    while i<len(lst):
        if lst[i] not in T:
            T.append(lst[i])
            if len(T)==len(lst):
                return(False)
        else : 
            return(True)
        
        i=i+1
   
        
    
    
    
        
        
        