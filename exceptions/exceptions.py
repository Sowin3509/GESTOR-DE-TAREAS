class TareaNoEncontradaError(Exception):
    def __init__(self, tarea_id, mensaje="La tarea no fue encontrada."):
        self.tarea_id = tarea_id
        self.codigo_error = 404
        super().__init__(f"{mensaje} (ID: {tarea_id})")

class EstadoInvalidoError(Exception):
    def __init__(self, estado, mensaje="El estado proporcionado no es válido."):
        self.estado = estado
        self.codigo_error = 400
        super().__init__(f"{mensaje} Estado: {estado}")

class IDInvalidoError(Exception):
    def __init__(self, id_recibido, mensaje="El ID proporcionado no es válido."):
        self.id_recibido = id_recibido
        self.codigo_error = 400
        super().__init__(f"{mensaje} ID recibido: {id_recibido}")

class DescripcionVaciaError(Exception):
    def __init__(self, mensaje="La descripción de la tarea no puede estar vacía."):
        self.codigo_error = 422
        super().__init__(mensaje)

class CategoriaInvalidaError(Exception):
    def __init__(self, categoria, mensaje="La categoría proporcionada no es válida."):
        self.categoria = categoria
        self.codigo_error = 400
        super().__init__(f"{mensaje} Categoría: {categoria}")

class UsuarioSinTareasError(Exception):
    def __init__(self, usuario, mensaje="El usuario no tiene tareas asignadas."):
        self.usuario = usuario
        self.codigo_error = 404
        super().__init__(f"{mensaje} Usuario: {usuario}")

class UsuarioNoEncontradoError(Exception):
    """Excepción para cuando un usuario no se encuentra en la base de datos."""
    def __init__(self, usuario):
        super().__init__(f"El usuario '{usuario}' no se encontró en la base de datos.")

class UsuarioExistenteError(Exception):
    """Excepción para cuando un usuario ya está registrado en la base de datos."""
    def __init__(self, usuario):
        super().__init__(f"El usuario '{usuario}' ya existe.")

class AutenticacionError(Exception):
    """Excepción para cuando las credenciales de usuario son incorrectas."""
    def __init__(self):
        super().__init__("Usuario o contraseña incorrectos.")

