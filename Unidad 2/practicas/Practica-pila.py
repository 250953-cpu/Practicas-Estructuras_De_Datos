pila_platos = []   #Creacion del constructor
print("Pila de platos inicializada")
print(pila_platos)

# Paso 2
print("\nApilando 10 platos")
for i in range(1, 11):
    pila_platos.append(f"Plato {i}")
print("Pila actual:", pila_platos)

# Paso 3
cima = pila_platos[-1]
print("\nConsultar la Cima ")
print("El plato que está arriba del todo es:", cima)

# Paso 4
print("\n Paso 4: Desapilando 4 elementos ")
for _ in range(4):
    plato_retirado = pila_platos.pop()
    print(f"Se retiró de la cima: {plato_retirado}")
print("Pila después de retirar 4 platos:", pila_platos)

# Paso 5
tamanio = len(pila_platos)
pila_vacia = len(pila_platos) == 0
print(f"Cantidad de platos restantes en la pila: {tamanio}")
print(f"¿La pila está vacía?: {pila_vacia}")

# Paso 6
print("\nVaciando la pila por completo ")
while len(pila_platos) > 0:
    plato_eliminado = pila_platos.pop()
    print(f"Vaciando... Se quitó: {plato_eliminado}")

# Resultado final
print(f"\n¿La pila quedó completamente vacía?: {len(pila_platos) == 0}")
