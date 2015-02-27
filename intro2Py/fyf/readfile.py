# -*- coding: utf-8 -*-
#voici un exemple de fichier simple qui utilise deux modules os et os.path
#pour s'assurer qu'un fichier n'existe pas
#le créer, accéder à sa taille et à sa date de modification, puis le supprimer

import os
import os.path


nom_fichier = 'fichier-temoin'

#au depart, le fchier n'existe pas. On teste son existence
print("Debut: teste existence de", nom_fichier, os.path.exists(nom_fichier))

#on crée le fichier
with open(nom_fichier, 'w') as output:
    output.write("0664915552\n")

#maintenant, le fichier doit exister. On teste son existence
print ("Milieu: teste exitence de", nom_fichier, os.path.exists(nom_fichier))

#regardons la taille du fichier
print ("taille", os.path.getsize(nom_fichier))

#afficher la date de modification du fichier
mtime_timestamp = os.path.getmtime(nom_fichier)
print ("derniere date de modification (1)", mtime_timestamp)

#afficher la date d'une manière plus lisible
from datetime import datetime
mtime_datetime = datetime.fromtimestamp(mtime_timestamp)
print ("date de derniere modification (2)", mtime_datetime)

#détruire le fichier
os.remove(nom_fichier)

#vérifier que le fichier n'exite plus
#print ("fin: existence de ", nom_fichier, os.path.exists(nom_fichier))
