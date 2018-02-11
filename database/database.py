import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="")

c = db.cursor()
c.execute('create database if not exists')

db.close()
