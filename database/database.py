import sqlite3

class ClassName(object):
    def __init__(self, databaseName, tableName):
    conn = sqlite3.connect(databaseName)
    c = conn.cursor()
    
    # calling create table method
    createTable()

    # creating dynamic database 
    def createTable(tableName):
        c.execute('CREATE TABLE IF NOT EXISTS' + tableName + '()')
        
        
        


c.execute('create database if not exists')

db.close()
