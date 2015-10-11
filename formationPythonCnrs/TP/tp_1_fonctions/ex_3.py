#!/usr/bin/env python
# coding=UTF-8
import random, math

LIST_DATA = [ 4.1, 9, 0, "coucou", -1000, 1000, [ 0, 1], "42", -float("inf"), 18, -49, -4999.0, -455, float("inf"), -541, 9999.9, float("nan") ]
LIST_DATA.extend(4.2 * random.randint(-1000,1000) for r in xrange(20))
CHAINE = "abcd0ef9ghij8klmA5BCD7EFG6HIJK4LMNO3PQR2STU1VWXYZnopqrstuvwxyz"

# Exercie 3.1: Filtrage de données de type liste
# ecrire un filtre de type lamda qui selection les données de types entières et flotante
LIST_DATA1 = filter(lambda x: isinstance(x,float) or isinstance(x,int), LIST_DATA)


# Exercie 3.2: Filtrage de données de type liste
# ecrire un filtre de type lamda qui selection les données comprise entre [-1000 et 1000[
LIST_DATA2 = filter(lambda x: -1000 <= x < 1000, LIST_DATA1) # x est supérieur à -1000 et inférieur à 1000

# Exercie 3.3: "Mappage" de données de type liste
# ecrire un map de type lamda qui transforme données en valeur absolues
LIST_DATA3 = map(lambda x: abs(x), LIST_DATA2)
LIST_DATA3 = map(lambda x: -x if(x < 0.) else x, LIST_DATA2) # les 2 syntaxees donnent le même résultat
	
# Exercie 3.4: "Réduction" de données de type liste
# ecrire un reduce de type lamda qui calcule la multiplication des données tronquées en entier (0 doit être traité comme 1)
LIST_DATA4 = reduce(lambda x,y: (2) * (3), LIST_DATA3)
# Exercie 3.5: Filtrage de données de type chaine
# ecrire un filtre de type lamda qui selection les characters entre e et n et également entre E et N
CHAINE5 = CHAINE











#*****************************************************************************#
#*****************************************************************************#
#***                             Vérifications                             ***#
#*****************************************************************************#
#*****************************************************************************#


print "\nVérifications exercice 3.1"
erreurDetecte = False
for e in LIST_DATA1:
	if not (isinstance(e, int) or isinstance(e, float)):
		print "  - ", e, "n'est ni entier ni flotant"
		erreurDetecte = True
if erreurDetecte:
	print "Vous devez corriger vos erreurs."
else:
	print "Bravo, le filtre semble fonctionner correctement."

print "\nVérifications exercice 3.2"
erreurDetecte = False
for e in LIST_DATA2:
	if isinstance(e, int) or isinstance(e, float):
		if math.isnan(e) or e >= 1000 or e < -1000:
			print "  - ", e, "n'est pas dans l'interval [-1000..1000["
			erreurDetecte = True
if erreurDetecte:
	print "Vous devez corriger vos erreurs."
else:
	print "Bravo, le filtre semble fonctionner correctement."

print "\nVérifications exercice 3.3"
erreurDetecte = False
for e in LIST_DATA3:
	if isinstance(e, int) or isinstance(e, float):
		if (not math.isnan(e)) and (-1000<e<=1000):
			if e < 0:
				print "  - ", e, "n'est pas >= 0"
				erreurDetecte = True
if erreurDetecte:
	print "Vous devez corriger vos erreurs."
else:
	print "Bravo, le map semble fonctionner correctement."

print "\nVérifications exercice 3.4"
verif = 1.
for e in LIST_DATA3:
	if (isinstance(e, int) or isinstance(e, float)) and (not math.isnan(e)) and (0<=e<=1000):
		e = int(e)
		verif = verif * 1 if (e == 0) else e
if LIST_DATA4 != verif:
	print "Vous devez corriger vos erreurs."
else:
	print "Bravo, la réduction semble fonctionner correctement."

print "\nVérifications exercice 3.5"
if CHAINE5 == 'efghijklmEFGHIJKLMNn':
	print "Bravo, le filtre semble fonctionner correctement."
else:
	print "Vous devez corriger vos erreurs."

