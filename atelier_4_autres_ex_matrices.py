#Mars Manon L3 ST 
#Atelier de programmation 4 
#Autres exercices sur les matrices 



import numpy as np 
import random

#Exercice 1 

matrice=np.array(([0,0,0],[0,0,0],[0,0,0]))
cpt=1
for i in range(len(matrice)):
    for j in range(len(matrice)):
        matrice[i,j]=cpt
        cpt=cpt+1
print(matrice)

for i in range(len(matrice)):
    for j in range(len(matrice)):
        matrice[i,j]=matrice[i,j]+10
print(matrice)

for i in range(len(matrice)):
    for j in range(len(matrice)):
        matrice[i,j]=matrice[i,j]*2
print(matrice)


print(matrice[1]) #ligne
print(matrice[:, 2]) #colonne

matrice=np.delete(matrice, 2, axis=1) #axis=1 : colonne, axis=0 : ligne 
matrice=np.delete(matrice, 2, axis=0)
print(matrice)

#Exercice 2 

mat=np.random.randint(0,11, size=(4,4))
print(mat)
id=np.zeros((4,4),dtype=int) #dtype=int car sinon on a des float et donc des . dans la matrice 
for i in range(len(id)):
    for j in range(len(id)):
        if i==j : 
            id[i,j]=1
print(id)

def matrice_trace(matrice:object)->int:
    
    """
    Calcule la somme des éléments diagonaux d'une matrice.
    
    :param matrice: Matrice pour laquelle calculer la trace.
    :return: Somme des éléments diagonaux de la matrice.
    """
    
    res=0
    for i in range(len(id)):
        for j in range(len(id)):
            if i==j : 
                res=res+matrice[i,j]
    print(res)
    
def produit_diago(matrice:object)->int:
    
    """
    Calcule le produit des éléments diagonaux d'une matrice.
    
    :param matrice: Matrice pour laquelle calculer le produit des éléments diagonaux.
    :return: Produit des éléments diagonaux de la matrice.
    """
    
    res=1
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if i==j : 
                res=res*matrice[i,j]
    print(res)
    
def est_sym(matrice:object)->bool:
    
    """
    Vérifie si une matrice est symétrique.
    
    :param matrice: Matrice à vérifier.
    :return: True si la matrice est symétrique, sinon False.
    """
    
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i,j] != matrice[j,i]: 
                return (False)
    return(True)


def appli_fonctions(A:object)->bool : 
    
    """
    Vérifie si la matrice est symétrique après avoir ajouté sa transposée et divisé par 2.
    
    :param A: Matrice à vérifier.
    :return: True si la matrice est symétrique après transformation, sinon False.
    """
    
    return(est_sym((A+(A.T))/2))


def appli_fonctions_2(I:object)->int:
    
    """
    Calcule le produit des éléments diagonaux de la matrice.
    
    :param I: Matrice pour laquelle calculer le produit des éléments diagonaux.
    :return: Produit des éléments diagonaux de la matrice.
    """
    
    return(produit_diago(I))

def inverse(A:object)->object:
    
    """
   Calcule l'inverse d'une matrice et le multiplie par la matrice originale.
   
   :param A: Matrice à inverser.
   :return: Produit de la matrice inverse et de la matrice originale.
   """
   
    A_inv=np.linalg.inv(A)
    return(np.dot(A_inv,A))
                
    