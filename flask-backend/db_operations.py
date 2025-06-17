import mysql.connector
import os

mysql_host=os.environ.get("MYSQL_HOST")
mysql_user=os.environ.get("MYSQL_USER")
mysql_db=os.environ.get("MYSQL_DATABASE")

with open("/run/secrets/db-password","r") as file:
    mysql_pass=file.read()

class DBManager:
    def __init__(self, host=mysql_host, user=mysql_user, password=mysql_pass, database=mysql_db):
        self.connection=mysql.connector.connect(host=host, user=user, password=password, database=database)
        self.cursor=self.connection.cursor()

    def insert_data(self,id, name, email, course, marks):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Student_Marks (ID INT, Name VARCHAR(50), Email VARCHAR(50), ' \
        'Course VARCHAR(10), Marks INT, Submitted_Date DATETIME DEFAULT CURRENT_TIMESTAMP)')
        self.cursor.execute('INSERT INTO Student_Marks (ID, Name, Email, Course, Marks) VALUES (%s,%s,%s,%s,%s)',
                            (id, name, email, course, marks))
        self.connection.commit()

    def query_data(self):
        self.cursor.execute('SELECT * FROM Student_Marks ORDER BY Submitted_Date DESC LIMIT 5')
        return self.cursor
