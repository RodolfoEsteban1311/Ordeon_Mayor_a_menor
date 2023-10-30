cantidad = int(input("Ingrese la cantidad de números que desea agregar: "))

numeros = []
for i in range(cantidad):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

numeros.sort(reverse=True)

print("El orden de los números de Mayor a Menor es:")
for numero in numeros:
    print(numero)