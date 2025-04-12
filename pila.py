class Pila:
    def _init_(self):
        self.lista = []  
    def apilar(self, elemento):
        self.lista.append(elemento) 

    def desapilar(self):
        if len(self.lista) == 0:  
            print("No se puede desapilar, la pila está vacía.")
            return None
        return self.lista.pop()  

    def ver_tope(self):
        if len(self.lista) == 0:
            print("La pila está vacía.")
            return None
        return self.lista[-1]  

    def esta_vacia(self):
        return len(self.lista) == 0  

    def tamaño(self):
        return len(self.lista)  

pila = Pila()

print("Apilando 1, 2 y 3...")
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)

print("Tope actual:", pila.ver_tope())  
print("Desapilando:", pila.desapilar()) 
print("Nuevo tope:", pila.ver_tope())  
print("Tamaño de la pila:", pila.tamaño())  

print("Vaciando la pila...")
pila.desapilar()
pila.desapilar()
print("¿Está vacía?", pila.esta_vacia())  
