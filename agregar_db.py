import cv2
import sys
import mysql.connector
from db_conn import cursor, cnx


# Get the screenshot path from the command-line argument
screenshot_path = sys.argv[1]

# Load the captured image
image = cv2.imread(screenshot_path)

if image is not None:
    print("IMAGEN CARGADA!!")
else:
    print("Failed to load the captured image.")

rico_Pollo = cv2.CascadeClassifier('cascade.xml')
atun = cv2.CascadeClassifier('atun.xml')
leche= cv2.CascadeClassifier('leche.xml')
sopa = cv2.CascadeClassifier('sopa.xml')
avena = cv2.CascadeClassifier('avena.xml')
palomita = cv2.CascadeClassifier('palomita.xml')
te = cv2.CascadeClassifier('te.xml')
colgate = cv2.CascadeClassifier('colgate.xml')


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

RP = rico_Pollo.detectMultiScale(gray,
        scaleFactor = 4,
        minNeighbors = 91,
        minSize=(70,98))

tuny = atun.detectMultiScale(gray,
        scaleFactor = 10,
        minNeighbors = 5,
        minSize=(70,98))

milk = leche.detectMultiScale(gray,
        scaleFactor = 8,
        minNeighbors = 91,
        minSize=(90,110))

soup = sopa.detectMultiScale(gray,
        scaleFactor = 6,
        minNeighbors = 91,
        minSize=(90,110))

oatmeal = avena.detectMultiScale(gray,
        scaleFactor = 6,
        minNeighbors = 91,
        minSize=(90,110))

popcorn = palomita.detectMultiScale(gray,
        scaleFactor = 6,
        minNeighbors = 91,
        minSize=(90,110))

tea = te.detectMultiScale(gray,
        scaleFactor = 6,
        minNeighbors = 91,
        minSize=(90,110))

colg8 = colgate.detectMultiScale(gray,
        scaleFactor = 6,
        minNeighbors = 91,
        minSize=(90,110))

### id Productos
### 1 Atun, 2 Sopa, 3, Gelatina, 4 te, 5 Avena,
### 6 Leche, 7 rico pollo, 8 jumex, 9 palomitas, 10 colgate

for (x,y,w,h) in RP:
    print("RICO POLLO ENCONTRADO!!")
    sql = "INSERT INTO lista_de_compras(producto_id) VALUES (%s)"
    values = ("7",)
    cursor.execute(sql, values)
    cnx.commit()

for (x,y,w,h) in tuny:
    print("ATUN ENCONTRADO!")
    sql = "INSERT INTO lista_de_compras(producto_id) VALUES (%s)"
    values = ("1",);
    cursor.execute(sql, values)
    cnx.commit()

for (x,y,w,h) in milk:
    print("LECHE ENCONTRADA!")
    sql = "INSERT INTO lista_de_compras(producto_id) VALUES (%s)"
    values = ("6",);
    cursor.execute(sql, values)
    cnx.commit()

for (x,y,w,h) in soup:
    print("SOPA ENCONTRADA!")
    sql = "INSERT INTO lista_de_compras(producto_id) VALUES (%s)"
    values = ("2",);
    cursor.execute(sql, values)
    cnx.commit()

for (x,y,w,h) in oatmeal:
    print("AVENA ENCONTRADA!")
    sql = "INSERT INTO lista_de_compras(producto_id) VALUES (%s)"
    values = ("5",);
    cursor.execute(sql, values)
    cnx.commit()

for (x,y,w,h) in popcorn:
    print("PALOMITAS ENCONTRADAS!")
    sql = "INSERT INTO lista_de_compras(producto_id) VALUES (%s)"
    values = ("9",);
    cursor.execute(sql, values)
    cnx.commit()

for (x,y,w,h) in tea:
    print("TÉ ENCONTRADO!")
    sql = "INSERT INTO lista_de_compras(producto_id) VALUES (%s)"
    values = ("4",);
    cursor.execute(sql, values)
    cnx.commit()

for (x,y,w,h) in colg8:
    print("PASTA DE DIENTES ENCONTRADO!")
    sql = "INSERT INTO lista_de_compras(producto_id) VALUES (%s)"
    values = ("10",);
    cursor.execute(sql, values)
    cnx.commit()




