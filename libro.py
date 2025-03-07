class Libro:
    def __init__(self, titulo, autor, genero, anio_de_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.anio_de_publicacion = anio_de_publicacion

    def obtener_titulo(self):
        return self.titulo

    def establecer_titulo(self, titulo):
        self.titulo = titulo

    def obtener_autor(self):
        return self.autor

    def establecer_autor(self, autor):
        self.autor = autor

    def obtener_genero(self):
        return self.genero

    def establecer_genero(self, genero):
        self.genero = genero

    def obtener_anio_de_publicacion(self):
        return self.anio_de_publicacion

    def establecer_anio_de_publicacion(self, anio):
        self.anio_de_publicacion = anio

    def mostrar_detalles(self):
        detalles = (
            f"Título: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"Género: {self.genero}\n"
            f"Año de Publicación: {self.anio_de_publicacion}"
        )
        print(detalles)

if __name__ == "__main__":
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", 1967)

    libro1.mostrar_detalles()

    libro1.establecer_titulo("Cien años de soledad - Edición Especial")
    libro1.establecer_anio_de_publicacion(2014)

    print("\nDetalles actualizados del libro:")
    libro1.mostrar_detalles()