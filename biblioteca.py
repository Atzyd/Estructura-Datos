persona = dict()

def agregar_valor(clave: str, valor: str):
    persona.update({clave: valor})

def eliminar_persona(clave: str):
    if clave in persona:
        persona.pop(clave)
        print(f'{clave} ha sido eliminado correctamente.')
    else:
        print(f'{clave} no se encuentra en la lista.')

while True:
    seleccion = int(input('''Seleccione una opción:
                              1. Agregar nombre
                              2. Eliminar nombre
                              3. Ver lista de nombres
                              4. Salir
                            '''))

    if seleccion == 1:
        nombre = input('Ingrese el nombre a agregar: ')
        clave= input("Agregue codigo: ")
        print(f'{nombre} ha sido agregado correctamente.')
    elif seleccion == 2:
        nombre = input('Ingrese el codigo a eliminar: ')
        eliminar_persona(clave)
    elif seleccion == 3:
        print('Lista de nombres:')
        print(clave)
    elif seleccion == 4:
        print('Saliendo...')
        break
    else:
        print('Opción no válida, por favor intente de nuevo.')


