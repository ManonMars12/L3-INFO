#Mars Manon L3 ST 
#Atelier de programmation 5 
#Partie 2 

import random as rd 
import time 
import matplotlib.pyplot as plt
import numpy as np


def tri(lst:list)->list:
    res=[]
    for i in range(len(lst)):
        res.append(min(lst))
        lst.remove(min(lst))
    return(res)





def gen_list_random_int(int_nb=10, int_binf=0, int_bsup=10):
    liste=[]
    for i in range(int_nb):
        liste.append(rd.randint(int_binf,int_bsup))
    return(liste)



def perf_mix2(fonction1:callable, fonction2:callable, lst_taille:list,nb_exec:int)->tuple: 
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

    
