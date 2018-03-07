import pymysql

class MySqlDB(object):

    def __init__(self, command, tableName, count, key, value):
        self.command = command
        self.tableName = tableName
        self.count = count
        self.key = key
        self.value = value

        self.createTable(tableName)
        self.createConn(self)

        if (command == 'insert'):
            self.insertData(tableName, count, key, value)
            pass
        elif (command == 'get'):
            self.fetchAll()
            pass
        else:
            pass

    
    # db is fixed for now
    def createConn(self):
        global c
        global sql
        conn = pymysql.connect(host='localhost', user='root', password='', db='pythontest')
        c = conn.cursor()
        sql = ('select * from' + self.tableName)
        pass

    # creating dynamic database 
    def createTable(tableName):
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

