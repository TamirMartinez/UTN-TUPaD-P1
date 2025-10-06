# TP N4 - Estructuras Repetitivas



# Ejercicio 1: Imprimir los numeros del 0 al 100 en orden creciente.
for i in range(101):
    print(i)


# Ejercicio 2: Determinar la cantidad de digitos de un numero ingresado por el usuario.
num = int(input("Ingrese un numero entero: "))
contador = 0
n = abs(num)
while n > 0:
    n //= 10
    contador += 1
if num == 0:
    contador = 1
print("El numero tiene", contador, "digitos.")


# Ejercicio 3: Sumar todos los numeros enteros comprendidos entre dos valores dados.
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
suma = 0
for i in range(min(a, b) + 1, max(a, b)):
    suma += i
print("La suma de los numeros comprendidos entre", a, "y", b, "es:", suma)


# Ejercicio 4: Sumar numeros ingresados hasta que se ingrese un 0.
suma = 0
while True:
    n = int(input("Ingrese un numero (0 para finalizar): "))
    if n == 0:
        break
    suma += n
print("La suma total es:", suma)


# Ejercicio 5: Juego de adivinar un numero entre 0 y 9.
import random
secreto = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivine el numero (entre 0 y 9): "))
    intentos += 1
    if intento == secreto:
        print("¡correcto! Lo adivino en", intentos, "intentos.")
        break
    else:
        print("incorrecto, intente nuevamente.")


# Ejercicio 6: Imprimir numeros pares entre 0 y 100 en orden decreciente.
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)


# Ejercicio 7: Calcular la suma de todos los numeros entre 0 y un numero positivo ingresado.
n = int(input("Ingrese un numero entero positivo: "))
suma = 0
for i in range(n + 1):
    suma += i
print("La suma de los números desde 0 hasta", n, "es:", suma)


# Ejercicio 8: Ingresar 100 numeros y contar pares, impares, positivos y negativos.
pares = impares = positivos = negativos = 0
cantidad = 100  
for i in range(cantidad):
    n = int(input(f"Ingrese el numero {i+1}: "))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)


# Ejercicio 9: Calcular la media de 100 numeros ingresados.
suma = 0
cantidad = 100  
for i in range(cantidad):
    n = float(input(f"Ingrese el numero {i+1}: "))
    suma += n
media = suma / cantidad
print("La media de los numeros ingresados es:", media)


# Ejercicio 10: Invertir los digitos de un numero ingresado.
num = int(input("Ingrese un numero entero: "))
invertido = 0
n = abs(num)
while n > 0:
    digito = n % 10
    invertido = invertido * 10 + digito
    n //= 10
if num < 0:
    invertido = -invertido
print("El numero invertido es:", invertido)


