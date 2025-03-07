import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_circunferencia(self):
        return 2 * math.pi * self.radio

    def establecer_radio(self, radio):
        self.radio = radio

    def obtener_radio(self):
        return self.radio

if __name__ == "__main__":
    circulo1 = Circulo(5)

    area = circulo1.calcular_area()
    circunferencia = circulo1.calcular_circunferencia()

    print(f"Área del círculo: {area:.2f}")
    print(f"Circunferencia del círculo: {circunferencia:.2f}")

    # Cambiar el radio
    circulo1.establecer_radio(10)

    area_actualizado = circulo1.calcular_area()
    circunferencia_actualizada = circulo1.calcular_circunferencia()

    print(f"Área del círculo actualizado: {area_actualizado:.2f}")
    print(f"Circunferencia del círculo actualizado: {circunferencia_actualizada:.2f}")
