import mysql.connector

class DB():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'rachidsql',
            database = 'zoo'
        )
class Zoo():
    def __init__(self,db):
        self.db = db
        self.cursor = self.db.mysql.cursor()
    
    def toutafficher(self):
        self.execute.cursor('SELECT*FROM animal')
        self.db.mysql.commit()

        results = self.cursor.fetchall()  
        result = self.cursor.fetchone()  

        print("Tous les animaux;")
        for row in results:
            print(row)

        print(":")
        print(result)

    def ajtanimal(self,nom,race,date_de_naissance,pays_d_origine):
        self.cursor.execute("INSERT INTO animal (nom, race, date_de_naissance, pays_d_origine)VALUES (%s, %s, %s, %s)", ('chat', 'félin', '2023-03-25', 'France', 'chat2', 'félin2', '2023-04-01', 'Italie'))        
        self.db.mysql.commit()

    def supanimal(self,nom,race,date_de_naissance,pays_d_origine):
        self.cursor.execute("DELETE FROM animal WHERE nom = %s", (nom,))        
        self.db.mysql.commit()

    def ajtcage(self,superficie,capacite_max):
        self.cursor.execute("INSERT INTO cage (superficie,capacite_max)VALUES (%s, %s)", ('150', '300'))        
        self.db.mysql.commit()

    def supcage(self,superficie,capacite_max):
        self.cursor.execute("DELETE FROM cage WHERE id  = %s", (id,))        
        self.db.mysql.commit()
