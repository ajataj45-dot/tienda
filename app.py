import sqlite3

conn = sqlite3.connect('tienda.db')

conn.execute(
    """
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellidos TEXT NOT NULL,
        telefono TEXT NOT NULL
    )
    """
)


conn.execute(
    """
    CREATE TABLE IF NOT EXISTS productos(
        id INTEGER PRIMARY KEY,
        nombre_producto TEXT NOT NULL,
        precio REAL NOT NULL,
        stock INTEGER DEFAULT 0
    )
    """
)



conn.execute(
    """
    INSERT INTO productos (nombre_producto, precio, stock)
    VALUES ('Piña', '15.5', '15')
    """
)
conn.commit()






    