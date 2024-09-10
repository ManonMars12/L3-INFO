#Mars Manon L3 ST 
#Atelier de programmation 3 ``
#Exercice 3 

import random

def places_lettre(ch:str, mot:str)->list:
    """
    Donne la ou les place(s) d'une lettre donnée dans un mot donné
    Arg : mot->str
    ch:str
    Return places->list
    """
    liste_mot=list(mot)
    places=[]
    for i in range(0,len(liste_mot)):
        liste_mot[i]=str(liste_mot[i])
        if liste_mot[i]==ch:
            places.append(i)
    return(places)

def outputStr(mot:str, lpos:list)-> str : 
    """
    Affiche le mot avec les _ et les lettres aux positions souhaitées  
    Arg : mot->str
    lpos->list
    Return res->str
    """
    liste_mot=list(mot)
    res=[]
    for i in range(len(liste_mot)) :
        if i in lpos : 
            res.append(liste_mot[i])
        else : 
            res.append("_")
    res=" ".join(res)
    return(res)
    
def runGame():
    """
    Procédure qui permet de lancer une partie de jeu du pendu
    """
    liste_de_mots=["python", "arbre", "soleil", "ordinateur", "livre", "montagne", "musique", "fleur", "voiture", "plage",
        "etoile", "guitare", "chien", "chat", "foret", "bouteille", "paysage", "riviere", "ballon", "nuage"] #  Liste générée avec ChatGPT 
    mot_aleatoire = liste_de_mots[random.randint(1, len(liste_de_mots))]
    mot_trouve=False
    pendu_dessine=False
    sorties_pendu=["|______", "|/ \ ",  "| T ", "| O ", "|---] "]
    #print(mot_aleatoire)
    mot_a_trous=outputStr(mot_aleatoire, [])
    print(mot_a_trous)
    i=0
    nb_echecs=0
    nb_coups_restants=5
    pos_lettres_trouvees = []
    
    
    while ((not mot_trouve) and (not pendu_dessine)): 
        lettre = str(input("Veuillez entrer une lettre"))
        places_de_la_lettre=places_lettre(lettre, mot_aleatoire)
        if places_de_la_lettre != []:
            pos_lettres_trouvees.extend(places_de_la_lettre)
            mot_a_trous = outputStr(mot_aleatoire, pos_lettres_trouvees)
            print(mot_a_trous)
            if "_" not in mot_a_trous : 
                print("Bravo, vous avez gagné")
                mot_trouve=True
            
        else :
            nb_echecs=nb_echecs+1
            for i in range (1,nb_echecs):
                print(sorties_pendu[-i])#Pour un affichage à l'endroit 
            if nb_echecs==5:
                print(sorties_pendu[0])
                    
            nb_coups_restants=nb_coups_restants-1
            str_nb_coups_restants=str(nb_coups_restants)
            if nb_coups_restants != 0 :
                print("Il vous reste " + str_nb_coups_restants + " coups restants")
            else : 
                print("Vous avez perdu, le mot était " + mot_aleatoire )
                pendu_dessine=True
            
       
def build_list(fileName:str)->list:
    """
    Créer une liste avec les mots présents dans un fichier
    Arg : fileName->str
    Return liste_elements_sans_slash_n-> liste
    """
    # lire un fichier
    liste_elements_sans_slash_n=[]
    file = open(fileName, "r")
    content = file.readlines()
    file.close()
    
    for i in range(len(content)):
        
        liste_mot_element_sans_slash_n=str(content[i]).split("\n")
        liste_mot_element_sans_slash_n.pop(1)
        liste_mot_element_sans_slash_n[0]=liste_mot_element_sans_slash_n[0].lower()
        liste_mot_element_sans_slash_n="".join(liste_mot_element_sans_slash_n)
        liste_elements_sans_slash_n.append(liste_mot_element_sans_slash_n)
        
    return(liste_elements_sans_slash_n)


        
def runGame_2():
    """
    Procédure qui permet de lancer une partie de jeu du pendu (avec fichier)
    """
    fileName=str(input("Veuillez entrer le nom du fichier"))
    liste_de_mots=build_list(fileName)
    mot_aleatoire = liste_de_mots[random.randint(1, len(liste_de_mots))]
    mot_trouve=False
    pendu_dessine=False
    sorties_pendu=["|______", "|/ \ ",  "| T ", "| O ", "|---] "]
    #print(mot_aleatoire)
    mot_a_trous=outputStr(mot_aleatoire, [])
    print(mot_a_trous)
    i=0
    nb_echecs=0
    nb_coups_restants=5
    pos_lettres_trouvees = []
    
    
    while ((not mot_trouve) and (not pendu_dessine)): 
        lettre = str(input("Veuillez entrer une lettre"))
        places_de_la_lettre=places_lettre(lettre, mot_aleatoire)
        if places_de_la_lettre != []:
            pos_lettres_trouvees.extend(places_de_la_lettre)
            mot_a_trous = outputStr(mot_aleatoire, pos_lettres_trouvees)
            print(mot_a_trous)
            if "_" not in mot_a_trous : 
                print("Bravo, vous avez gagné")
                mot_trouve=True
            
        else :
            nb_echecs=nb_echecs+1
            for i in range (1,nb_echecs):
                print(sorties_pendu[-i])#Pour un affichage à l'endroit 
            if nb_echecs==5:
                print(sorties_pendu[0])
                    
            nb_coups_restants=nb_coups_restants-1
            str_nb_coups_restants=str(nb_coups_restants)
            if nb_coups_restants != 0 :
                print("Il vous reste " + str_nb_coups_restants + " coups restants")
            else : 
                print("Vous avez perdu, le mot était " + mot_aleatoire)
                pendu_dessine=True
   
