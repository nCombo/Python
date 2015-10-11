#!/usr/bin/env python
# coding=UTF-8

# Dictionnaire de conversion de devises
DEVISES = {
	u'€':{ u'€':1.00, u'$':1.25, u'£':0.80 },
	u'$':{ u'€':0.80, u'$':1.00, u'£':0.64 },
	u'£':{ u'€':1.25, u'$':1.56, u'£':1.00 }
}

#TODO: fonction conversionDeDevise
	#"""Convertit la "valeur" exprimée en "deviseValeur" vers la devise "deviseRetour", arrondi a deux chiffres après la virgule.
	
	#Args :
		#valeur(float)     -- la valeur à convertir ;
		#deviseValeur(str) -- la devise de la valeur à convertir ;
		#deviseRetour(str) -- la devise attendue par l'appeleur de cette fonction.
    #Returns :
		#float : la "valeur" exprimée en "deviseRetour"
	#"""

#TODO: fonction lectureLigne
	#"""Lit une ligne du fichier csv sous forme d'un tuple (Libellé,Auteur,Prix,Devise)
	
	#Args :
		#ligne(str) -- une ligne du fichier csv
    #Returns :
		#tuple : un tuple (Libellé:str,Auteur:str,Prix:float,Devise:str)
	#"""
	## indices:
	##	- dans ipython taper help(str) et regarder la documentation de la méthode "split" ;
	##	- dans ipython taper help(str) et regarder la documentation de la méthode "strip".

#TODO: fonction lectureCSV
#indications: codecs.open(chemin, encoding='utf-8', mode='r') ouvre le fichier chemin en
#lecture seule et converti les lignes en UTF-8 vers l'encodage unicode de Python
	#"""Lit le fichier csv qui se trouve dans "chemin" et le convertit en une liste de tuples (Libellé,Auteur,Prix,Devise).
	
	#Args:
		#chemin(str) -- le chemin vers le fichier csv.
    #Returns:
		#list: une liste des tuples (Libellé,Auteur,Prix,Devise) contenus dans le fichier csv, cette liste n'inclut pas l'entête.
	#"""

#TODO: fonction conversionDonnees
	#"""Convertit une liste de tuples (Libellé,Auteur,Prix,Devise) en liste de tuples (Libellé,Auteur,Prix,deviseRetour).
	
	#Args :
		#donnees(list)     -- une liste des tuples (Libellé,Auteur,Prix,Devise) ;
		#deviseRetour(str) -- la devise attendue pour toutes les cases de la liste de retour.
    #Returns :
		#list : une liste des tuples (Libelléls ,Auteur,Prix,deviseRetour).
	#"""

#TODO: fonction ecritureCSV
#indications: codecs.open(chemin, encoding='utf-8', mode='w+') ouvre le fichier chemin en
#lecture écrasement et converti les chaine unicode de Python vers l'UTF-8
	#"""Crée un fichier csv dans "chemin" (et l'écrase s'il existe déjà) et écrit les "donnees" au format csv.
	
	#Args :
		#chemin(str)   -- le chemin vers le nouveau fichier csv ;
		#donnees(list) -- une liste des tuples (Libellé,Auteur,Prix,Devise).
	#"""






#*****************************************************************************#
#*****************************************************************************#
#***                             Vérifications                             ***#
#*****************************************************************************#
#*****************************************************************************#

# Exercice 4.1: Conversion de devises
#	- Compléter la fonction conversionDeDevise grâce au dictionnaire "DEVISES".
# Vérification (non exhaustive) des spécifications de la fonction conversionDeDevise.
print "\nVérifications exercice 4.1"
try:
	erreurDetecte = False
	if conversionDeDevise(1., u"€", u"€") != 1.:
		print " - Erreur de conversion € => €"
		erreurDetecte = True
	if conversionDeDevise(1., u"€", u"$") != 1.25:
		print " - Erreur de conversion € => $"
		erreurDetecte = True
	if conversionDeDevise(1., u"£", u"$") != 1.56:
		print " - Erreur de conversion £ => $"
		erreurDetecte = True
	if conversionDeDevise(1., u"$", u"€") != .8:
		print " - Erreur de conversion $ => €"
		erreurDetecte = True

	if erreurDetecte:
		print "Vous devez corriger vos erreurs."
	else:
		print "Bravo, la conversion semble fonctionner correctement."
