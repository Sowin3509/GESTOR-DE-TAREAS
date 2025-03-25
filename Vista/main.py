from Vista.vista import Vista
from Conexion.ConexionDB import ConexionDB
from services.gestor_tareas import GestorTareas

def main():
    db = ConexionDB()
    gestor = GestorTareas(db)
    vista = Vista(gestor)
    vista.mostrar_inicio()  # Aquí se inicia

if __name__ == "__main__":
    main()
