texto = "texto"
entero = 12
decimal = 25.65
booleanos = True

cadena = (texto) + "/" + str(entero) + "/" + str(decimal) + "/" + str(booleanos)


# Los enteros en Python están limitados a 32 bits, lo que significa que pueden almacenar valores de hasta 2^31 - 1.
# Los flotantes en Python están limitados a 64 bits, lo que significa que pueden almacenar valores de hasta 2^63 - 1.

n = 10
sumaP = 0
for i in range(1, n + 1, 2):
  sumaP+= i
  
print(cadena)
print("El límite de los enteros en Python es 2^31 - 1.")
print("El límite de los flotantes en Python es 2^63 - 1.")
print("La suma de los primeros 10 números pares es", sumaP)