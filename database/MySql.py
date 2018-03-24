import pymysql

class MySqlDB(object):
    print('working')

    def __init__(self, command, tableName, count, key, value):
        self.command = command
        self.tableName = tableName
        self.count = count
        self.key = key
        self.value = value

        self.conn = pymysql.connect(host='localhost', user='root', password='', db='pythontest')
        self.cursor = self.conn.cursor()
        self.sql = ('select * from' + self.tableName)
        print('working2')

        # self.createConn()
        # self.createTable(tableName)

        if (command == 'insert'):
            print('working3')
            self.insertData()
        elif (command == 'get'):
            self.fetchAll(self)
        else:
            pass

    
    # db is fixed for now
    # def createConn(self):
    #     conn = pymysql.connect(host='localhost', user='root', password='', db='pythontest')
    #     MySqlDB.cursor = conn.cursor()
    #     MySqlDB.sql = ('select * from' + self.tableName)
    #     pass

    # creating dynamic database 
    # def createTable(self, tableName):
    #     self.cursor.execute('CREATE TABLE IF NOT EXISTS TesttableName(count INT, progName TEXT, progPath TEXT)')
    
    # fetch all data
    @staticmethod
    def fetchAll(self):
        self.cursor.execute(self.sql)
        return self.cursor.fetchall()

    # insert Data
    def insertData(self):
        print('working4')
        self.cursor.execute('INSERT INTO' + self.tableName + 'VALUES('+ self.count +', '+ self.key +' '+ self.value +')')
        print('workingasdasd')
        

testCount = 4
print('working5')
MySqlDB('insert', 'TesttableName', '6', 'testKey', 'testvalue')
print('working6')
