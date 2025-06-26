import time
import random

# Estados globales para controlar recursos compartidos
baño_disponible = True
telefono_disponible = True

def tomar(nombre):
    print(f"🍺 {nombre} está tomando cerveza...")
    time.sleep(random.uniform(0.5, 1.5))
    print(f"🍺 {nombre} terminó de tomar")

def usar_baño(nombre):
    global baño_disponible
    if baño_disponible:
        baño_disponible = False
        print(f"🚽 {nombre} entró al baño...")
        time.sleep(random.uniform(1, 2))
        print(f"🚽 {nombre} salió del baño.")
        baño_disponible = True
        return True
    return False

def llamar_ex(nombre):
    global telefono_disponible
    if telefono_disponible:
        telefono_disponible = False
        print(f"📞 {nombre} está llamando a su ex... (¡peligro!)")
        time.sleep(random.uniform(1.5, 2.5))
        print(f"📞 {nombre} terminó la llamada (con lágrimas o risas)")
        telefono_disponible = True
        return True
    return False

def cantar(nombre):
    print(f"🎤 {nombre} está cantando desafinadamente...")
    time.sleep(random.uniform(0.8, 1.2))
    print(f"🎤 {nombre} terminó su 'interpretación'")

def asignar_acciones(borrachos):
    # Lista de todas acciones posibles
    acciones_disponibles = ['tomar', 'usar_baño', 'llamar_ex', 'cantar']
    
    # Primero asignamos acciones exclusivas
    for accion in ['usar_baño', 'llamar_ex']:
        # Elegir un borracho al azar que no tenga acción asignada
        candidatos = [b for b in borrachos if 'accion' not in b]
        if candidatos:
            borracho = random.choice(candidatos)
            if accion == 'usar_baño' and baño_disponible:
                borracho['accion'] = 'usar_baño'
            elif accion == 'llamar_ex' and telefono_disponible:
                borracho['accion'] = 'llamar_ex'
    
    # Asignar el resto de acciones
    acciones_restantes = ['tomar', 'cantar'] * 3  # Dar más peso a estas
    random.shuffle(acciones_restantes)
    
    for borracho in borrachos:
        if 'accion' not in borracho:
            # Buscar una acción que no haya hecho en su último turno
            posibles = [a for a in acciones_restantes if a != borracho.get('ultima_accion')]
            if not posibles:
                posibles = acciones_restantes
            
            borracho['accion'] = random.choice(posibles)
            acciones_restantes.remove(borracho['accion'])

def ejecutar_acciones(borrachos):
    # Ejecutar acciones en orden aleatorio para mayor realismo
    orden_ejecucion = random.sample(borrachos, len(borrachos))
    
    for borracho in orden_ejecucion:
        accion = borracho['accion']
        nombre = borracho['nombre']
        
        if accion == 'tomar':
            tomar(nombre)
        elif accion == 'usar_baño':
            if not usar_baño(nombre):  # Si el baño está ocupado
                # Reasignar acción alternativa
                alternativas = ['tomar', 'cantar']
                if borracho.get('ultima_accion') in alternativas:
                    alternativas.remove(borracho.get('ultima_accion'))
                if not alternativas:
                    alternativas = ['tomar', 'cantar']
                accion = random.choice(alternativas)
                borracho['accion'] = accion
                if accion == 'tomar':
                    tomar(nombre)
                else:
                    cantar(nombre)
        elif accion == 'llamar_ex':
            if not llamar_ex(nombre):  # Si el teléfono está ocupado
                # Reasignar acción alternativa
                alternativas = ['tomar', 'cantar']
                if borracho.get('ultima_accion') in alternativas:
                    alternativas.remove(borracho.get('ultima_accion'))
                if not alternativas:
                    alternativas = ['tomar', 'cantar']
                accion = random.choice(alternativas)
                borracho['accion'] = accion
                if accion == 'tomar':
                    tomar(nombre)
                else:
                    cantar(nombre)
        elif accion == 'cantar':
            cantar(nombre)
        
        borracho['ultima_accion'] = accion
        del borracho['accion']

# Lista de borrachos
borrachos = [
    {"nombre": "Elvis", "ultima_accion": None},
    {"nombre": "Hugo", "ultima_accion": None},
    {"nombre": "Alain", "ultima_accion": None},
    {"nombre": "Chelmi", "ultima_accion": None},
    {"nombre": "Jesus", "ultima_accion": None}
]

# Simulación
ciclo = 1
while True:
    print(f"\n=== CICLO {ciclo} ===")
    print("Estado: Baño {'disponible' if baño_disponible else 'ocupado'}, Teléfono {'disponible' if telefono_disponible else 'ocupado'}")
    
    # Asignar acciones para este ciclo
    asignar_acciones(borrachos)
    
    # Mostrar asignación planeada
    print("Asignación de acciones:")
    for b in borrachos:
        print(f" - {b['nombre']}: {b['accion']}")
    
    # Ejecutar acciones
    ejecutar_acciones(borrachos)
    
    ciclo += 1
    time.sleep(2)  # Pausa más larga entre ciclos para mejor lectura