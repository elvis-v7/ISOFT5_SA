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

def validar_correo(correo):
    return re.match("^[A-Za-z0-9]+$", correo) is not None

# Registro de usuario
def registrar_usuario():
    print("\n📝 Registro de Usuario")
    nombre = input("Ingrese su primer nombre: ")
    if not validar_nombre(nombre):
        print("❌ El nombre solo debe contener letras.")
        return None, None

    correo = input("Ingrese su correo electrónico: ")
    if not validar_correo(correo):
        print("❌ Correo inválido. Intente nuevamente.")
        return None, None

    if correo in usuarios_registrados:
        print("⚠️ Ya existe un usuario con este correo.")
        return None, None
    else:
        usuarios_registrados[correo] = nombre
        print(f"✅ Registro exitoso. ¡Bienvenido, {nombre}!")
        return correo, nombre

# Mostrar menú de productos
def mostrar_precios():
    print("\n📋 Lista de Precios")
    for producto, precio in productos.items():
        print(f"- {producto}: $ {precio:.2f}")

# Inicio del sistema
def inicio():
    print("🍗 Bienvenido al sistema de la Pollería")
    while True:
        print("\n¿Tiene una cuenta?")
        print("1. Sí, tengo una cuenta")
        print("2. No, deseo registrarme")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            correo = input("Ingrese su correo registrado: ")
            if correo in usuarios_registrados:
                nombre = usuarios_registrados[correo]
                print(f"\n👋 Bienvenido de nuevo, {nombre}!")
                mostrar_precios()
                break
            else:
                print("❌ Correo no encontrado. Por favor regístrese.")
        elif opcion == "2":
            correo, nombre = registrar_usuario()
            if correo and nombre:
                print(f"\n👋 ¡Hola, {nombre}! Gracias por registrarte.")
                mostrar_precios()
                print("3. Salir")
                opcion = input("Seleccione 3 para salir: ")
                if opcion == "3":
                    print("👋 Gracias por visitarnos. ¡Hasta pronto!")
                    break
                else:
                    print("❌ Opción no válida. Intente de nuevo.")
                
        elif opcion == "3":
            print("👋 Gracias por visitarnos. ¡Hasta pronto!")
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")
 
# Ejecutar el sistema
if __name__ == "__main__":
    inicio()

