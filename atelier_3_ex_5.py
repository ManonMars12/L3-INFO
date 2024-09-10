#Mars Manon L3 ST 
#Atelier de programmation 3 
#Exercice 5 

def ouvrante(car:chr)->bool:
    
    """
   Vérifie si le caractère fourni est un parenthèse ouvrante.

   Args:
       car (chr): Le caractère à vérifier.

   Returns:
       bool: True si le caractère est '(', '[' ou '{', sinon False.
   """
   
    return (car=="(" or car=="[" or car=="{")

def fermante(car:chr)->bool:
    
    """
    Vérifie si le caractère fourni est une parenthèse fermante.

    Args:
        car (chr): Le caractère à vérifier.

    Returns:
        bool: True si le caractère est ')', ']' ou '}', sinon False.
    """
    
    return (car==")" or car=="]" or car=="}")

def operateur(car:chr)->bool:
    
    """
    Vérifie si le caractère fourni est un opérateur arithmétique.

    Args:
        car (chr): Le caractère à vérifier.

    Returns:
        bool: True si le caractère est '+', '-' ou '*', sinon False.
    """
    
    ope=["+","-","*"]
    return(car in ope)

def nombre(car:str)->bool:
    
    """
    Vérifie si le caractère fourni est un chiffre.

    Args:
        car (str): Le caractère à vérifier.

    Returns:
        bool: True si le caractère est un chiffre (0-9), sinon False.
    """
    
    return(car.isdigit())


def reverse(car:chr)->chr: #ou car:str si nombre et return :str si pas valide 

     """
    Renvoie le caractère opposé pour les parenthèses fermantes.
    Les autres caractères sont retournés inchangés.

    Args:
        car (chr): Le caractère à inverser.

    Returns:
        chr: La parenthèse ouvrante correspondante si 'car' est une parenthèse fermante.
             Sinon, retourne le caractère inchangé s'il est un chiffre, un opérateur ou une parenthèse ouvrante.
             Retourne "Ce n'est pas valide" si le caractère n'est ni une parenthèse ni un opérateur ni un chiffre.
    """
     if car==")" : 
        return("(")
     elif car=="]" :
        return("[")
     elif car=="}" : 
        return("{")
     elif nombre(car) or operateur(car) or ouvrante(car) : 
        return(car)
  
     else : 
        return("Ce n'est pas valide") 

def caractere_valide(car:chr)->bool: #car peut etre str car nombre 

    """
    Vérifie si le caractère fourni est valide dans le contexte des parenthèses, des opérateurs ou des chiffres.

    Args:
        car (chr): Le caractère à vérifier.

    Returns:
        bool: True si le caractère est une parenthèse ouvrante ou fermante, un opérateur, un chiffre ou un espace, sinon False.
    """
    
    return(ouvrante(car) or fermante(car) or operateur(car) or nombre(car) or car==" ")


def verif_parenthese(expression:str)->bool:
    """
    Vérifie si une expression contient une séquence valide de parenthèses ouvrantes 
    et fermantes.

    Cette fonction utilise une pile pour vérifier que chaque parenthèse fermante 
    correspond bien à une parenthèse ouvrante correspondante. Si toutes les 
    parenthèses sont bien appariées et dans le bon ordre, la fonction retourne `True`, 
    sinon elle retourne `False`.

    Args:
        expression (str): L'expression contenant des parenthèses à vérifier.

    Returns:
        bool: `True` si les parenthèses sont bien équilibrées et correctement fermées, 
              `False` sinon.
    """
    p=[]
    res=True
    for i in range(len(expression)):
        if ouvrante(expression[i]):
            p.append(expression[i])
        elif fermante(expression[i]):
            if p[0]==reverse(expression[i]):
                p.pop(0)
            else :
                res=False
    return(res)
            
   # Je ne peux pas tester verif_parenthese("((3+2)*6-1") car la parenthèse n'est pas considerée dans la str 
            
    
    