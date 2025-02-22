#Terea 1
#def fibonacci(n, a=0, b=1):
 #   if n <= 0:
  #      return []
   # elif n == 1:
    #    return [a]
    #else:
    #    return [a] + fibonacci(n - 1, b, a + b)
#if __name__ == "__main__":
 #   n = 10
  #  print(fibonacci(n))

#Actividad 2 Sumaaaaaa
#def sumar_lista(arr, n):
   # if n == 0:
    #    return 0
   # return arr[n - 1] + sumar_lista(arr, n - 1)

#numeros = [10, 2, 10, 2, 34, 9]  
#resultado = sumar_lista(numeros, len(numeros))
#print(f"Suma de la lista: {resultado}")

# Actividad de Multiplicacion
#def multiplicacion(a, b):
  #  if b == 0:
   #     return 0
   # elif b == 1:
   #     return a
   # else:
   #     return a + multiplicacion(a, b - 1)
#if __name__ == "__main__":
 #   print(multiplicacion(9, 2))  
  #  print(multiplicacion(3, 8)) 


# Actividad de Divisiones 

#def division(a, b):
  #  if b == 0:
   #     return "Error matematico (0) "  
   # if a < b:
  #      return 0 
  #  return 1 + division(a - b, b)  

#dividendo = 7
#divisor = 7
#resultado = division(dividendo, divisor)
#print(f"{dividendo} dividido entre {divisor} es {resultado}")