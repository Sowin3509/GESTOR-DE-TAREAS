import sqlite3

class ConexionDB:
    def __init__(self):
        self.conexion = sqlite3.connect("gestor_tareas.db")
        self.cursor = self.conexion.cursor()
        self._crear_tablas()

    def _crear_tablas(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                usuario TEXT PRIMARY KEY,
                contrasena TEXT NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tareas (
                id_tarea INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT,
                texto TEXT NOT NULL,
                categoria TEXT,
                estado TEXT CHECK(estado IN ('Pendiente', 'Completada')),
                FOREIGN KEY(usuario) REFERENCES usuarios(usuario)
            )
        """)
        self.conexion.commit()

    def cerrar(self):
        self.conexion.close()
