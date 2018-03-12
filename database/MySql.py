import pymysql

class MySqlDB(object):

    def __init__(self, command, tableName, count, key, value):
        self.command = command
        self.tableName = tableName
        self.count = count
        self.key = key
        self.value = value

        self.conn = pymysql.connect(host='localhost', user='root', password='', db='pythontest')
        self.cursor = self.conn.cursor()
        self.sql = ('select * from' + self.tableName)

        # self.createConn()
        self.createTable(tableName)

        if (command == 'insert'):
            self.insertData(self.tableName, self.count, self.key, self.value)
            pass
        elif (command == 'get'):
            self.fetchAll(self)
            pass
        else:
            pass

    
    # db is fixed for now
    # def createConn(self):
    #     conn = pymysql.connect(host='localhost', user='root', password='', db='pythontest')
    #     MySqlDB.cursor = conn.cursor()
    #     MySqlDB.sql = ('select * from' + self.tableName)
    #     pass

    # creating dynamic database 
    def createTable(self, tableName):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS TesttableName(count INT, progName TEXT, progPath TEXT)')
    
    # fetch all data
    @staticmethod
    def fetchAll(self):
        self.cursor.execute(self.sql)
        return self.cursor.fetchall()
        pass

    # insert Data
    def insertData(self, tableName, count, key, value):
        self.cursor.execute('INSERT INTO' + tableName + 'VALUES('+ count +', '+ key +' '+ value +')')
        pass 

testCount = 1

MySqlDB('insert', 'TesttableName', testCount, 'testKey', 'testvalue')
