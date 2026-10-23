#PYTHON NATIVA

#Creación de la matriz 3X3 
matriz=[
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
#ACCESO A LOS ELEMENTOS DE LA MATRIZ (FILA)(COLUMNA)
print(matriz[1][2])#IMPRIMIRA LA FILA INDICE 1, COLUMNA INDICE 2

#MODIICAR UN ELEMENTO

matriz [0][0]=100

#RECORRER LA MATRIZ
for fila in matriz:
    for elemento in fila:
        print(elemento, end = " ")
    print()