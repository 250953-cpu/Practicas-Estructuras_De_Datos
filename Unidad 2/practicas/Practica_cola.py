from collections import deque
import time

cola_turnos=deque()

#Se agrega turnos a la cola (ENCOLAR) 

cola_turnos.append("Turno A01 - ISIDRO ORTIZ RAMIREZ")
cola_turnos.append("Turno A02 - GUADALUPE PEREZ DIAZ")
cola_turnos.append("Turno A03 - JUANA LAZCANO RODRIGUEZ")

#Mostrar los turnos en espera

print("Turnos emitidos en la fila del banco:")
for clientes in cola_turnos:
    print(f" - {clientes}")

print("\nIniciando atención en ventanilla\n")

# El while se repite hasta que se remueva todos los clientes(DESENCOLAR usando un ciclo while)
while cola_turnos:
    # Remueve al primer cliente en llegar
    cliente_actual = cola_turnos.popleft()
    
    print(f"Llamando a ventanilla: {cliente_actual}")
    
    # Tiempo de atención simulado
    time.sleep(1) 
    
    print(f"Atención finalizada: {cliente_actual}")

    # Muestra la cantidad de clientes restantes
    print(f" (Clientes restantes en la fila: {len(cola_turnos)})\n")

print("Se han atendido todos los turnos. Fila vacía.")