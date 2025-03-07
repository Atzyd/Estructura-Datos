class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

    def establecer_base(self, base):
        self.base = base

    def establecer_altura(self, altura):
        self.altura = altura

    def obtener_base(self):
        return self.base

    def obtener_altura(self):
        return self.altura

if __name__ == "__main__":
    rectangulo1 = Rectangulo(5, 3)

    area = rectangulo1.calcular_area()
    perimetro = rectangulo1.calcular_perimetro()

    print(f"Área del rectángulo: {area}")
    print(f"Perímetro del rectángulo: {perimetro}")

    rectangulo1.establecer_base(10)
    rectangulo1.establecer_altura(4)

    area_actualizado = rectangulo1.calcular_area()
    perimetro_actualizado = rectangulo1.calcular_perimetro()

    print(f"Área del rectángulo actualizado: {area_actualizado}")
    print(f"Perímetro del rectángulo actualizado: {perimetro_actualizado}")