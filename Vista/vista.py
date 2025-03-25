from exceptions.exceptions import (
    UsuarioExistenteError, UsuarioNoEncontradoError,
    AutenticacionError, UsuarioSinTareasError, TareaNoEncontradaError
)
from services.gestor_tareas import GestorTareas

class Vista:
    def __init__(self, gestor):
        self.gestor = gestor

    def mostrar_inicio(self):
        usuario = None
        while not usuario:
            print("\n🔹 Bienvenido al Gestor de Tareas 🔹")
            print("1. Registrarse")
            print("2. Iniciar sesión")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                usuario = self.registrar_usuario()
            elif opcion == "2":
                usuario = self.iniciar_sesion()
            elif opcion == "3":
                print("👋 Saliendo del sistema...")
                return
            else:
                print("❌ Opción inválida. Intente de nuevo.")

        self.mostrar_menu(usuario)  # Ir al menú principal si el usuario inicia sesión

    def registrar_usuario(self):
        print("\n🔹 Registro de usuario")
        usuario = input("Ingrese un nombre de usuario: ")
        contraseña = input("Ingrese una contraseña: ")
        try:
            self.gestor.registrar_usuario(usuario, contraseña)
            print(f"✅ Usuario '{usuario}' registrado con éxito.")
            return usuario
        except UsuarioExistenteError as e:
            print(f"⚠️ {e}")
            return None

    def iniciar_sesion(self):
        print("\n🔹 Inicio de sesión")
        usuario = input("Ingrese su usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        try:
            if self.gestor.autenticar_usuario(usuario, contraseña):
                print(f"✅ Bienvenido, {usuario}!")
                return usuario
        except (UsuarioNoEncontradoError, AutenticacionError) as e:
            print(f"⚠️ {e}")
        return None

    def mostrar_menu(self, usuario):
        while True:
            print(f"\n🔹 Menú Principal (Usuario: {usuario}) 🔹")
            print("1. Agregar tarea")
            print("2. Ver tareas")
            print("3. Actualizar tarea")
            print("4. Eliminar tarea")
            print("5. Cerrar sesión")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_tarea(usuario)
            elif opcion == "2":
                self.ver_tareas(usuario)
            elif opcion == "3":
                self.actualizar_estado_tarea(usuario)
            elif opcion == "4":
                self.eliminar_tarea(usuario)
            elif opcion == "5":
                print("👋 Cerrando sesión...")
                break
            else:
                print("❌ Opción inválida. Intente de nuevo.")

    def agregar_tarea(self, usuario):
        descripcion = input("Ingrese la descripción de la tarea: ")
        categoria = input("Ingrese la categoría: ")
        try:
            self.gestor.agregar_tarea(usuario, descripcion, categoria)
            print("✅ Tarea agregada correctamente.")
        except Exception as e:
            print(f"⚠️ Error: {e}")

    def ver_tareas(self, usuario):
        try:
            tareas = self.gestor.obtener_tareas(usuario)
            if not tareas:
                print("⚠️ No tienes tareas registradas.")
                return
            print("\n📌 Tus Tareas:")
            for tarea in tareas:
                print(f"- [{tarea.id_tarea}] {tarea.texto} ({tarea.categoria}) - {tarea.estado}")
        except UsuarioSinTareasError as e:
            print(f"⚠️ {e}")

    def actualizar_estado_tarea(self, usuario):
        id_tarea = input("Ingrese el ID de la tarea a actualizar: ")

        # Mostrar estados válidos antes de pedir el nuevo estado
        print(f"Estados disponibles: {', '.join(GestorTareas.ESTADOS_VALIDOS)}")
        nuevo_estado = input("Ingrese el nuevo estado: ")

        try:
            self.gestor.actualizar_tarea(id_tarea, nuevo_estado)
        except ValueError as e:
            print(f"❌ Error: {e}")

    def eliminar_tarea(self, usuario):
        tarea_id = input("Ingrese el ID de la tarea a eliminar: ")
        try:
            self.gestor.eliminar_tarea(tarea_id)
            print("✅ Tarea eliminada correctamente.")
        except TareaNoEncontradaError as e:
            print(f"⚠️ {e}")
