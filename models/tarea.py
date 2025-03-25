class Tarea:
    def __init__(self, id_tarea, usuario, texto, categoria, estado="Pendiente"):
        self.id_tarea = id_tarea
        self.usuario = usuario
        self.texto = texto
        self.categoria = categoria
        self.estado = estado

    def __str__(self):
        return f"{self.id_tarea}: {self.texto} [{self.categoria}] - {self.estado}"
