#Ejercicio 1
edad=int(input("ingrese su edad"=)
         if edad> 18:
         print("Es mayor de edad")
         else:
         print("No es mayor de edad")
        
# se utiliza una estrucura if-else para verificar si la edad ingresada es mayor a 18.


#Ejercicio 2
nota=int(input("Ingrese su nota:"))
if nota>=6:
print("Aprobado")
else:
print("Desasprobado")
# Se unsa if--else comparando con >=6 para decidir si aprueba o no

#Ejercicio 3
numero=int(input("Ingrese un numero:"))
if nunmero%2 == 0:
print("Ingreso un numero par")
else:
print("Ingrese un numero par")
# Se usa el % para comprobar si el resto de dividir por 2 es cero.

#Ejercicio 4
edad = int(input("Ingrese su edad:"))
if edad < 12:
print("Niño")
elif edad < 18:
pirnt("Adolescente")
elif edad < 30:
print("Adulto joven")
# Se emplea if-elif-else para manejar varios rangos de edad

#Ejercicio 5
contrasena = input("Ingrese una contrasena:")
if 8 <= len(contrasena) <= 14:
print ("Ingreso una contreseña correcta")
else:
print("Por favor ingrese una contrasena de 8 o 14 caracteres")
# Se utiliza la funcion len() para medir la longitud de la contraseña

#Ejercicio 6
import random
from statistics import mean, median, moda
numeros_aleatorios = [random.randint(1, 100) for i in range (50)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numero_aleatorios)

print("media:", media)
print("mediana:", moda)
print("moda:", moda)
if media > mediana  > moda:
print("sesgo positivo o a la derecha")
elif media < mediana < moda
print("sesgo negativo o a la izquierda")
else:
print("sin sesgo")
# Se usan funciones mean, median, moda del modulo statistics para calcular medidas estadisticas.

#Ejercicio 7
texto = input("ingrese una palabra o frase")
if texto [-1].lower()  in "aeiou":
print(texto +  "!")
else:
print(texto)
# se toma el ultimo caracterr con texto [-1] y se verifica si es vocal.

#Ejercicio 8
nombre= input("ingrese su nombre:")
opcion= int(input("ingrese 1 para matusculas, 2 para minusculas o  3 para primera mayuscula:")
            if opcion == 1:
            print(nombre.upper())
            elif opcion == 2:
            print(nombre.lower())
            elif opcion == 3:
            print(nombre.title())
            else:
            print("opcion no valida")

# se usan los metodos upper, lower, title para modificar el string segun la opcion.

#Ejercicio 9
magnitud = float(input("ingrese la magnitud del terremoto:"))
if magnitud < 3:
print("Muy leve")
elif magnintud < 4:
print("leve")
elif magnitud < 5:
print("moderado")
elif magnitud < 6:
print("fuerte")
elif magnitud < 7:
print("muy fuerte")
else:
print("extremo")

# Se usa if,elif,else comparando intervalos de la magnitud.

#Ejercicio 10
hemisferio = input("ingrese hemisferio (n/s):").upper()
mes = int(input("ingrese numero de mes (1-12):"))
dia = int(input("ingrese dia:"))

if (mes == 12 and dia >= 21) or mes in [1,2] or (mes == 3 and dia <=20 ):
estacionN, estacionS = "Invierno", "Verano"
elif (mes == 3 and dia >= 21) or mes in [4,5]or (mes== 6 and dia <= 20 ):
estacionN, estacionS = "Primavera", "Otono"
elif(mes== 6 and dia>= 21) or mes [7,8] or (mes== 9 and dia<=20):
estacionN, estacionS = "Verano", "Invierno"
else:
estacionN, estacionnS = "Otono", "Primavera"
if hemisferio == "N":
print("Estacion:", estacionN)
else:
print("Estacion:", estacionS)
# Se evaluan los intervalos de fechas y se asignan estaciones distintas segun el hemisferio.