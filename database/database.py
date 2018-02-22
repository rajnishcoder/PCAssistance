import sqlite3

class ClassName(object):
    def __init__(self, databaseName):
    conn = sqlite3.connect(databaseName)
    c = conn.cursor()

    #creating database 
    def createTable():
        c.execute('CREATE TABLE IF NOT EXISTS')
        
        
        


c.execute('create database if not exists')

db.close()
