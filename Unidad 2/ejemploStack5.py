historial_navegacion=[]
#Operación para apilar
historial_navegacion.append("google.com""")
historial_navegacion.append("youtube.com")
historial_navegacion.append("wikipedia.org")
print("\nhistorial cargado", historial_navegacion) 

#Operacion cima (TOP-PEEK)

pagina_actual=historial_navegacion[-1]
print("\nPagina actual en pantalla:", pagina_actual)

#Operacion para desapilar(POP)

pagina_cerrada=historial_navegacion.pop()
print("\nSaliendo de:", pagina_cerrada)
print("\nHistorial después de presionar 'Atras'", historial_navegacion)
#Operacion tamaño 
total_paginas=len(historial_navegacion)
print("\nPaginas guardadas", total_paginas)

#Operacion vacia(Empety)

sin_paginas=len(historial_navegacion)==0
print("\n¿El historial esta vacio?", sin_paginas)
