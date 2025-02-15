numeros = []

def agregar (numero : int ) ->None :

    numeros.append(numero)
    
def eliminar (numero : int) ->None :

        numeros.pop(numero)

while True:
      
    seleccion = int (input('''Seleccione una opcion
                              1. Agregar numero
                              2. Eliminar numero
                              3. Ver lista de numeros
                           
                           '''))
    if seleccion == 1:
         numero = int(input("Agregue un numero a la lista:"))
         agregar(numero)
    elif seleccion == 2:
         numero = int(input("Elimine un numero"))
         eliminar(numero)
    elif seleccion==3:
         print("Numeros en la lista")
         print(numeros)
    elif seleccion == 0:
        break

print(numeros)
