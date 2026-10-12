# PRÁCTICA DE LABORATORIO: REGISTRO Y EVALUACIÓN DE CALIFICACIONES

# 1. Función sin parámetros y sin retorno
def mostrar_encabezado_escuela():
    print("=========================================")
    print("               UTXJ                      ")
    print("      INSTITUTO X - REPORTE ACADÉMICO    ")
    print("=========================================")

# 2. Función sin parámetros que retorna un valor fijo
def obtener_nota_minima_aprobatoria():
    return 6.0

# 3. Función con 1 parámetro que retorna una categoría de texto
def evaluar_rendimiento(nota_final):
    if nota_final < 7.0:
        return "Reprobado"
    elif 7.0 <= nota_final <= 9.4:
        return "Aprobado"
    elif 9.5 <= nota_final <= 10.0:
        return "Excelente"
    return "Nota fuera de rango"

# 4. Función con 2 parámetros que retorna la calificación ponderada
def calcular_promedio_ponderado(nota_examenes, nota_tareas):
    # Exámenes valen 70% (0.7) y Tareas valen 30% (0.3)
    final = (nota_examenes * 0.7) + (nota_tareas * 0.3)
    return round(final, 1)

# 5. Función con 3 parámetros que integra a las anteriores
def generar_boleta(nombre_alumno, nota_examenes, nota_tareas):
    # Integración de funciones auxiliares
    nota_final = calcular_promedio_ponderado(nota_examenes, nota_tareas)
    nota_minima = obtener_nota_minima_aprobatoria()
    estado = evaluar_rendimiento(nota_final)
    
    # Determinar si necesita examen extraordinario
    necesita_extraordinario = "SÍ" if nota_final < nota_minima else "NO"
    
    # Imprimir desglose en pantalla
    print(f"\n--- BOLETA DE CALIFICACIONES ---")
    print(f"Alumno: {nombre_alumno}")
    print(f"Calificación Final Ponderada: {nota_final}")
    print(f"Estado Académico: {estado}")
    print(f"¿Necesita Examen Extraordinario?: {necesita_extraordinario}")
    print("---------------------------------")


# =====================================================================
# EJEMPLO DE USO / PRUEBA DEL PROGRAMA
# =====================================================================
if __name__ == "__main__":
    # Mostrar el encabezado de la escuela
    mostrar_encabezado_escuela()
    
    # Prueba 1: Alumno Excelente
    generar_boleta("Sofía López", 9.8, 9.5)
    
    # Prueba 2: Alumno Aprobado pero cerca del límite
    generar_boleta("Carlos Pérez", 6.5, 7.0)
    
    # Prueba 3: Alumno Reprobado y que requiere extraordinario (menor a 6.0)
    generar_boleta("Luis Gómez", 5.0, 5.5)
