class Animal:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo
    
    def __str__(self):
        return f"{self.nombre} ({self.tipo}), {self.edad} años"

class Nodo:
    def __init__(self, animal):
        self.animal = animal
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def agregar_animal(self, animal):
        if self.buscar_animal(animal.nombre, animal.tipo):
            print("Error: El animal ya está registrado.")
            return
        nuevo_nodo = Nodo(animal)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
    
    def buscar_animal(self, nombre, tipo):
        actual = self.cabeza
        while actual:
            if actual.animal.nombre == nombre and actual.animal.tipo == tipo:
                return True
            actual = actual.siguiente
        return False
    
    def mostrar_animales_iterativo(self):
        actual = self.cabeza
        while actual:
            print(actual.animal)
            actual = actual.siguiente
    
    def mostrar_animales_recursivo(self, nodo=None):
        if nodo is None:
            nodo = self.cabeza
        if nodo is not None:
            print(nodo.animal)
            self.mostrar_animales_recursivo(nodo.siguiente)
zoologico = ListaEnlazada()
zoologico.agregar_animal(Animal("León", 5, "Felino"))
zoologico.agregar_animal(Animal("Tigre", 7, "Felino"))
zoologico.agregar_animal(Animal("Elefante", 4, "Mamífero"))
print("Animales (Iterativo):")
zoologico.mostrar_animales_iterativo()

print("\nAnimales (Recursivo):")
zoologico.mostrar_animales_recursivo()