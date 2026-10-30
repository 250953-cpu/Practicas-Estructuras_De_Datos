import numpy as np

# MATRIZ A Y B
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# SUMA ELEMENTOS
suma = A + B
print("---SUMA (A+B)---")
print(suma)

# MULTIPLICACIÓN DE ELEMENTOS
prod_elem = A * B
print("\n---MULTIPLICACIÓN (A*B)---")  
print(prod_elem)

# PRODUCTO MATRICIAL
prod_mat = A @ B
print("\n---PRODUCTO MATRICIAL (A@B)---") 
print(prod_mat)

# TRANSPUESTA 
transpuesta = A.T
print("\n---TRANSPUESTA DE A (A.T)---")  
print(transpuesta)

# DETERMINANTE E INVERSA
det = np.linalg.det(A)
inv = np.linalg.inv(B)

print("\n---DETERMINANTE DE A---") 
print(det)

print("\n---INVERSA DE B---")  
 