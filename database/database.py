import sqlite3

class DatabaseClass(object):
    def __init__(self, databaseName, tableName):
        conn = sqlite3.connect(databaseName)
        self.c = conn.cursor()
    
        # calling create table method
        self.createTable(tableName)

    # creating dynamic database 
    def createTable(self, tableName):
        self.c.execute('CREATE TABLE IF NOT EXISTS' + tableName + '()')
        
        
        


    self.c.execute('create database if not exists')

    db.close()
