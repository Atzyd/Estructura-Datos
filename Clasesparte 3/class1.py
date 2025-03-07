#class Empleado:
   # def __init__(self, nombre, salario, departamento):
  #      self.nombre = nombre
  #      self.salario = salario
   #     self.departamento = departamento

  #  def trabajar(self):
  #      return f"{self.nombre} está trabajando en el departamento de {self.departamento}."


#class Gerente(Empleado):
   # def __init__(self, nombre, salario, departamento, equipo=None):
  #      super().__init__(nombre, salario, departamento)
  #      if equipo is None:
    #        equipo = []
    #    self.equipo = equipo

   # def supervisar_a_equipo(self):
   #     return f"{self.nombre} está supervisando a su equipo: {', '.join([empleado.nombre for empleado in self.equipo])}."

   # def trabajar(self):
  #      return f"{self.nombre} está gestionando el departamento de {self.departamento}."

#class Desarrollador(Empleado):
  #  def __init__(self, nombre, salario, departamento, lenguaje_de_programacion):
  #      super().__init__(nombre, salario, departamento)
   #     self.lenguaje_de_programacion = lenguaje_de_programacion

  #  def escribir_codigo(self):
  #      return f"{self.nombre} está escribiendo código en {self.lenguaje_de_programacion}."

  #  def trabajar(self):
 #       return f"{self.nombre} está desarrollando software en el departamento de {self.departamento}."

#if __name__ == "__main__":
    
 #   empleado1 = Desarrollador("Arturo", 60000, "Desarrollo", "Python")
  #  empleado2 = Desarrollador("Rachel", 65000, "Desarrollo", "Java")
   # gerente = Gerente("Diegiño", 80000, "Desarrollo", [empleado1, empleado2])

  #  print(empleado1.trabajar())
  #  print(empleado1.escribir_codigo())
    
   # print(empleado2.trabajar())
   # print(empleado2.escribir_codigo())
    
  #  print(gerente.trabajar())
   # print(gerente.supervisar_a_equipo())

#class FiguraGeométrica:
 #   def calcular_area(self):
 #       raise NotImplementedError("Este método debe ser implementado por las clases derivadas.")


#class Triángulo(FiguraGeométrica):
  #  def __init__(self, base, altura):
   #     self.base = base
   #     self.altura = altura

 #   def calcular_area(self):
 #       return (self.base * self.altura) / 2


#class Cuadrado(FiguraGeométrica):
 #   def __init__(self, lado):
 #       self.lado = lado

 #   def calcular_area(self):
  #      return self.lado ** 2


#if __name__ == "__main__":
 #   triángulo = Triángulo(5, 10)
 #   cuadrado = Cuadrado(4)

  #  print(f"Área del triángulo: {triángulo.calcular_area()} unidades cuadradas.")
  #  print(f"Área del cuadrado: {cuadrado.calcular_area()} unidades cuadradas.")

#class Electrodoméstico:
   # def __init__(self, marca, modelo, consumo_energético):
     #   self.marca = marca
    #    self.modelo = modelo
     #   self.consumo_energético = consumo_energético

    #def encender(self):
    #    return f"{self.marca} {self.modelo} está encendido."


#class Lavadora(Electrodoméstico):
   # def __init__(self, marca, modelo, consumo_energético, capacidad):
    #    super().__init__(marca, modelo, consumo_energético)
    #    self.capacidad = capacidad

   # def iniciar_ciclo_de_lavado(self):
    #    return f"La lavadora {self.marca} {self.modelo} está iniciando un ciclo de lavado."

   # def encender(self):
       # return super().encender() + " " + self.iniciar_ciclo_de_lavado()


#class Refrigerador(Electrodoméstico):
    #def __init__(self, marca, modelo, consumo_energético, tiene_congelador):
   #     super().__init__(marca, modelo, consumo_energético)
   #     self.tiene_congelador = tiene_congelador

   # def regular_temperatura(self):
   #     return f"El refrigerador {self.marca} {self.modelo} está regulando la temperatura."

  #  def encender(self):
    #    return super().encender() + " " + self.regular_temperatura()


#if __name__ == "__main__":
  #  lavadora = Lavadora("LG", "TWINWash", 0.8, 10)
   # refrigerador = Refrigerador("Samsung", "Family Hub", 1.5, True)

   # print(lavadora.encender())
   # print(refrigerador.encender())

#class Usuario:
    #def __init__(self, nombre_de_usuario, contraseña):
      #  self.nombre_de_usuario = nombre_de_usuario
      #  self.contraseña = contraseña

    #def iniciar_sesión(self, contraseña_introducida):
       # if contraseña_introducida == self.contraseña:
         #   return f"{self.nombre_de_usuario} ha iniciado sesión correctamente."
       # else:
         #   return "Contraseña incorrecta. No se pudo iniciar sesión."


#class Administrador(Usuario):
   # def gestionar_usuarios(self):
      #  return f"{self.nombre_de_usuario} está gestionando usuarios."


#class Cliente(Usuario):
   # def realizar_compra(self):
    #    return f"{self.nombre_de_usuario} está realizando una compra."


#if __name__ == "__main__":
  #  admin = Administrador("admin123", "adminpass")
   # cliente = Cliente("cliente456", "clientepass")

   # print(admin.iniciar_sesión("adminpass"))
   # print(admin.gestionar_usuarios())

  #  print(cliente.iniciar_sesión("clientepass"))
  #  print(cliente.realizar_compra())