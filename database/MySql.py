import pymysql

class MySqlDB(object):
    def __init__(self, command, tableName, count, key, value):
        self.createTable(tableName)
        if (command == 'insert'):
            self.insertData(tableName, count, key, value)
            pass
        elif (command == 'get'):
            self.fetchAll()
            pass
        else:
            pass

    
    # db is fixed for now
    conn = pymysql.connect(host='localhost', user='root', password='', db='pythontest')
    c = conn.cursor()
    sql = ('select * from' + tableName)

    # creating dynamic database 
    def createTable(tableName):
        global c
        global sql
        c.execute('CREATE TABLE IF NOT EXISTS' + tableName + '(count REAL, key TEXT, value TEXT)')
    
    # fetch all data
    @staticmethod
    def fetchAll():
        c.execute(sql)
        return c.fetchall()
        pass

    # insert Data
    def insertData(tableName, count, key, value):
        c.execute('INSERT INTO' + tableName + 'VALUES('+ count +', '+ key +' '+ value +')')
        pass 


# MySqlDB()

