import re
import networkx as nx
import matplotlib.pyplot as plt

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

# Visualización de flujo específico
def visualizar_flujo():
    G = nx.DiGraph()
    
    # Agregar nodos en el orden específico solicitado
    G.add_nodes_from([
        "Mensaje",
        "Opciones",
        "Ingresar al sistema",
        "Registrarse",
        "Menú",
        "Salir"
    ])
    
    # Conectar los nodos exactamente como se pidió
    G.add_edges_from([
        ("Mensaje", "Opciones"),
        ("Opciones", "Ingresar al sistema"),
        ("Opciones", "Registrarse"),
        ("Ingresar al sistema", "Menú"),
        ("Registrarse", "Menú"),
        ("Menú", "Salir")
    ])
    
    # Configurar el gráfico con estilo profesional
    plt.figure(figsize=(10, 6))
    
    # Posicionamiento manual para el flujo solicitado
    pos = {
        "Mensaje": (0.5, 1),
        "Opciones": (0.5, 0.8),
        "Ingresar al sistema": (0.3, 0.6),
        "Registrarse": (0.7, 0.6),
        "Menú": (0.5, 0.4),
        "Salir": (0.5, 0.2)
    }
    
    # Dibujar con colores específicos
    nx.draw(G, pos, with_labels=True, 
            node_color=['#FFD700', '#FFA500', '#32CD32', '#32CD32', '#1E90FF', '#FF6347'],
            node_size=2500, font_size=10, font_weight='bold',
            arrows=True, arrowsize=20, edge_color='gray', width=2)
    
    plt.title("Flujo del Sistema de Pollería", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()

# Funciones para los 4 tipos de grafos
def crear_grafos():
    # Datos comunes para todos los grafos
    nodos = ["User", "Menu", "Product Description"]
    aristas_dirigidas = [("User", "Menu"), ("Menu", "Product Description")]
    aristas_no_dirigidas = [("User", "Menu"), ("Menu", "Product Description"), ("Product Description", "User")]
    aristas_multi = [("User", "Menu"), ("User", "Menu"), ("Menu", "Product Description"), ("Menu", "Product Description")]

    # 1. Grafo Dirigido (DiGraph)
    G_dirigido = nx.DiGraph()
    G_dirigido.add_nodes_from(nodos)
    G_dirigido.add_edges_from(aristas_dirigidas)

    # 2. Multigrafo Dirigido (MultiDiGraph)
    G_multidirigido = nx.MultiDiGraph()
    G_multidirigido.add_nodes_from(nodos)
    G_multidirigido.add_edges_from(aristas_multi)

    # 3. Grafo No Dirigido (Graph)
    G_no_dirigido = nx.Graph()
    G_no_dirigido.add_nodes_from(nodos)
    G_no_dirigido.add_edges_from(aristas_no_dirigidas)

    # 4. Multigrafo No Dirigido (MultiGraph)
    G_multino_dirigido = nx.MultiGraph()
    G_multino_dirigido.add_nodes_from(nodos)
    G_multino_dirigido.add_edges_from(aristas_multi)

    return G_dirigido, G_multidirigido, G_no_dirigido, G_multino_dirigido

def visualizar_grafos():
    G_dirigido, G_multidirigido, G_no_dirigido, G_multino_dirigido = crear_grafos()

    # Configurar subplots
    plt.figure(figsize=(15, 10))

    # 1. Grafo Dirigido
    plt.subplot(2, 2, 1)
    pos = nx.spring_layout(G_dirigido)
    nx.draw(G_dirigido, pos, with_labels=True, node_color='lightblue', node_size=1500, arrows=True)
    plt.title("Grafo Dirigido (DiGraph)")

    # 2. Multigrafo Dirigido
    plt.subplot(2, 2, 2)
    pos = nx.spring_layout(G_multidirigido)
    nx.draw(G_multidirigido, pos, with_labels=True, node_color='lightgreen', node_size=1500, arrows=True)
    plt.title("Multigrafo Dirigido (MultiDiGraph)")

    # 3. Grafo No Dirigido
    plt.subplot(2, 2, 3)
    pos = nx.spring_layout(G_no_dirigido)
    nx.draw(G_no_dirigido, pos, with_labels=True, node_color='lightcoral', node_size=1500)
    plt.title("Grafo No Dirigido (Graph)")

    # 4. Multigrafo No Dirigido
    plt.subplot(2, 2, 4)
    pos = nx.spring_layout(G_multino_dirigido)
    nx.draw(G_multino_dirigido, pos, with_labels=True, node_color='lightyellow', node_size=1500)
    plt.title("Multigrafo No Dirigido (MultiGraph)")

    plt.tight_layout()
    plt.show()

# Inicio del sistema
def inicio():
    print("🍗 Bienvenido al sistema de la Pollería")
    while True:
        print("\nOpciones:")
        print("1. Ingresar al sistema")
        print("2. Registrarse")
        print("3. Ver grafo del sistema")
        print("4. Ver todos los tipos de grafos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            correo = input("Ingrese su correo registrado: ")
            if correo in usuarios_registrados:
                nombre = usuarios_registrados[correo]
                print(f"\n👋 Bienvenido de nuevo, {nombre}!")
                mostrar_precios()
            else:
                print("❌ Correo no encontrado. Por favor regístrese.")
        elif opcion == "2":
            correo, nombre = registrar_usuario()
            if correo and nombre:
                print(f"\n👋 ¡Hola, {nombre}! Gracias por registrarte.")
                mostrar_precios()
        elif opcion == "3":
            visualizar_flujo()
        elif opcion == "4":
            visualizar_grafos()
        elif opcion == "5":
            print("👋 Gracias por visitarnos. ¡Hasta pronto!")
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")

# Ejecutar el sistema
if __name__ == "__main__":
    inicio()