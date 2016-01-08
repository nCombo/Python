#!/usr/bin/env/python
#-*- coding: utf-8 -*-

'''
Created on 10 nov. 2015

@author: combo
'''

import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="root", database="test1")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS visiteurs (
    id int(5) NOT NULL AUTO_INCREMENT,
    name varchar(50) DEFAULT NULL,
    age INTEGER DEFAULT NULL,
    PRIMARY KEY(id) 
);
               """)
user = ("olivier", "31")
#user = {"name" : "Philippe", "age" : "45"}
cursor.execute("""INSERT INTO  visiteurs (name, age) VALUES(%s, %s)""", user)

cursor.execute("""SELECT id, name, age FROM visiteurs WHERE id = %s""", ("5",))
rows = cursor.fetchall()
for row in rows:
    print("{0} : {1} - {2}".format(row[0],row[1],row[2]))
    
conn.close()

if __name__ == '__main__':
    pass