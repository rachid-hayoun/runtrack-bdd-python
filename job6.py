import mysql.connector

class DB():
    def __init__(self):
        self.mysql = mysql.connector.connect(
            host='localhost',
            user='root',
            password='rachidsql',
            database='laplateforme'
        )

mysql_db = DB()

cursor = mysql_db.mysql.cursor()
cursor.execute('SELECT SUM(capacite) FROM salle;')

results = cursor.fetchall()  
result = cursor.fetchone()   

print(results)
print(result)

cursor.close()
mysql_db.mysql.close() 
