def move(origen, destino):
    print(f"Mover de {origen} a {destino}")


def hanoi(n, a, b, c):
    if n == 1:
        move(a, c)
        return
    hanoi(n - 1, a, c, b)
    move(a, c)
    hanoi(n - 1, b, a, c)  


hanoi(3, "Torre A", "Torre B", "Torre C")
