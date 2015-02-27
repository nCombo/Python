# -*- coding: utf-8 -*-
#TP créer un jeu de casino: jeu de roulettte


from random import randrange
from math import ceil

argent = 1000 # on a 1000 $ au debut du jeu
continuer_partie = True # bolléen qui est vraie tant qu'on doit continuer la partie

print("Vous vous installez à la table de roulette avec", argent, "$")

while continuer_partie: # tant qu'on doit continuer la partie
    # on demande à l'utilisateur de saisir le nombre sur lequel il va miser
    nombre_mise = -1
    while nombre_mise < 0 or nombre_mise > 49:
        nombre_mise = input("Tapez le nombre sur lequel vous voulez miser (entre 0 et 49) : ")
        # on convertit le nombre misé en Entier
        try :
            nombre_mise = int(nombre_mise)
        except ValueError:
            print("Vous n'avez pas de nombre")
            nombre_mise = -1
            continue
        if nombre_mise < 0 :
            print("Ce nombre est négatif")
        if nombre_mise > 49 :
            print("Ce nombre est supérieur à 49")    
    
    #à présent,on sélectionne la somme à miser sur le nombre
    mise = 0
    while mise <= 0 or mise > argent:
        mise = input("Tapez le montant de votre mise : ")
        #on convertit la mise
        try :
            mise = int(mise)
        except ValueError:
            print("Vous n'avez pas saisi de nombe")
            mise = -1
            continue
        if mise <= 0:
            print("La somme saisie est négative ou nulle.")
        if mise > argent:
            print("Vous ne pouvez pas miser autant, vous n'avez pas que ", argent, "$")
    
    #le nombre misé et la mise ont été sélectionnés par l'utilisateur
    # on fait tourner la roulette
    numero_gagnant = randrange(50)
    print("La roulette tourne... et s'arrête sur le numéro", numero_gagnant)
    
    #on établit le gain du joueur
    if numero_gagnant == nombre_mise:
        print("félicitation! Vous obtenez", mise * 3, "$ !")
        argent += mise * 3
    elif numero_gagnant % 2 == nombre_mise % 2: # ils sont de la même couleur
        mise = ceil(mise * 0.5)
        print("Vous avez misé sur la bonne couleur. Vous obtenez", mise, "$")
        argent += mise
    else:
        print("Désolé l'ami, c'est pas pour cette fois. Vous perdez votre mise.")
        argent -= mise    
    
    #on interrompt la partie si le joueur est ruiné
    if argent <= 0:
        print("Vous vous êtes ruiné! C'est la fin de la partie.")
        continuer_partie = False
    else:
        #on affiche l'argent du joueur
        print("Vous avez à présent", argent, "$")
        quitter = input("Tapez 'o'pour quitter ou 'n' pour continuer : ")
        if quitter == "o" or quitter == "O":
            print("Vous quittez le casino avec vos gains.")  
            continuer_partie = False
    
