import sqlite3 as sq

con = sq.connect('cars.db')

with con:
    con.execute("""
        CREATE TABLE CARS(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            plate TEXT NOT NULL UNIQUE,
            model TEXT,
            color TEXT,
            toPay float
        );
    """)
    
sql = "INSERT INTO CARS (plate, model, color, toPay) VALUES(?, ?, ?, ?)"
data = [
    ("SB 841AL", "Ferrari 360", "red", 12.45),
    ("GTC 21156", "Audi TT", "red", 6.50),
    ("WCI 48323", "Ferrari 599", "black", 11.10)
]

with con:
    con.executemany(sql, data)
    
with con:
    result = con.execute("SELECT * FROM CARS")
    for row in result:
        print(row)
