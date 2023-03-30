import sqlite3 as sq
import car
con = sq.connect('cars.db')

carList = []


def getDBData():
    with con:
        global carList
        result = con.execute("SELECT * FROM CARS")
        carList = []
        print("Baza danych zawiera:")
        for row in result:
            print(row)
            carList.append(car.Car(row[0], row[1], row[2], row[3], row[4]))
        print("Poprawnie pobrano baze")
            

def setToPayDB(carID, toAdd):
    result = con.execute("SELECT toPay FROM CARS WHERE ID=" + str(carID))
    for row in result:
        toSet = row[0] + toAdd
    con.execute("UPDATE CARS SET toPay=" + str(toSet) + " WHERE ID=" + str(carID))
    
def setPayment(carID, toSubtract):
    result = con.execute("SELECT toPay FROM CARS WHERE ID=" + str(carID))
    for row in result:
        toSet = row[0] - toSubtract
    con.execute("UPDATE CARS SET toPay=" + str(toSet) + " WHERE ID=" + str(carID))
    

getDBData()
