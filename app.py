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
    CREATE TABLE IF NOT EXISTS pedidos(
        id INTEGER PRIMARY KEY,
        fecha_pedido DATE NOT NULL,
        cantidad INTEGER NOT NULL,
        cliente_id  INTEGER NOT NULL,
        producto_id INTEGER NOT NULL,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id),
        FOREIGN KEY (producto_id) REFERENCES productos(id)
    )
    """
)


print("\nCLIENTES")
cursor = conn.execute("SELECT * FROM clientes")
for fila in cursor:
    print(fila)
    
    
print("\nPRODUCTOS")
cursor = conn.execute("SELECT * FROM productos")
for fila in cursor:
    print(fila)
    
    
print("\nPEDIDOS")
cursor = conn.execute("SELECT * FROM pedidos")
for fila in cursor:
    print(fila)







    