#Mars Manon L3 ST 
#Atelier de programmation 4 
#Partie 3 

import numpy as np 

def matrice_adjacence(A:list, S:list)->object:
    
    """
    Crée une matrice d'adjacence à partir d'une liste d'arêtes.

    Paramètres:
    A (list): Liste d'arêtes où chaque arête est représentée comme un tuple (i, j).
    S (list): Liste des sommets.

    Retourne:
    object: Matrice d'adjacence sous forme de tableau numpy 2D où mat[i, j] est 1 s'il existe une arête entre i et j, sinon 0.
    """
    
    mat=np.zeros((len(S),len(S)), dtype=int)
    for i in range(len(mat)):
        for j in range(len(mat)):
            if (i,j) in A : 
                mat[i,j]=1
    return(mat)
    
    
def matriceAdjacencePond(S:list,A:list)->object:
    
    """
    Crée une matrice d'adjacence pondérée à partir d'une liste d'arêtes pondérées.

    Paramètres:
    S (list): Liste des sommets.
    A (list): Liste des arêtes pondérées où chaque arête est représentée comme un tuple (i, j, poids).

    Retourne:
    object: Matrice d'adjacence pondérée sous forme de tableau numpy 2D où mat[i, j] est le poids de l'arête entre i et j, ou 0 s'il n'y a pas d'arête.
    """
    
    mat=np.zeros((len(S),len(S)), dtype=int)
    for e in A : 
        mat[e[0], e[1]]=e[2]
    return(mat)
    


def lire_matrice(fichier:str)->str:
    
    """
    Lit une matrice depuis un fichier.

    Paramètres:
    fichier (str): Chemin du fichier contenant la matrice.

    Retourne:
    str: Matrice lue depuis le fichier sous forme de tableau numpy.
    """
    
    mat=np.loadtxt(fichier)
    return(mat)    

def tout_les_sommets(mat:object)->list:
    
    """
    Retourne une liste de tous les indices de sommets dans la matrice.

    Paramètres:
    mat (object): Matrice d'adjacence ou toute autre matrice carrée.

    Retourne:
    list: Liste des indices des sommets.
    """


    lst=[]
    for i in range(len(mat)):
        lst.append(i)
        
    return(lst)

def list_arc_mat(mat:object)->list:
    
    """
    Retourne une liste des arêtes à partir de la matrice d'adjacence.

    Paramètres:
    mat (object): Matrice d'adjacence où mat[i, j] est non nul s'il y a une arête entre i et j.

    Retourne:
    list: Liste des arêtes représentées comme des tuples (i, j) où mat[i, j] est non nul.
    """
    
    liste=[]
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i,j] != 0 : 
                liste.append((i,j))
    return(liste)

def matriceIncidence(mat:object)->object:
    
    """
    Crée une matrice d'incidence à partir de la matrice d'adjacence.

    Paramètres:
    mat (object): Matrice d'adjacence où mat[i, j] est non nul s'il y a une arête entre i et j.

    Retourne:
    object: Matrice d'incidence sous forme de tableau numpy 2D où chaque colonne représente une arête et les lignes indiquent l'incidence des sommets avec -1, 1, ou 0.
    """

    arcs=[]
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i,j] != 0 : 
                arcs.append((i,j))
    mat_inci=np.zeros((len(mat),len(arcs)), dtype=int)
    for i in range(len(arcs)):
        e = arcs[i]
        mat_inci[e[0], i] = 1
        mat_inci[e[1], i] = -1
    
    return (mat_inci)


def est_voisin(mat:object, s:int, v:int)->bool:
    
    """
    Vérifie si deux sommets sont voisins dans la matrice d'adjacence.

    Paramètres:
    mat (object): Matrice d'adjacence où mat[i, j] est non nul s'il y a une arête entre les sommets i et j.
    s (int): Index du premier sommet.
    v (int): Index du deuxième sommet.

    Retourne:
    bool: Vrai si les sommets s et v sont voisins (c'est-à-dire qu'il existe une arête entre eux), sinon Faux.
    """
    
    return(mat[s,v] != 0 or mat[v, s] != 0)
       
   
