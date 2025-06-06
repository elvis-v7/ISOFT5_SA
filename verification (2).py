import re

# Datos simulados
productos = {
    "Pollo entero": 28.50,
    "1/2 Pollo": 15.00,
    "1/4 Pollo": 9.00,
    "Papas fritas": 5.00,
    "Gaseosa": 3.00
}

usuarios_registrados = {}

# Validaciones
def validar_nombre(nombre):
    return nombre.isalpha()

def validar_usuario(usuario):
    return re.match("^[A-Za-z0-9]+$", usuario) is not None

def validar_correo(correo):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", correo) is not None

# Registro de usuario
def registrar_usuario():
    print("\n📝 Registro de Usuario")
    nombre = input("Ingrese su primer nombre: ")
    if not validar_nombre(nombre):
        print("❌ El nombre solo debe contener letras y sin espacios.")
        return None

    usuario = input("Cree su nombre de usuario (sin símbolos ni espacios): ")
    if not validar_usuario(usuario):
        print("❌ El usuario solo debe contener letras y números.")
        return None

    if usuario in usuarios_registrados:
        print("⚠️ Usuario ya registrado.")
        return None

    correo = input("Ingrese su correo electrónico: ")
    if not validar_correo(correo):
        print("❌ Correo inválido. Asegúrese de incluir '@' y un dominio válido.")
        return None

    usuarios_registrados[usuario] = {"nombre": nombre, "correo": correo}
    print(f"✅ Usuario '{usuario}' registrado exitosamente.")
    return nombre

# Mostrar menú de productos
def mostrar_precios():
    print("\n📋 Lista de Precios")
    for producto, precio in productos.items():
        print(f"- {producto}: $ {precio:.2f}")

# Menú principal
def menu_principal():
    print("🍗 Bienvenido a la Pollería 🐔")

    while True:
        print("\n¿Tiene una cuenta o desea registrarse?")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuario = input("Ingrese su nombre de usuario: ")
            if usuario in usuarios_registrados:
                nombre = usuarios_registrados[usuario]["nombre"]
                print(f"\n👋 ¡Bienvenido de nuevo, {nombre}!")
                mostrar_precios()
            else:
                print("❌ Usuario no encontrado. Regístrese primero.")
        elif opcion == "2":
            nombre = registrar_usuario()
            if nombre:
                print(f"\n👋 ¡Bienvenido, {nombre}!")
                mostrar_precios()
        elif opcion == "3":
            print("👋 Gracias por visitar la pollería.")
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")

# Ejecutar el sistema
if __name__ == "__main__":
    menu_principal()
