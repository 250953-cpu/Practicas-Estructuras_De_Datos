import datetime
def saludar():
    print("Hola, Bienvenidos")
saludar()

def mostrarHora():

    horaActual = datetime.datetime.now().strftime("%H", "%M", "%S")
    
    print(f"La hora actual es: {horaActual}")
    mostrarHora()

    # NOW() Consulta el reloj o la hora del SO
    # strftime Convertir la fecha y la hora en texto, usando el formato establecido
    # f-string La letra "f" indica a python que procese el texto
    # e Inserte las variables dentro de las llaves
    # {horaActual} se toma el valor almacenado en la varible de horaActual
    # Y lo reemplaza ahi mismo