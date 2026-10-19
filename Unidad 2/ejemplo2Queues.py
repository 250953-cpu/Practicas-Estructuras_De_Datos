from collections import deque
import time

cola_reproduccion=deque()

#El usuario agrega canciones 

cola_reproduccion.append("1.Antologia")
cola_reproduccion.append("2.Historia de amor")
cola_reproduccion.append("3.Historia entre tus dedos")

#Mostrar las canciones en espera

print("Canciones en espera:")
for cancion in cola_reproduccion:
    print("_", cancion)
    print("Iniciando reproduccion....")
#El reproductor procesa la cola cancion por cancion(DESENCOLAR)

cancion_actual=cola_reproduccion.popleft()
print(f"Sonando ahora: {cancion_actual}")
time.sleep(1)#SIMULA LA DURACION DEL TEMA
print(f"Finalizo: {cancion_actual}")

#Muestra cuantas canciones quedan en la cola

print(f"Quedan: {len (cola_reproduccion)}) Canciones en la cola)")
print("La cola de reproduccion ha terminado")
