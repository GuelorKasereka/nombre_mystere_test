######################################################################################################
##     Est un MINI PROGRAMME DE LA RÉCHERCHE DE NOMBRE MYSTERE entre le NOMBRE_MIN & NOMBRE_MAX     ##
##                                                                                                  ##    
##  Grace à l'Algorithme de la Récherche dichotomique,j'ai fais en sorte que l'ordinateur elle meme ##  
##  puisse chercher et trouver le nombre mystère exacte sans l'intervention de l'homme au clavier   ##  
##                                                                                                  ##  
##     _______________Cet Algorithme est beaucoup plus précis qu'un humain_________________         ##
##                                                                                                  ##  
##                        *** ON PEUT TOUJOURS SE FIER AUX ALGORITHMES ***                          ## 
######################################################################################################

import random

# Les Constantes
NOMBRE_MIN = 1
NOMBRE_MAX = 985633444555543568955545386342349595959595757998346528572904556766767433226778932567563

# Le nombres aléatoire entre MIN & MAX
nb_mystere = random.randint(NOMBRE_MIN, NOMBRE_MAX)

# Cette fonction va traiter le processus de la manière dont l'ordinateur va déviner le nombre mystère 
def devinerNombre(n):
    if n > nb_mystere:
        print("Le nombre mystère est plus pétit")
        return -1
    elif n < nb_mystere:
        print("Le nombre mystère est plus grand")
        return 1
    else:
        print("Bravo, Vous avez trouvé le nombre mystère")
        return 0
    
# je stoke mes constantes dans ces variables
min = NOMBRE_MIN
max = NOMBRE_MAX

# Cette fonction va démander à l'ordinateur de répondre aux questions et aussi
# C'est sont ces processus qui permettra à l'ordinateur d'aboutir à la réponse 
def demanderNombre_IA(r, last_n):
    global min, max
    
    if r == 0:
        return last_n
    
    if r == 1:
        min = last_n +1
        
    if r == -1:
        max = last_n -1
        
    if min == max:
        return min
    
    if max - min == 1:
        if min == last_n:
            return max
        else:
            return min      
    return (min+max)//2

# Nous affichons le nombre mystère à l'avance pour voir si l'ordinateur ne s'est pas trompée!
print("Le nombre mystère est : ", nb_mystere)
print()

# je propose à l'ordinateur de commencer par 2
n = 2
print("Je teste avec :", n)

r = devinerNombre(n)
print()
    
# Nous allons boucler tant que l'ordinateur n'a pas encore trouver la bonne réponse et   
# C'est le processus qui va permettre à l'ordinateur de trouver le nombre mystère exacte :
while(r != 0):
    n = demanderNombre_IA(r, n)
    print("Je teste avec :", n)
    r =  devinerNombre(n)
    print()
    if r == 0:
        break
    
