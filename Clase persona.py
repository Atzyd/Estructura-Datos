class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_edad(self):
        return self.edad

    def establecer_edad(self, edad):
        self.edad = edad

    def obtener_genero(self):
        return self.genero

    def establecer_genero(self, genero):
        self.genero = genero

    def presentarse(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y soy {self.genero}."

# Ejemplo de uso
if __name__ == "__main__":
    persona1 = Persona("Juan", 30, "masculino")
    print(persona1.presentarse())

    persona1.establecer_edad(31)
    print(f"Ahora tengo {persona1.obtener_edad()} años.")