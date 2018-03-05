import pymysql

class MySqlDB(object):
    def __init__(self, command, tableName, count, key, value):
        createTable(tableName)

    
    # db is fixed for now
    conn = pymysql.connect(host='localhost', user='root', password='', db='pyhontest')
    c = conn.cursor()
    sql = ('select * from' + tableName)

    # creating dynamic database 
    def createTable(tableName):
        global c
        global sql
        c.execute('CREATE TABLE IF NOT EXISTS' + tableName + '(count REAL, key TEXT, value TEXT)')
    
    # fetch all data
    def fetchAll():
        c.execute(sql)
        return c.fetchall()
        pass

    # insert Data
    def insertData(tableName, count, key, value):
        c.execute('INSERT INTO' + tableName + 'VALUES('+ count +', '+ key +' '+ value +')')
        pass 


# MySqlDB()

