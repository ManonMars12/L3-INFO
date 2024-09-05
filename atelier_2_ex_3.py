#Mars Manon L3 ST 
#Atelier de programmation 2 
#Exercice 3 

def separer(L:list)->list:
    LSEP=[]
    cpt=0
    for i in range(len(L)):
        if L[i]<0 :
            LSEP.insert(0, L[i])
            cpt=cpt+1
        elif L[i]>0 : 
            LSEP.append(L[i]) 
        else : 
            LSEP.insert(cpt, 0)
                    
    return(LSEP)

def test_separer()->None:
    test=[0, 2, -1, 0, -3, 4, 4, 0, 3]
    print(test)
    print(separer(test))
