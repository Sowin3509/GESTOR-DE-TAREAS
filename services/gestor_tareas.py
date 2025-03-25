from Conexion.ConexionDB import ConexionDB
from models.tarea import Tarea
from models.usuario import Usuario
from exceptions.exceptions import ( TareaNoEncontradaError, EstadoInvalidoError , IDInvalidoError,DescripcionVaciaError,
CategoriaInvalidaError,UsuarioSinTareasError,UsuarioExistenteError,AutenticacionError
)

import sqlite3

import sqlite3

class GestorTareas:
    ESTADOS_VALIDOS = ["Pendiente", "En progreso", "Completada"]

    def __init__(self, db_path="gestor_tareas.db"):  # Recibe la ruta como str
        self.db = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.db.cursor()
        self.crear_tablas()

    def crear_tablas(self):
        """Crea las tablas necesarias en la base de datos si no existen."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL,
                texto TEXT NOT NULL,
                categoria TEXT,
                estado TEXT CHECK(estado IN ('Pendiente', 'En progreso', 'Completada'))
            )
        """)
        self.db.commit()

    def registrar_usuario(self, usuario, contrasena):
        """Registra un nuevo usuario en la base de datos."""
        try:
            self.db.cursor.execute("INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)", (usuario, contrasena))
            self.db.conexion.commit()
            print(f"Usuario '{usuario}' registrado exitosamente.")
        except sqlite3.IntegrityError:
            raise UsuarioExistenteError(f"El usuario '{usuario}' ya existe.")

    def autenticar_usuario(self, usuario, contrasena):
        """Verifica si las credenciales de usuario son correctas."""
        self.db.cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND contrasena = ?", (usuario, contrasena))
        if not self.db.cursor.fetchone():
            raise AutenticacionError("Usuario o contraseña incorrectos.")
        print(f"Usuario '{usuario}' autenticado exitosamente.")
        return True

    def agregar_tarea(self, usuario, texto, categoria):
        """Añade una nueva tarea para el usuario dado."""
        self.db.cursor.execute("INSERT INTO tareas (usuario, texto, categoria, estado) VALUES (?, ?, ?, 'Pendiente')",
                               (usuario, texto, categoria))
        self.db.conexion.commit()
        print("Tarea agregada exitosamente.")

    def obtener_tareas(self, usuario):
        """Devuelve una lista de tareas asignadas a un usuario."""
        self.db.cursor.execute("SELECT id_tarea, texto, categoria, estado FROM tareas WHERE usuario = ?", (usuario,))
        tareas = self.db.cursor.fetchall()
        if not tareas:
            raise UsuarioSinTareasError(f"El usuario '{usuario}' no tiene tareas asignadas.")
        return [Tarea(id_tarea, usuario, texto, categoria, estado) for id_tarea, texto, categoria, estado in tareas]

    def actualizar_tarea(self, id_tarea, nuevo_estado):
        """Actualiza el estado de una tarea si el estado es válido"""


        print(f"Estados permitidos: {', '.join(self.ESTADOS_VALIDOS)}")

        if nuevo_estado not in self.ESTADOS_VALIDOS:
            raise ValueError(f"Estado inválido. Debe ser uno de: {', '.join(self.ESTADOS_VALIDOS)}")

        self.db.cursor.execute(
            "UPDATE tareas SET estado = ? WHERE id_tarea = ?",
            (nuevo_estado, id_tarea)
        )
        self.db.conexion.commit()
        print(f"Tarea {id_tarea} actualizada a estado: {nuevo_estado}")

    def eliminar_tarea(self, id_tarea):
        """Elimina una tarea de la base de datos."""
        self.db.cursor.execute("DELETE FROM tareas WHERE id_tarea = ?", (id_tarea,))
        if self.db.cursor.rowcount == 0:
            raise TareaNoEncontradaError("No se encontró la tarea especificada.")
        self.db.conexion.commit()
        print("Tarea eliminada exitosamente.")
