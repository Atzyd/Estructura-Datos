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
 #Clase cancion 
 ##  def __init__(self, titulo, artista, album, duracion):
   ####  self.duracion = duracion  

   # def obtener_titulo(self):
   #     return self.titulo

   # def establecer_titulo(self, titulo):
   #     self.titulo = titulo

    #def obtener_artista(self):
   #     return self.artista

   # def establecer_artista(self, artista):
  #      self.artista = artista

   # def obtener_album(self):
   #     return self.album

   # def establecer_album(self, album):
   #     self.album = album

  #  def obtener_duracion(self):
  #      return self.duracion

   # def establecer_duracion(self, duracion):
    #    self.duracion = duracion

    #def reproducir(self):
     #   print(f"Reproduciendo '{self.titulo}' de {self.artista} del álbum '{self.album}'. Duración: {self.duracion}.")


#if __name__ == "__main__":
 #   cancion1 = Cancion("Bohemian Rhapsody", "Queen", "A Night at the Opera", "5:55")

  #  cancion1.reproducir()

   # cancion1.establecer_titulo("Bohemian Rhapsody - Remastered")
    #cancion1.establecer_duracion("6:00")

    #print("\nDetalles actualizados de la canción:")
    #cancion1.reproducir()