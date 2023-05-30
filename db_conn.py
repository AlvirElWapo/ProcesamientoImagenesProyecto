import mysql.connector

cnx = mysql.connector.connect(
    host="172.17.0.2",
    user="alvirelwapo",
    password="6327",
    database="ProcesamientoDatabase"
)

cursor = cnx.cursor()

