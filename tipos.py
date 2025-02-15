numeros = []

def agregar(numero: int) -> None:
    numeros.append(numero)

def eliminar(numero: int) -> None:
    if numero in numeros:
        numeros.remove(numero)  
    else:
        print("El número no está en la lista")

while True:
    seleccion = int(input('''Seleccione una opción
                              1. Agregar número
                              2. Eliminar número
                              3. Ver lista de números
                            '''))
    if seleccion == 1:
        numero = int(input("Agregue un número a la lista:"))
        agregar(numero)
    elif seleccion == 2:
        numero = int(input("Elimine un número:"))
        eliminar(numero)
    elif seleccion == 3:
        print("Números en la lista")
        print(numeros)
    elif seleccion == 0:
        break

print(numeros)
