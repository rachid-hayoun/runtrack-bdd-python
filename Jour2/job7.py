import mysql.connector

class DB():
    def __init__(self):
        self.mysql = mysql.connector.connect(
            host='localhost',
            user='root',
            password='rachidsql',
            database='entreprise'
        )

class Employe:
    def __init__(self, db):
        self.db = db
        self.cursor = self.db.mysql.cursor()

    def ajout(self, nom, prenom, salaire, id_service):
        self.cursor.execute('INSERT INTO employe (nom, prenom, salaire, id_service) VALUES ('', '', , )', (nom, prenom, salaire, id_service))
        self.db.mysql.commit()

    def supprime(self, nom, prenom, salaire, id_service):
        self.cursor.execute('DELETE FROM employe WHERE nom = '' AND prenom = '' AND salaire =  AND id_service = ', (nom, prenom, salaire, id_service))
        self.db.mysql.commit()

    def afficher_employes(self):
        self.cursor.execute('SELECT * FROM employe')
        
        results = self.cursor.fetchall()  
        result = self.cursor.fetchone()  

        print("Tous les employés:")
        for row in results:
            print(row)

        print("\nPremier employé:")
        print(result)

mysql_db = DB()

employe = Employe(mysql_db)

employe.ajout("Dupont", "Jean", 3000, 1)

employe.supprime("Dupont", "Jean", 3000, 1)

employe.afficher_employes()

employe.cursor.close()
mysql_db.mysql.close()
