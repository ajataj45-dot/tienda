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
    INSERT INTO clientes (nombre, apellidos, telefono)
    VALUES ('Juan', 'Perez Gomes', '12345678')
    """
)
conn.commit()



print("\nCLIENTES")
cursor = conn.execute("SELECT * FROM clientes")
for fila in cursor:
    print(fila)
    