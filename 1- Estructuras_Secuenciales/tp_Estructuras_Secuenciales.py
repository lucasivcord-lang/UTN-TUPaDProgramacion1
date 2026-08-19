# Actividad 1: Imprimimos en pantalla "Hola Mundo"
print("Hola Mundo!!")

print("/////////////////////////////////////////////////////") # Utilizamos un separador con barras

# Actividad 2: 
# Colocamos la variable nombre
nombre = input("Ingresa tu nombre: ")
# creamos un "f-string" para poder insertar variables dentro de la siguiente funcion
print(f"Hola {nombre}!") 

print("/////////////////////////////////////////////////////")

# Actividad 3
# Solicitamos 4 variables: Nombre, Apellido, Edad y Residencia
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Lugar de residencia: ")
# creamos un "f-string" para imprimir las variables solicitadas anteriormente
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

print("/////////////////////////////////////////////////////")

# Actividad 4
# Agregamos "import math" para tener acceso a funciones matematicas (ej: pi)
import math
# Solicitamos con "float" un numero decimal
radio = float(input("Ingrese el radio del circulo: "))
# math.pi = pi (3.141592653589793) * radio al cuadrado
area = math.pi * radio ** 2
# perimetro es 2 * pi (3.141592653589793) * radio
perimetro = 2 * math.pi * radio
# creamos "f-string" para insertar variables dentro de la siguiente funcion
print(f"Area:  {area}")
print(f"Perimetro: {perimetro}")

print("/////////////////////////////////////////////////////")

# Actividad 5
# Creamos la variable donde se ingrese un numero entero
segundos = int(input("Ingresa una cantidad de segundos: "))
# la siguiente variable sera la cantidad de segundos dividido segundos en una hora (3600)
horas = segundos / 3600
# creamos un "f-string" donde imprima el resultado
print(f"{segundos} segundos equivalen a {horas} horas.")

print("/////////////////////////////////////////////////////")

# Actividad 6
# Solicitamos un numero entero
numero = int(input("Ingresa el numero a multiplicar"))
# Utilizamos \n para hacer un salto de lineas
print(f"\nTabla de multiplicar del {numero}:")
# Indicamos que se imprima un rango del 1 al 10
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

print("/////////////////////////////////////////////////////")

# Actividad 7
# Solicitamos 2 numeros distintos de cero

num1 = int(input("Ingrese el primer número entero (distinto de 0): "))
num2 = int(input("Ingrese el segundo número entero (distinto de 0): "))

# Realizar las operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

# Mostrar los resultados
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

print("/////////////////////////////////////////////////////")

# Actividad 8
# Solicitamos la variables peso y altura
peso = float(input("Ingrese el peso en kilogramos: "))
altura = float(input("Igrese la altura en metros: "))

# Calculamos el IMC realizando peso dividido (altura al cuadrado)
imc = peso / (altura ** 2)

# Imprimimos el indice con un "f-string" con la variable IMC
print(f"El indice de masa corporal es {imc}")

print("/////////////////////////////////////////////////////")

# Actividad 9
# Solicitamos la temperatura en Celsius
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Convertimos a Fahrenheit con el siguiente calculo
fahrenheit = (9 / 5) * celsius + 32

# Mostramos el resultado
print(f"{celsius} °C equivalen a {fahrenheit} °F")

print("/////////////////////////////////////////////////////")

# Actividad 10
# Solicitamos 3 numeros flotantes
numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
numero3 = float(input("Ingrese el tercer numero: "))

# Calculamos el promedio de la siguiente forma
promedio = (numero1 + numero2 + numero3) / 3

# Imprimimos el promedio
print(f"el promedio es de {promedio}")

