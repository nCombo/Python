#!/usr/bin/env python
# coding=UTF-8

# Exercice 1.1 fonction afficheBonjour
def afficheBonjour():
    print('Bonjour')

# Exercice 1.2 fonction afficheBonjourA(nom, prenom)
nom ='Combo'
prenom = 'Nourdine'

def afficheBonjourA(a, b):
    print 'Bonjour', a, b
afficheBonjourA(nom, prenom)




#*****************************************************************************#
#*****************************************************************************#
#***                             Vérifications                             ***#
#*****************************************************************************#
#*****************************************************************************#

print "**Le résultat attendu est :\nBonjour"
print "->Votre résultat :"
try:
	afficheBonjour()
except NameError:
	print "La fonction afficheBonjour() n'est pas définie"

print "\n**Le résultat attendu est :\nBonjour tata TODO"
print "->Votre résultat :"
try:
	afficheBonjourA("TODO", "tata")
except NameError:
	print "La fonction afficheBonjourA() n'est pas définie"


