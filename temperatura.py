temperatura = []

for n in range (0, 5):
    t=int(input("Ingrese la temperatura"))
    temperatura.append(t)
promedio = sum (temperatura)/ len(temperatura)

if promedio < 20:
    print("Se necesita mantenimiento")
elif 20<= promedio <=30:
    print("La temperatura es optima")
else:
    print("Se necesita un arreglo,la temperatura es Alta")
