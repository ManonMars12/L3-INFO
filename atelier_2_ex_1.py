#Mars Manon L3 ST 
#Atelier de programmation 2 
#Exercice 1 

def somme_for_indices(L:list)->float:
    
    """
    Fais la somme des éléments d'une liste 
    Arg : L->list
    Return somme->float
    """
    
    somme=0
    for i in range (len(L)):
        somme=somme+L[i]
    return(somme)

def somme_for_elements(L:list)->float:
    
    """
    Fais la somme des éléments d'une liste 
    Arg : L->list
    Return somme->float
    """
    
    somme=0
    for e in L :
        somme=somme+e
    return(somme)

def somme_while(L:list)->float:
    
    """
    Fais la somme des éléments d'une liste 
    Arg : L->list
    Return somme->float
    """
    
    somme=0
    i=0
    while i<len(L):
        somme=somme+L[i]
        i=i+1
    return(somme)

#somme_for_element me parait la solution la plus adaptée 

def test_exercice1_for_indices()->None: 
    print("TEST SOMME")
#test liste vide
    print("Test liste vide : ", somme_for_indices([]))
#tests sommes
    lst2test1=[1,2,3, 4,5]
    print("Test somme 15 : ",  somme_for_elements(lst2test1))
    lst2test1=[1,10,100, 1000,10000]
    print("Test somme 1111 : ",  somme_for_indices(lst2test1))
    
def test_exercice1_for_elements()->None: 
    print("TEST SOMME")
#test liste vide
    print("Test liste vide : ", somme_for_elements([]))
#tests sommes
    lst2test1=[1,2,3, 4,5]
    print("Test somme 15 : ",  somme_for_elements(lst2test1))
    lst2test1=[1,10,100, 1000,10000]
    print("Test somme 1111 : ",  somme_for_indices(lst2test1))
    
def test_exercice1_while()->None: 
    print("TEST SOMME")
#test liste vide
    print("Test liste vide : ", somme_while([]))
#tests sommes
    lst2test1=[1,2,3, 4,5]
    print("Test somme 15 : ",  somme_while(lst2test1))
    lst2test1=[1,10,100, 1000,10000]
    print("Test somme 1111 : ",  somme_for_indices(lst2test1))


def moyenne(L:list)->float:
    
    """
    Calcule la moyenne des éléments d'une liste 
    Arg : L->list
    Return moy->float
    """
    
    if len(L)==0:
        moy=0
    else:
        somme=somme_for_elements(L)
        nb_elements=len(L)
        moy=somme/nb_elements
    return(moy)
    

def nb_sup_for_indices (L:list,e:float)->int:
    
    """
    Donne le nb d'élément superieur à l'élément e
    Arg : L->list
          e->float
    Return cpt->int
    """
    cpt=0
    for i in range(len(L)):
        if L[i]>e:
            cpt=cpt+1 
    return(cpt)


def nb_sup_for_elements (L:list,e:float)->int:
    
     
    """
    Donne le nb d'élément superieur à l'élément e
    Arg : L->list
          e->float
    Return cpt->int
    """
    
    cpt=0
    for e_liste in L :
        if e_liste>e:
            cpt=cpt+1 
    return(cpt)

def moy_sup (L:list,e:float)->float:
    
     
    """
    Donne la moyenne des éléments superieurs à l'élément e
    Arg : L->list
          e->float
    Return moy->float
    """
    somme=0
    if nb_sup_for_elements (L,e)==0 :
        moy=0
    else:
        for e_liste in L :
            if e_liste>e:
                somme=somme+e_liste
    moy=somme/nb_sup_for_elements(L,e)
    return(moy)
                
def val_max(L:list)->float:
    
     
    """
    Donne la valeur max des éléments d'une liste 
    Arg : L->list   
    Return maxi->float
    """
    max=0
    for e in L : 
        if e>max : 
            max=e 
    return(max)

def ind_val_max(L:list)->int:

    """
    Donne l'indice de la valeur max des éléments d'une liste 
    Arg : L->list   
    Return res->int
    """
    
    maxi=val_max(L)
    for i in range(len(L)):
        if maxi==L[i]:
            res=i
    return(res)
        