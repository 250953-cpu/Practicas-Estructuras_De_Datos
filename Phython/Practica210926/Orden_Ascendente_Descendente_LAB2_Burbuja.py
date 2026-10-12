# practica2_burbuja.py

# 2. Declaración de la lista con 15 calificaciones de ejemplo
# (Sustituye estos números por los valores reales de tu grupo)
calificaciones = [85, 92, 74, 60, 95, 88, 71, 90, 65, 81, 78, 89, 100, 67, 83]

# ==========================================
# Parte 1 (Orden Ascendente)
# ==========================================
lista_asc = calificaciones.copy()  # Copia para no alterar la original
n = len(lista_asc)

for i in range(n):
    swapped = False
    # El bucle interno reduce su rango en cada pasada porque los elementos finales ya están ordenados
    for j in range(0, n - i - 1):
        # Operador '>' para ordenar de menor a mayor
        if lista_asc[j] > lista_asc[j + 1]:
            lista_asc[j], lista_asc[j + 1] = lista_asc[j + 1], lista_asc[j]
            swapped = True
    # Si no hubo intercambios en toda la pasada, la lista ya está ordenada
    if not swapped:
        break

print("Orden Ascendente:", lista_asc)

# ==========================================
# Parte 2 (Orden Descendente)
# ==========================================
lista_desc = calificaciones.copy()
n = len(lista_desc)

for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        # Operador '<' para ordenar de mayor a menor
        if lista_desc[j] < lista_desc[j + 1]:
            lista_desc[j], lista_desc[j + 1] = lista_desc[j + 1], lista_desc[j]
            swapped = True
    if not swapped:
        break

print("Orden descendente:", lista_desc: desc)
