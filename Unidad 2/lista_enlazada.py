class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None # REFERENCIA INICIAL QUE VA A INDICAR EL ORIGEN DE LA LISTA

    def insertar_final(self, dato):
        nuevo_nodo = Nodo(dato)

        # CASO 1: SI LA LISTA ESTA VACIA (Ahora está dentro de insertar_final)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        
        # CASO 2: RECORRER HASTA EL ULTIMO NODO QUE EXISTE
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
            
        # CONECTAR EL ULTIMO NODO CON EL NUEVO NODO (Fuera del while, dentro del método)
        actual.siguiente = nuevo_nodo

    def mostrar_lista(self):
        actual = self.cabeza
        elementos = []
   
        # Se alineó el while y se corrigieron sus niveles internos
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
            
        # El print debe ir al terminar el ciclo while para mostrar toda la lista junta
        print(" -> ".join(elementos) + " -> None")

# USO DEL PROGRAMA
lista = ListaEnlazada()

# INSERTAR ELEMENTOS A UTILIZAR
lista.insertar_final("A")
lista.insertar_final("B")
lista.insertar_final("C")

lista.mostrar_lista()
