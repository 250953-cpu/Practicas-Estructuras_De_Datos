import numpy as np

print("---ENFOQUE PYTHON NATIVO---")

# 1. Creación de las matrices de ventas del Sábado (A) y Domingo (B)
matriz_A_nativa = [[10, 15], [20, 5]]
matriz_B_nativa = [[5, 12], [15, 8]]

# Calcular el total 
total_unidades_nativa = []
for i in range(len(matriz_A_nativa)):
    fila = []
    for j in range(len(matriz_A_nativa[i])):
        fila.append(matriz_A_nativa[i][j] + matriz_B_nativa[i][j])
    total_unidades_nativa.append(fila)

# Calcular el ingreso total 
ingreso_total_nativa = []
for i in range(len(total_unidades_nativa)):
    fila = []
    for j in range(len(total_unidades_nativa[i])):
        fila.append(total_unidades_nativa[i][j] * 50)
    ingreso_total_nativa.append(fila)

# Imprimir recorrido de las matrices 
print("Total de productos vendidos (Sábado + Domingo):")
for fila in total_unidades_nativa:
    for elemento in fila:
        print(elemento, end=" ")
    print()

print("\nIngreso total en pesos (a 50 pesos por producto):")
for fila in ingreso_total_nativa:
    for elemento in fila:
        print(elemento, end=" ")
    print()

print("\n" + "="*40 + "\n")


# NUMPY
print("--- ENFOQUE CON NUMPY ---")

A = np.array([[10, 15], [20, 5]])
B = np.array([[5, 12], [15, 8]])

#  Calcular el total de productos vendidos (Suma matricial directa)
total_unidades_numpy = A + B

# Calcular el ingreso total (Multiplicación escalar directa)
ingreso_total_numpy = total_unidades_numpy * 50

# Imprimir
print("Total de productos vendidos (Sábado + Domingo):")
print(total_unidades_numpy)

print("\nIngreso total en pesos (a 50 pesos por producto):")
print(ingreso_total_numpy)