def mots_Nlettres(lst_mots:list, n:int)->list: #Importée de l'atelier 3 ex 2
    """
    Créer une liste avec les mots de n lettres présents dans la liste placée en argument
    Arg : lst_mots->liste
    n:int
    Return res-> liste
    """
    res=[]
    for i in range(len(lst_mots)):
        liste_detail=list(lst_mots[i])
        if len(liste_detail)==n:
            res.append(lst_mots[i])
    return(res)

def build_dict(lst:list)->dict:
    """
    Créer un dictionnaire avec les mots présents dans une liste selon leur nombre de lettres 
    Arg : lst->list
    Return dico->dict
    """
    dico = {}
    len_max=0
    for i in range(len(lst)):
        if len(lst[i])>len_max:
            len_max=len(lst[i])
        
    for i in range (len_max):
        
        nouveaux_elements={i+1 : mots_Nlettres(lst, i+1)}
        dico.update(nouveaux_elements)
    return(dico)

def select_word(sorted_words:dict, word_len:int)->str: 
    """
    Sélectionne un mot selon sa longueur
    Arg : sorted_words->dict
    word_len->int
    Return mot_aleatoire->str
    """
    cle=word_len
    liste_mots_longueur_cle=sorted_words[cle]
    
    
    hasard=random.randint(0, len(liste_mots_longueur_cle) - 1)
    
    mot_aleatoire=liste_mots_longueur_cle[hasard]
    return(mot_aleatoire)

def runGame_3():
    """
    Procédure qui permet de lancer une partie de jeu du pendu (avec fichier et dictionnaire (mot aléatoire))
    """
    
    fileName=str(input("Veuillez entrer le nom du fichier"))
    difficulte=str(input("Veuillez choisir une difficulté : easy, normal, hard"))
    liste_de_mots=build_list(fileName)
    nb_lettres_max=0
    for i in range(len(liste_de_mots)):
        if len(list(liste_de_mots[i])) > nb_lettres_max:
            nb_lettres_max=len(liste_de_mots[i])
        
    dico=build_dict(liste_de_mots)
    if difficulte=="easy":
        nb_lettres=random.randint(1,6)
        mot_aleatoire=select_word(dico, nb_lettres)
    elif difficulte=="hard":
        nb_lettres=random.randint(9, nb_lettres_max)
        mot_aleatoire=select_word(dico, nb_lettres)
    else : 
        nb_lettres=random.randint(7, 8)
        mot_aleatoire=select_word(dico, nb_lettres)
        
    mot_trouve=False
    pendu_dessine=False
    sorties_pendu=["|______", "|/ \ ",  "| T ", "| O ", "|---] "]
    #print(mot_aleatoire)
    mot_a_trous=outputStr(mot_aleatoire, [])
    print(mot_a_trous)
    i=0
    nb_echecs=0
    nb_coups_restants=5
    pos_lettres_trouvees = []
    
    
    while ((not mot_trouve) and (not pendu_dessine)): 
        lettre = str(input("Veuillez entrer une lettre"))
        places_de_la_lettre=places_lettre(lettre, mot_aleatoire)
        if places_de_la_lettre != []:
            pos_lettres_trouvees.extend(places_de_la_lettre)
            mot_a_trous = outputStr(mot_aleatoire, pos_lettres_trouvees)
            print(mot_a_trous)
            if "_" not in mot_a_trous : 
                print("Bravo, vous avez gagné")
                mot_trouve=True
            
        else :
            nb_echecs=nb_echecs+1
            for i in range (1,nb_echecs):
                print(sorties_pendu[-i])#Pour un affichage à l'endroit 
            if nb_echecs==5:
                print(sorties_pendu[0])
                    
            nb_coups_restants=nb_coups_restants-1
            str_nb_coups_restants=str(nb_coups_restants)
            if nb_coups_restants != 0 :
                print("Il vous reste " + str_nb_coups_restants + " coups restants")
            else : 
                print("Vous avez perdu, le mot était " + mot_aleatoire)
                pendu_dessine=True



        
       
    