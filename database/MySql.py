import pymysql

class MySqlDB(object):
    cursor
    sql

    def __init__(self, command, tableName, count, key, value):
        self.command = command
        self.tableName = tableName
        self.count = count
        self.key = key
        self.value = value

        self.createConn()
        self.createTable(tableName)

        if (command == 'insert'):
            self.insertData(self.tableName, self.count, self.key, self.value)
            pass
        elif (command == 'get'):
            self.fetchAll()
            pass
        else:
            pass

    
    # db is fixed for now
    def createConn(self):
        conn = pymysql.connect(host='localhost', user='root', password='', db='pythontest')
        MySqlDB.cursor = conn.cursor()
        MySqlDB.sql = ('select * from' + self.tableName)
        pass

    # creating dynamic database 
    def createTable(self, tableName):
        MySqlDB.cursor.execute('CREATE TABLE IF NOT EXISTS' + tableName + '(count REAL, key TEXT, value TEXT)')
    
    # fetch all data
    @staticmethod
    def fetchAll():
        MySqlDB.cursor.execute(MySqlDB.sql)
        return MySqlDB.cursor.fetchall()
        pass

    # insert Data
    def insertData(self, tableName, count, key, value):
        MySqlDB.cursor.execute('INSERT INTO' + tableName + 'VALUES('+ count +', '+ key +' '+ value +')')
        pass 


# MySqlDB()

