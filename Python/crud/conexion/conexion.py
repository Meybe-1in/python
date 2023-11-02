import sqlite3

# Conexión a la base de datos SQLite (creará un archivo si no existe)
conn = sqlite3.connect('mi_base_de_datos.db')
cursor = conn.cursor()

# Crear una tabla
cursor.execute('''CREATE TABLE IF NOT EXISTS empleados (
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                cargo TEXT NOT NULL,
                salario REAL NOT NULL
                )''')


# Función para crear un nuevo registro
def crear_empleado(nombre, cargo, salario):
    cursor.execute("INSERT INTO empleados (nombre, cargo, salario) VALUES (?, ?, ?)", (nombre, cargo, salario))
    conn.commit()

# Función para leer todos los registros
def leer_empleados():
    cursor.execute("SELECT * FROM empleados")
    empleados = cursor.fetchall()
    for empleado in empleados:
        print(empleado)

# Función para actualizar un registro por ID
def actualizar_empleado(id, nuevo_salario):
    cursor.execute("UPDATE empleados SET salario = ? WHERE id = ?", (nuevo_salario, id))
    conn.commit()

# Función para eliminar un registro por ID
def eliminar_empleado(id):
    cursor.execute("DELETE FROM empleados WHERE id = ?", (id,))
    conn.commit()

# Ejemplo de uso
crear_empleado("Juan Pérez", "Gerente", 50000.0)
crear_empleado("María López", "Analista", 35000.0)
leer_empleados()

actualizar_empleado(1, 55000.0)
eliminar_empleado(2)

print("Después de actualizar y eliminar:")
leer_empleados()

# Cerrar la conexión a la base de datos
conn.close()