except NameError:
	print "Vous devez implémenter la fonction conversionDeDevise"



# Exercice 4.2: Transformation d'un texte vers une structure de données.
#	- Compléter la fonction lectureLigne.
# Vérification (non exhaustive) des spécifications de la fonction lectureLigne.
print "\nVérifications exercice 4.2"
try:
	erreurDetecte = False
	attendu = u'abcd', u'efg h', 42.0, u'$'
	obtenu  = lectureLigne(u"abcd,efg h,42.0,$")
	if obtenu != attendu or not isinstance(obtenu[2], float):
		print "erreur, obtenu:", obtenu, ", attendu:", attendu
		erreurDetecte = True
	attendu = u'abcd', u'efg h', 4.2, u'€'
	obtenu  = lectureLigne(u"abcd  ,efg h, 4.2, €")
	if obtenu != attendu or not isinstance(obtenu[2], float):
		print "erreur, obtenu:", obtenu, ", attendu:", attendu
		erreurDetecte = True

	if erreurDetecte:
		print "Vous devez corriger vos erreurs."
	else:
		print "Bravo, la conversion d'une ligne semble fonctionner correctement."
except NameError:
	print "Vous devez implémenter la fonction lectureLigne"


# Exercice 4.3: Lecture d'un fichier.
#	- Compléter la fonction lectureCSV
# Vérification (non exhaustive) des spécifications de la fonction lectureCSV.
print "\nVérifications exercice 4.3"
try:
	donnees = lectureCSV('data_3_v0.csv')
	attendu = u'Python Pocket Reference 5ed', u'Mark Lutz', 12.62, u'€'
	if donnees[1] == attendu:
		print "Bravo, la lecture de fichier semble fonctionner correctement."
	else:
		print "Vous devez corriger vos erreurs."
except NameError:
	print "Vous devez implémenter la fonction lectureCSV"

# Exercice 4.4: Gestion de l'entête.
#	- Modifier la fonction lectureCSV de telle façon qu'elle ignore la ligne 
#   d'entête lorsque la variable avecEntete est True.
# Vérification (non exhaustive) des spécifications de la fonction lectureCSV.
print "\nVérifications exercice 4.4"
try:
	erreurDetecte = True
	attendu = u'Python Pocket Reference 5ed', u'Mark Lutz', 12.62, u'€'
	try:
		donnees = lectureCSV('data_3_v1.csv', True)
		if donnees[1] == attendu:
			erreurDetecte = False
	except ValueError:
		pass
	if erreurDetecte:
		print "Vous devez corriger vos erreurs."
	else:
		print "Bravo, la lecture de fichier avec entête semble fonctionner correctement."
except NameError:
	print "Vous devez implémenter la fonction lectureCSV"


# Exercice 4.5: Conversion en €
#	- Compléter la fonction conversionDonnees en modifiant les données pour que toutes les lignes soient en €.
print "\nVérifications exercice 4.5"
try:
	erreurDetecte = True
	donnees2 = conversionDonnees(donnees, u'€')
	attendu = u'Python 3', u'Sébastien CHAZALLET', 38.89, u'€'
	if donnees2[2] == attendu:
		print "Bravo, la conversion des données semble fonctionner correctement."
		if donnees2 is donnees:
			erreurDetecte = False
		else:
			print " ! Cependant la modification doit être faite en place."
	if erreurDetecte:
		print "Vous devez corriger vos erreurs."
except NameError:
	print "Vous devez implémenter la fonction conversionDonnees"


# Exercie 4.6: Écriture d'un fichier
#	- Compléter la fonction ecritureCSV
print "\nVérifications exercice 4.6"
try:
	ecritureCSV('data_out.csv', donnees)
	donneesTest = lectureCSV('data_out.csv')
	if donnees == donneesTest:
		print "Bravo, l'écriture de fichier semble fonctionner correctement."
	else:
		print "Vous devez corriger vos erreurs."
except NameError:
	print "Vous devez implémenter la fonction ecritureCSV et la fonction lectureCSV"

