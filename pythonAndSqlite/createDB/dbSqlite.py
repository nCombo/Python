#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 5 nov. 2015

@author: combo
'''

import sqlite3

try:
    conn = sqlite3.connect('ma_base.db')
    
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT,
        age INTERGER
    )
    """)
    conn.commit()
    # inserer une ligne dans la table
    cursor.execute("""
    INSERT INTO users(name, age) VALUES(?, ?)""", ("Olivier", 30))
    
    id = cursor.lastrowid
    print("dernier id: %d" % id)
    
    users = []
    users.append(("Jean", 28))
    users.append(("Jean-Louis", 20))
    users.append(("Paul", 35))
    users.append(("Liza", 18))
    # inserer plusieurs listes à partir un tableau
    cursor.executemany("""
    INSERT INTO users (name, age) VALUES(?, ?)""", users)
    
    # recuperer les données de la première ligne
    # ensuite récupérer plusieurs donées de la même recherche
    cursor.execute("""SELECT id, name, age FROM users""")
    user1 = cursor.fetchone()
    print("utilisateur 1 est ", user1)
    
    #rows = cursor.fetchall()
    #for row in rows:
        #print('{0}: {1}, {2}'.format(row[0], row[1], row[2]))
    
    for row in cursor:
        print("======")
        print('{0}: {1}, {2}'.format(row[0], row[1], row[2]))
    
    #modifier des entrées
    cursor.execute("""UPDATE users SET age = ? WHERE id = 2""", (31,))
except sqlite3.OperationalError:
    print("Erreur la table déjà")
except Exception as e:
    print("Erreur")
    conn.rollback() # pour revenir au dernier commit de la base de données
finally:
    conn.close()

if __name__ == '__main__':
    pass