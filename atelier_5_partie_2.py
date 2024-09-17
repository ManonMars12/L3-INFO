#Mars Manon L3 ST 
#Atelier de programmation 5 
#Partie 2 

import random as rd 
import time 
import matplotlib.pyplot as plt
import numpy as np


def tri(lst:list)->list:
    
    """
    Trie une liste en utilisant l'algorithme de tri par sélection qui sélectionne le plus petit élément de la liste
    à chaque itération et le place dans une nouvelle liste.

    Args:
        lst (list): Liste d'éléments à trier.

    Returns:
        list: Nouvelle liste contenant les éléments triés.
    """
    
    res=[]
    for i in range(len(lst)):
        res.append(min(lst))
        lst.remove(min(lst))
    return(res)





def gen_list_random_int(int_nb=10, int_binf=0, int_bsup=10):
    
    """
   Génère une liste de nombres entiers aléatoires dans une plage donnée.

   Args:
       int_nb (int): Nombre d'entiers dans la liste. Par défaut 10.
       int_binf (int): Borne inférieure des entiers générés. Par défaut 0.
       int_bsup (int): Borne supérieure des entiers générés. Par défaut 10.

   Returns:
       list: Liste d'entiers aléatoires générés.
   """
   
    liste=[]
    for i in range(int_nb):
        liste.append(rd.randint(int_binf,int_bsup))
    return(liste)



def perf_mix2(fonction1:callable, fonction2:callable, lst_taille:list,nb_exec:int)->tuple: 
    
    """
    Compare les performances de deux fonctions sur des listes de différentes tailles, en mesurant le temps d'exécution moyen.

    Args:
        fonction1 (callable): Première fonction à tester (par exemple `sorted`).
        fonction2 (callable): Deuxième fonction à tester (par exemple `tri`).
        lst_taille (list): Liste des tailles des listes sur lesquelles tester les fonctions.
        nb_exec (int): Nombre d'exécutions pour chaque taille de liste afin d'obtenir une moyenne.

    Returns:
        tuple: Deux listes contenant les temps d'exécution moyens pour `fonction1` et `fonction2` pour chaque taille de liste.
    """
    
    perf_f1=[]
    perf_f2=[]
    moy=0
    nb_hasard=rd.randint(0, 9)
    for i in range(len(lst_taille)):
        # Configuration 1 lst_hasard=gen_list_random_int(lst_taille[i], int_binf=0, int_bsup=10)
        #Configuration 2 lst_hasard=sorted(gen_list_random_int(lst_taille[i], int_binf=0, int_bsup=10))
        #configuration 3 lst_hasard=gen_list_random_int(lst_taille[i], int_binf=0, int_bsup=10)
        #res=[]
        #for i in range(len(lst)):
            #res.append(max(lst))
            #lst.remove(max(lst))
                            
        for i in range(nb_exec):
            start_pc = time.perf_counter()
            fonction1(lst_hasard)
            end_pc = time.perf_counter()
            elapsed_time_pc = end_pc-start_pc
            moy=moy+elapsed_time_pc
        moy=moy/nb_exec
        perf_f1.append(moy)
            
        for i in range(nb_exec):
            start_pc = time.perf_counter()
            fonction2(lst_hasard)
            end_pc = time.perf_counter()
            elapsed_time_pc = end_pc-start_pc
            moy=moy+elapsed_time_pc
        moy=moy/nb_exec
        perf_f2.append(moy)
            
    return(perf_f1, perf_f2)
    
def plot_q3()->None:
    
    """
    Trace un graphique comparant les performances entre les fonctions `sorted` et `tri` pour des tailles de listes variées.

    Le graphique montre le temps d'exécution en fonction de la taille de la liste pour chaque fonction testée.

    Returns:
        None: Cette fonction n'a pas de valeur de retour.
    """
    
    lst_taille = [10, 500, 5000, 50000, 100000]
    x_axis_list = np.array(lst_taille)

    perf_sorted, perf_tri = perf_mix2(sorted, tri, lst_taille, 100)

    # Création de la figure et des axes
    fig, ax = plt.subplots()

    # Tracé de la courbe pour rd.shuffle
    ax.plot(x_axis_list, perf_sorted, 'bo-', label='sorted')

    # Tracé de la courbe pour mix_list
    ax.plot(x_axis_list, perf_tri, 'r*-', label='tri')

    # Ajout des légendes et des labels
    ax.set(xlabel='Taille de la liste', ylabel='Temps (secondes)', title='Comparaison des performances entre rd.sample et extract_elements_list')


    # Affichage de la légende
    ax.legend(loc='upper left', shadow=True, fontsize='x-large')

    # Affichage du graphique
    plt.show()

    

    
