class Vehiculo:
    def __init__(self, marca, combustible):
        self.marca = marca
        self.combustible = combustible
        self.tipo = None  
    
    def __str__(self):
        return f"Marca: {self.marca}, Combustible: {self.combustible:.2f}, Tipo: {self.tipo}"

    def encender(self):
        if self.combustible < 10:
            print("Advertencia: Necesitas ir a la gasolinera. Nivel de combustible bajo.")
        else:
            print(f"El vehículo {self.marca} está encendido.")

    def arrancar(self):
        if self.combustible <= 0:
            print("El vehículo no puede arrancar, no hay combustible.")
        else:
            print(f"El vehículo {self.marca} ha arrancado.")

    def marcha(self, km):
        consumo_por_km = 0.1  
        consumo_total = km * consumo_por_km
        self.combustible -= consumo_total
        
        if self.combustible < 0:
            self.combustible = 0
        
        print(f"El vehículo {self.marca} ha recorrido {km} km. Combustible restante: {self.combustible:.2f} galones.")
        
        if self.combustible < 10 and self.combustible > 0:
            print("Advertencia: Nivel de combustible bajo. Necesitas ir a la gasolinera.")

        if self.combustible == 0:
            print(f"El vehículo {self.marca} se ha detenido debido a que el combustible se agotó.")

class Moto(Vehiculo):
    def __init__(self, marca, combustible):
        super().__init__(marca, combustible)
        self.tipo = "Moto"  

class Carro(Vehiculo):
    def __init__(self, marca, combustible):
        super().__init__(marca, combustible)
        self.tipo = "Carro"  

moto = Moto("Yamaha", 9)
carro = Carro("Toyota", 11)

print(moto)
print(carro)

moto.encender()
carro.encender()
moto.arrancar()
carro.arrancar()

moto.marcha(50)  
carro.marcha(100)  