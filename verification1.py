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

# Función de validación de nombre (solo letras)
def validar_nombre(nombre):
    return nombre.isalpha()

# Función de validación de usuario (alfanumérico sin símbolos)
def validar_usuario(usuario):
    return re.match("^[A-Za-z0-9]+$", usuario) is not None

# Registro de usuario
def registrar_usuario():
    print("📝 Registro de Usuario")
    nombre = input("Ingrese su primer nombre: ")
    if not validar_nombre(nombre):
        print("❌ El nombre solo debe contener letras y sin espacios.")
        return
    
    usuario = input("Cree su nombre de usuario (sin símbolos ni espacios): ")
    if not validar_usuario(usuario):
        print("❌ El usuario no debe contener ni simbolos ni espacios.")
        return
    
    if usuario in usuarios_registrados:
        print("⚠️ Usuario ya registrado.")
    else:
        usuarios_registrados[usuario] = nombre
        print(f"✅ Usuario '{usuario}' registrado exitosamente.")

# Mostrar menú de productos
def mostrar_precios():
    print("\n📋 Lista de Precios")
    for producto, precio in productos.items():
        print(f"- {producto}: $ {precio:.2f}")

# Menú principal
def menu_principal():
    print("\n🍗 Bienvenido al Sistema de Pollería")
    while True:
        print("\nMenú Principal:")
        print("1. Registrar usuario")
        print("2. Ver precios")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            mostrar_precios()
        elif opcion == "3":
            print("👋 Gracias por visitar la pollería.")
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")

# Ejecutar el sistema
if __name__ == "__main__":
    menu_principal()
