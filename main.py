import cv2
import subprocess
from db_conn import cursor

cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(0)


rico_Pollo = cv2.CascadeClassifier('cascade.xml')
atun = cv2.CascadeClassifier('atun.xml')
leche= cv2.CascadeClassifier('leche.xml')
sopa = cv2.CascadeClassifier('sopa.xml')
avena = cv2.CascadeClassifier('avena.xml')
palomita = cv2.CascadeClassifier('palomita.xml')
te = cv2.CascadeClassifier('te.xml')
colgate = cv2.CascadeClassifier('colgate.xml')
jumex = cv2.CascadeClassifier('jumex.xml')
gelatina = cv2.CascadeClassifier('gelatina.xml')

while True:

    ret,frame = cap.read()
    frame2 = frame;
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    RP = rico_Pollo.detectMultiScale(gray,
            scaleFactor = 4,
            minNeighbors = 91,
            minSize=(70,98))

    tuny = atun.detectMultiScale(gray,
            scaleFactor = 10,
            minNeighbors = 5,
            minSize=(70,98))

    milk = leche.detectMultiScale(gray,
            scaleFactor = 5,
            minNeighbors = 91,
            minSize=(90,110))

    soup = sopa.detectMultiScale(gray,
            scaleFactor = 6,
            minNeighbors = 91,
            minSize=(90,110))

    oatmeal = avena.detectMultiScale(gray,
            scaleFactor = 6,
            minNeighbors = 91,
            minSize=(70,98))

    popcorn = palomita.detectMultiScale(gray,
            scaleFactor = 6,
            minNeighbors = 91,
            minSize=(90,110))

    tea = te.detectMultiScale(gray,
            scaleFactor = 4,
            minNeighbors = 91,
            minSize=(70,98))

    colg8 = colgate.detectMultiScale(gray,
            scaleFactor = 6,
            minNeighbors = 200,
            minSize=(70,110))

    jmex = jumex.detectMultiScale(gray,
            scaleFactor = 6,
            minNeighbors = 200,
            minSize=(70,110))

    gelat = gelatina.detectMultiScale(gray,
            scaleFactor = 6,
            minNeighbors = 200,
            minSize=(70,110))

    for (x,y,w,h) in RP:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(109, 191, 209),2)
        cv2.putText(frame,'Rico Pollo',(x,y-10),2,0.7,(109, 191, 209),2,cv2.LINE_AA)

    for (x,y,w,h) in tuny:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(149, 125, 173),2)
        cv2.putText(frame,'Atún',(x,y-10),2,0.7,(149, 125, 173),2,cv2.LINE_AA)

    for (x,y,w,h) in milk:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(255, 172, 99),2)
        cv2.putText(frame,'Leche',(x,y-10),2,0.7,(255, 172, 99),2,cv2.LINE_AA)

    for (x,y,w,h) in soup:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(255, 172, 99),2)
        cv2.putText(frame,'SOPA',(x,y-10),2,0.7,(255, 172, 99),2,cv2.LINE_AA)

    for (x,y,w,h) in oatmeal:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(255, 172, 99),2)
        cv2.putText(frame,'avena',(x,y-10),2,0.7,(255, 172, 99),2,cv2.LINE_AA)
    
    for (x,y,w,h) in popcorn:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(255, 172, 99),2)
        cv2.putText(frame,'Palomitas',(x,y-10),2,0.7,(255, 172, 99),2,cv2.LINE_AA)

    for (x,y,w,h) in tea:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(255, 172, 99),2)
        cv2.putText(frame,'te de tila',(x,y-10),2,0.7,(255, 172, 99),2,cv2.LINE_AA)
    
    for (x,y,w,h) in colg8:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(255, 172, 99),2)
        cv2.putText(frame,'pasta de dientes',(x,y-10),2,0.7,(255, 172, 99),2,cv2.LINE_AA)

    for (x,y,w,h) in jmex:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(255, 172, 99),2)
        cv2.putText(frame,'jumex',(x,y-10),2,0.7,(255, 172, 99),2,cv2.LINE_AA)

    for (x,y,w,h) in gelat:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(255, 172, 99),2)
        cv2.putText(frame,'gelatina',(x,y-10),2,0.7,(255, 172, 99),2,cv2.LINE_AA)

    cv2.imshow('identificar_objeto',frame)

    key_press = cv2.waitKey(1);

    if key_press  == ord('s'):
        cv2.imwrite("./imagen_req.jpg", frame2)
        subprocess.Popen(['python3', 'agregar_db.py', './imagen_req.jpg'])
        
    if key_press == 27:
        break


cap.release()
cv2.destroyAllWindows()


# SQL query
sql = "SELECT prd.name, COUNT(prd.name), ldc.id " \
      "FROM Producto_disponible prd " \
      "JOIN lista_de_compras ldc ON ldc.producto_id = prd.id " \
      "GROUP BY prd.name"

cursor.execute(sql)

results = cursor.fetchall()


print(".____    .__          __               .___       _________                                            ")
print("|    |   |__| _______/  |______      __| _/____   \_   ___ \  ____   _____ __________________    ______")
print("|    |   |  |/  ___/\   __\__  \    / __ |/ __ \  /    \  \/ /  _ \ /     \\____ \_  __ \__  \  /  ___/")
print("|    |___|  |\___ \  |  |  / __ \_ / /_/ \  ___/  \     \___(  <_> )  Y Y  \  |_> >  | \// __ \_\___ \ ")
print("|_______ \__/____  > |__| (____  / \____ |\___  >  \______  /\____/|__|_|  /   __/|__|  (____  /____  >")
print("        \/       \/            \/       \/    \/          \/             \/|__|              \/     \/ ")


for result in results:
    name = result[0]
    count = result[1]
    ldc_id = result[2]

    print("Nombre del Producto:", name)
    print("Cantidad a Comprar:", count)
    print("ID en Lista:", ldc_id)
    print("---")

