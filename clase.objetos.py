class Vehiculo:
    color: str
    modelo: int
    cilindraje: int
    numero_ruedas: int
    combustible: int
    marca: str

    def __init__(self, marca: str, modelo: int, combustible: int) -> None:
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible

    def __str__(self):
        return f"La marca del vehiculo es {self.marca} y el nivel de combustible es de {self.combustible}"

    def encender(self):
        pass

    def acelerar(self):
        pass

    def frenar(self):
        pass

    def apagar(self):
        pass

class Moto(Vehiculo):
    pass
class Carro(Vehiculo):
    pass

vehiculo1 = Vehiculo('Mazda', 2023, 80)

print(vehiculo1)

moto1 = Moto ('Honda', 50)

print (moto1)

carro1 = Carro ("Renault", 80)
print = (carro1)