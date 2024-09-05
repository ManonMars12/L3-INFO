#Mars Manon L3 ST 
#Atelier de programmation 2
#Exercice 4 

import matplotlib.pyplot as plt


def nb_occurrences(lst:list,e:int)->int:
    cpt=0
    for e_liste in lst:
        if e_liste==e:
            cpt=cpt+1
    return(cpt)

def val_max(L:list)->float:
    
    max=0
    for e in L : 
        if e>max : 
            max=e 
    return(max)



def histo(F:list)->list:
    H=[]
    maximum=val_max(F)
    for i in range (0, maximum+1):
        nb_occ_elmt = nb_occurrences(F, i)
        H.append(nb_occ_elmt)
    return(H)



def est_injective(F:list)->bool:
    liste_occurences=histo(F)
    for i in range (len(liste_occurences)):
        if liste_occurences[i]>1 : 
            return(False)
    return(True)

def est_surjective(F:list)->bool:
    liste_occurences=histo(F)
    for i in range (len(liste_occurences)):
        if liste_occurences[i]==0 : 
            return(False)
    return(True)
    

def est_bijective(F:list)->bool:
    return(est_injective(F) and est_surjective(F))


def affiche_histo(F:list)->None:
    print("TEST HISTOGRAMME")
    H=histo(F)
    print(F)
    print(H)
    print("HISTOGRAMME")
    H=histo(F)
    MAXOCC=val_max(H)

    for i in range(MAXOCC):
        res=""
        for e in H:
            if (e >= MAXOCC-i) :
               res = res + " # "
            else : 
                res = res + "   "
        print(res)
        
    res=""
    for i in range(len(H)):
        res=res+ " " + str(i) + " "
    print(res)
    
def affiche_histo_2(F:list)->None: 
    print(F)
    x = histo(F)
    print(x)
    MAXOCC=val_max(x)
    plt.hist(F, bins=range(0, val_max(F)+1), edgecolor="black") #+1 pour lisibilité du plot 
    plt.xticks(range(0, val_max(F) + 1)) #pour les graduations 
    edgecolor = ('black')
    plt.title('Histogramme')
    plt.axis([0, val_max(F), 0, MAXOCC])