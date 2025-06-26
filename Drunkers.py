import time
import random

# Acciones disponibles
acciones = ["baño", "borracho", "llamar a la ex", "cantar"]

# Borrachitos
borrachos = ["Borrachito 0", "Borrachito 1", "Borrachito 2", "Borrachito 3", "Borrachito 4"]

# Definición de cada acción
def tomar(nombre):
    print(f"{nombre} está tomando cerveza 🍺")
    time.sleep(1)

def cantar(nombre):
    print(f"{nombre} está cantando 🎤")
    time.sleep(1)

def baño(nombre):
    print(f"{nombre} fue al baño 🚽")
    time.sleep(1)
    print(f"{nombre} salió del baño 🚪")

def llamar_ex(nombre):
    print(f"{nombre} está llamando a su ex 📞💔")
    time.sleep(1)
    print(f"{nombre} colgó la llamada 📴")

# Acciones mapeadas a funciones
funciones = {
    "baño": baño,
    "borracho": tomar,
    "llamar a la ex": llamar_ex,
    "cantar": cantar
}

# Ejecutar 4 ciclos
for ciclo in range(4):
    print(f"\n--- CICLO {ciclo + 1} ---")
    random.shuffle(borrachos)  # Cambiar orden para que cada ciclo sea diferente
    
    baño_usado = False
    llamada_usada = False

    for i, borracho in enumerate(borrachos):
        # Elegir acción respetando restricciones
        posibles = acciones.copy()
        if baño_usado:
            posibles.remove("baño")
        if llamada_usada:
            posibles.remove("llamar a la ex")

        accion = random.choice(posibles)

        if accion == "baño":
            baño_usado = True
        elif accion == "llamar a la ex":
            llamada_usada = True

        funciones[accion](borracho)

    print(f"--- FIN CICLO {ciclo + 1} ---")
    time.sleep(2)
