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


class CuentaBancaria:
    def __init__(self, titular, saldo_inicial, numero_de_cuenta):
        self.titular = titular  # Debe ser un objeto de la clase Persona
        self.saldo = saldo_inicial
        self.numero_de_cuenta = numero_de_cuenta

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se han depositado {cantidad} unidades. Nuevo saldo: {self.saldo}.")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Error: No se puede retirar más de lo que hay en la cuenta.")
        elif cantidad <= 0:
            print("La cantidad a retirar debe ser mayor que cero.")
        else:
            self.saldo -= cantidad
            print(f"Se han retirado {cantidad} unidades. Nuevo saldo: {self.saldo}.")

    def consultar_saldo(self):
        return f"El saldo actual de la cuenta es: {self.saldo}."

    def presentar_titular(self):
        return self.titular.presentarse()

if __name__ == "__main__":
    persona1 = Persona("Juan", 30, "masculino")
    cuenta1 = CuentaBancaria(persona1, 1000, "123456789")

    print(cuenta1.presentar_titular())
    print(cuenta1.consultar_saldo())

    cuenta1.depositar(500)
    cuenta1.retirar(200)
    print(cuenta1.consultar_saldo())

    cuenta1.retirar(500)  