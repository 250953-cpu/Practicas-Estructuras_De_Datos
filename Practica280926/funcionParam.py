def calcularAreaTriangulo(base, altura):
    area = (base*altura)/2
    return area
    
    resultado = calcularAreaTriangulo(10, 5)
    print(f"El area del triangulo es: {resultado}")
    
def saludarPersona(nombre, edad):
     print(f"Hola {nombre}, tienes {edad} años.")
saludarPersona("Elena", 28)