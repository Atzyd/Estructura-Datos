class Pila:
    def _init_(self):
        self.lista = []  # Crear una lista vacía

    def apilar(self, elemento):
        self.lista.append(elemento)  # Agregar elemento a la pila

    def desapilar(self):
        if len(self.lista) == 0:  # Verificar si la pila está vacía
            print("No se puede desapilar, la pila está vacía.")
            return None
        return self.lista.pop()  # Quitar y devolver el último elemento

    def ver_tope(self):
        if len(self.lista) == 0:
            print("La pila está vacía.")
            return None
        return self.lista[-1]  # Mostrar el último elemento sin quitarlo

    def esta_vacia(self):
        return len(self.lista) == 0  # Retorna True si está vacía, False si no

    def tamaño(self):
        return len(self.lista)  # Retorna la cantidad de elementos

pila = Pila()

print("Apilando 1, 2 y 3...")
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)

print("Tope actual:", pila.ver_tope())  # 3
print("Desapilando:", pila.desapilar())  # 3
print("Nuevo tope:", pila.ver_tope())  # 2
print("Tamaño de la pila:", pila.tamaño())  # 2

print("Vaciando la pila...")
pila.desapilar()
pila.desapilar()
print("¿Está vacía?", pila.esta_vacia())  