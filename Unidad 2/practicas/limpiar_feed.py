def limpiar_feed(publicaciones: list) -> list:
    if len(publicaciones) <= 1:
        return publicaciones
    
    if publicaciones[0] == publicaciones[1]:
        return limpiar_feed(publicaciones[1:])
    else:
        return [publicaciones[0]] + limpiar_feed(publicaciones[1:])

feed = ["Post A", "Post B", "Post B", "Post C", "Post B"]
print(limpiar_feed(feed))

#EJERCICIO 2:  

def calcular_saldo_final(depositos: list, tasa_interes: float) -> float:
    if len(depositos) == 0:
        return 0.0
    
    saldo_anterior = calcular_saldo_final(depositos[:-1], tasa_interes)
    deposito_actual = depositos[-1]
    
    return (saldo_anterior + deposito_actual) * (1 + tasa_interes)

mis_depositos = [1000, 2000, 1500]
print(calcular_saldo_final(mis_depositos, 0.05))  # Salida: 4937.625

#EJERCICIO 3: 

def maxima_profundidad(comentarios: list) -> int:
    if len(comentarios) == 0:
        return 0
    
    max_prof = 0 
    
    for elem in comentarios:
        if isinstance(elem, list):
            profundidad_actual = 1 + maxima_profundidad(elem)
        else:
            profundidad_actual = 1
            
        if profundidad_actual > max_prof:
            max_prof = profundidad_actual
            
    return max_prof

hilo = ["Comentario 1", ["Respuesta 1.1", ["Respuesta 1.1.1"]], "Comentario 2"]
print(maxima_profundidad(hilo))  # Salida: 3
