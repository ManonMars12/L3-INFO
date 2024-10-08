#Mars Manon L3 ST 
#Atelier de programmation 5 
#Partie 1 

#Exercice 1 

import random as rd 
import time 
import matplotlib.pyplot as plt
import numpy as np


def gen_list_random_int(int_nb=10, int_binf=0, int_bsup=10):
    
    """
  Génère une liste de nombres entiers aléatoires.

  Args:
      int_nb (int): Nombre d'éléments dans la liste. Par défaut 10.
      int_binf (int): Borne inférieure des entiers générés. Par défaut 0.
      int_bsup (int): Borne supérieure des entiers générés. Par défaut 10.

  Returns:
      list: Liste d'entiers aléatoires.
  """
  
    liste=[]
    for i in range(int_nb):
        liste.append(rd.randint(int_binf,int_bsup))
    return(liste)



#Exercice 2 

def mix_list(list_to_mix:list)->list:
    
    """
    Mélange une liste en permutant des éléments de manière aléatoire.

    Args:
        list_to_mix (list): Liste à mélanger.

    Returns:
        list: Une copie de la liste mélangée.
    """

    res=list_to_mix.copy()
    for i in range(rd.randint(1, len(list_to_mix))):
        pos_1=rd.randint(0,len(list_to_mix)-1)
        pos_2=rd.randint(0,len(list_to_mix)-1)
        while pos_1==pos_2:
            pos_2=rd.randint(0,len(list_to_mix)-1)
        element_1=list_to_mix[pos_1]
        element_2=list_to_mix[pos_2]
        res[pos_1]=element_2
        res[pos_2]=element_1
    return(list_to_mix, res)
    
        


#Exercice 3 

def choose_element_list(list_in_which_to_choose:list): 
    
    """
    Sélectionne aléatoirement un élément d'une liste.

    Args:
        list_in_which_to_choose (list): Liste dans laquelle choisir l'élément.

    Returns:
        any: L'élément sélectionné aléatoirement.
    """
    
    pos=rd.randint(0, len(list_in_which_to_choose)-1)
    return(list_in_which_to_choose[pos])


#Exercice 4 


def extract_elements_list(list_in_which_to_choose:list, int_nbr_of_element_to_extract:int)->list:
    
    """
   Extrait un nombre donné d'éléments d'une liste de façon aléatoire.

   Args:
       list_in_which_to_choose (list): Liste dans laquelle extraire les éléments.
       int_nbr_of_element_to_extract (int): Nombre d'éléments à extraire.

   Returns:
       list: Liste contenant les éléments extraits.
   """
   
    res=[]
    liste=list_in_which_to_choose.copy()
    for i in range(int_nbr_of_element_to_extract):
        element=choose_element_list(liste)
        res.append(element)
        liste.remove(element)
    return(res)



#Exercice 5 

    

def perf_mix(fonction1:callable, fonction2:callable, lst_taille:list,nb_exec:int)->tuple: 
    
    
    """
   Compare les performances de deux fonctions en mesurant le temps d'exécution moyen pour des tailles de listes variées.

   Args:
       fonction1 (callable): Première fonction à évaluer.
       fonction2 (callable): Deuxième fonction à évaluer.
       lst_taille (list): Liste des tailles des listes à tester.
       nb_exec (int): Nombre d'exécutions pour chaque test.

   Returns:
       tuple: Deux listes contenant les temps d'exécution moyens pour chaque fonction.
   """
   
    perf_f1=[]
    perf_f2=[]
    moy=0
    for i in range(len(lst_taille)):
        lst_hasard=gen_list_random_int(lst_taille[i], int_binf=0, int_bsup=10) #Juste à changer selon configuration 
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

def plot_q1()->None:
    
    """
    Trace un graphique comparant les performances entre `rd.shuffle` et `mix_list` pour des tailles de listes variées.
    """
    
    # Les tailles de listes à utiliser pour les tests
    lst_taille = [10, 500, 5000, 50000, 100000]
    x_axis_list = np.array(lst_taille)

    perf_shuffle, perf_mixlist = perf_mix(rd.shuffle, mix_list, lst_taille, 100)

    # Création de la figure et des axes
    fig, ax = plt.subplots()

    # Tracé de la courbe pour rd.shuffle
    ax.plot(x_axis_list, perf_shuffle, 'bo-', label='rd.sample')

    # Tracé de la courbe pour mix_list
    ax.plot(x_axis_list, perf_mixlist, 'r*-', label='')

    # Ajout des légendes et des labels
    ax.set(xlabel='Taille de la liste', ylabel='Temps (secondes)', title='Comparaison des performances entre rd.shuffle et mix_list')



    plt.show()
    
    
def perf_mix2(fonction1:callable, fonction2:callable, lst_taille:list,nb_exec:int)->tuple: 
    
    """
    Compare les performances de deux fonctions (qui acceptent un élément en plus d'une liste) en mesurant le temps d'exécution moyen pour des tailles de listes variées.

    Args:
        fonction1 (callable): Première fonction à évaluer.
        fonction2 (callable): Deuxième fonction à évaluer.
        lst_taille (list): Liste des tailles des listes à tester.
        nb_exec (int): Nombre d'exécutions pour chaque test.

    Returns:
        tuple: Deux listes contenant les temps d'exécution moyens pour chaque fonction.
    """
    
    perf_f1=[]
    perf_f2=[]
    moy=0
    nb_hasard=rd.randint(0, 9)
    for i in range(len(lst_taille)):
        lst_hasard=gen_list_random_int(lst_taille[i], int_binf=0, int_bsup=10)
        for i in range(nb_exec):
            start_pc = time.perf_counter()
            fonction1(lst_hasard, lst_hasard[nb_hasard])
            end_pc = time.perf_counter()
            elapsed_time_pc = end_pc-start_pc
            moy=moy+elapsed_time_pc
        moy=moy/nb_exec
        perf_f1.append(moy)
            
        for i in range(nb_exec):
            start_pc = time.perf_counter()
            fonction2(lst_hasard,lst_hasard[nb_hasard])
            end_pc = time.perf_counter()
            elapsed_time_pc = end_pc-start_pc
            moy=moy+elapsed_time_pc
        moy=moy/nb_exec
        perf_f2.append(moy)

    return(perf_f1, perf_f2)
    
def plot_q2()->None:
    
    """
    Trace un graphique comparant les performances entre `rd.sample` et `extract_elements_list` pour des tailles de listes variées.
    """
    
    lst_taille = [10, 500, 5000, 50000, 100000]
    x_axis_list = np.array(lst_taille)

    perf_sample, perf_extract = perf_mix2(rd.sample, extract_elements_list, lst_taille, 100)

    # Création de la figure et des axes
    fig, ax = plt.subplots()

    # Tracé de la courbe pour rd.shuffle
    ax.plot(x_axis_list, perf_sample, 'bo-', label='rd.shuffle')

    # Tracé de la courbe pour mix_list
    ax.plot(x_axis_list, perf_extract, 'r*-', label='extract_elements_list')

    # Ajout des légendes et des labels
    ax.set(xlabel='Taille de la liste', ylabel='Temps (secondes)', title='Comparaison des performances entre rd.sample et extract_elements_list')


    # Affichage de la légende
    ax.legend(loc='upper left', shadow=True, fontsize='x-large')

    # Affichage du graphique
    plt.show()
    

    
