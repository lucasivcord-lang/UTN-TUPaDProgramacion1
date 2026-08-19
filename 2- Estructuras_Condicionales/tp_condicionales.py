# Actividad 1:
# solicitaremos que se ingrese una edad y creamos un bucle infinito para evitar errores al ingresar caracteres que no sean numericos

# Solicitamos el ingreso de la edad
edad = int(input("Por favor, ingrese su edad: "))
# si es mayor o igual a 18 es "mayor de edad"
if edad >= 18:
    print("Es mayor de edad")
# si es menor a 18 es "menor de edad"        
else:
    print("Es menor de edad")

print("/////////////////////////////////////////////////////")

# Actividad 2:
# El usuario debera ingresar una calificacion mayor o igual (>=) a 6
# mayor a 6 sera aprobado, menor a 6 desaprobado

nota = int(input("Ingrese su calificacion (del 1 al 10): "))
# Colocamos la condicion de que el numero sea mayor o igual a 1 y menor o igual a 10
if 1 <= nota <= 10:
# si la nota es mayor o igual a 6 imprimira "Aprobado"
    if nota >= 6:
        print("Aprobado")
    # si la nota es menor a 6 imprimira "Desaprobado"        
    else:
        print("Desaprobado")
# Si se ingresa un numero mayor a 10
else:
    print("Ingrese una nota del 1 al 10.")
                       
print("/////////////////////////////////////////////////////")

# Actividad 3:
# El usuario debera ingresar un numero par
# Caso contrario se volvera a solicitar el numero par
# Usando el operador de resto (%). Para cualquier número entero, si el numero % 2 devuelve cero, es par; si devuelve uno, es impar.
numero = int(input("Ingrese un numero par: "))
if numero % 2 == 0:
    print("Ha ingresado un numero par")
# Si el numero % da un numero impar         
else:
    print("Por favor, ingrese un número par.")

print("/////////////////////////////////////////////////////")

# Actividad 4:
# Ingresar una edad para saber a cual categoria pertenece
edad = int(input("Ingrese su edad: "))
if edad < 0:
  print("Por favor, ingrese un número positivo")
# Si es menor de 12 = Niño
elif edad < 12:
    print("Eres un niño/a.")
# Si es mayor o igual de 13 y menor o igual a 17 = Adolecente
elif 12 <= edad < 18:
    print("Eres un adolecente.")
# Si es mayor o igual a 18 y menor o igual a 29 = adluto/a joven
elif 18 <= edad < 30:
    print("Eres un adulto/a joven.")
# Si es mayor a 30 = Adulto
else:
    print("Eres un adulto.")

print("/////////////////////////////////////////////////////")

# Actividad 5:
#La función len() se usa para obtener la cantidad de elementos de un objeto, como una cadena de texto, una lista o una tupla.
contraseña = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
# Se debera ingresar una contraseña alfanumerica de entre 8 a 14 caracteres
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta. ")
# Caso contrario se volvera a solicitar una contraseña con las condiciones requeridas
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres. ")

print("/////////////////////////////////////////////////////")


# Actividad 6:
# indique la categoría del consumo según el siguiente criterio
consumo = float(input("Ingrese el consumo de energia electrica en kilovatios: "))
# Si el consumo es menor a 149 kWh = Consumo bajo
if consumo < 150:
    print("Consumo bajo.")
# Si el consumo es mayor o igual a 150 kWh y menor o igual a 300 kWh = Consumo medio
elif 150 <= consumo <= 300:
    print("Consumo medio.")
# Si el consumo es mayor o igual a 301 kWh y menor o igual a 500 kWh = Consumo alto
elif consumo < 500:
    print("Consumo alto.")
# Si el consumo es mayor a 500 kWh se imprimira la advertencia
else:
    print("Considere medidas de ahorro energético.")

print("/////////////////////////////////////////////////////")

# Actividad 7:
frase = input("Ingrese una frase o palabra: ")
# Los strings en Python son secuencias de caracteres y cada carácter tiene una posición (índice).
# Para acceder al ultimo caracter ingresamos [-1]
# El operador "in" sirve para verificar si un elemento está contenido dentro de otro
# Si la frase termina en vocal mayuscula o minuscula se imprimira el signo "!" al final
if frase[-1] in ("AEIOUaeiou"):
    print(f"{frase}!")
# En caso de que la frase no termine en vocal se imprimira normalmente sin singo "!" al final
else:
    print(frase)

print("/////////////////////////////////////////////////////")

# Actividad 8:
# Pedimos al usuario un nombre
nombre = input("Ingrese su nombre: ")
# imprimimos opciones a elegir
print("""
Elija la opcion que desee:
1. ¿Desea su nombre en mayusculas?
2. ¿Desea su nombre en minusculas?
3. ¿Desea su nombre solo con la inicial en mayusculas?
""")
opcion = int(input("Elija el numero de la opcion correspondiente: "))
if opcion == 1:
# upper() Convierte todas las letras a mayusculas.    
    nombre_mayuscula = nombre.upper()
    print(nombre_mayuscula)
# lower() Convierte todas las letras a minúsculas.
elif opcion == 2:
    nombre_minuscula = nombre.lower() 
    print(nombre_minuscula)
# title() Convierte la primera letra de cada palabra a mayúscula y el resto a minúscula.
elif opcion == 3:
    inicial_mayuscula = nombre.title()
    print(inicial_mayuscula)   
else:
    print("Por favor, ingrese solo 1, 2 o 3.")   

print("/////////////////////////////////////////////////////")

# Actividad 9:
# Ingresamos la magnitud del terremoto
magnitud = float(input("Ingrese la magnitud del terremoto en escala de Richter: "))
# Si es menor de 3
if magnitud < 3:
    print("Muy leve (imperceptible).")
# Si es mayor o igual a 3 y menor a 4
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible).")
# Si es mayor o igual a 4 y menor a 5
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
# Si es mayor o igual a 5 y menor a 6
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
# Si es mayor o igual a 6 y menor a 7
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
#si es mayor de 7
else:
    print("Extremo (puede causar graves daños a gran escala).")

print("/////////////////////////////////////////////////////")

# Actividad 10:
# ingresamos hemisferio, mes y dia
hemisferio = input("¿En qué hemisferio te encuentras? N/S: ").upper()
mes = int(input("Ingreses el numero del mes (1-12): "))
dia = int(input("Ingrese el dia del mes: "))

# Hemsferio Norte
if hemisferio == "N": 
    # si el mes es 12 y el dia mayor o igual a 21, o mes entre 1 y 2, o mes 3 y dia menor a 21 sera invierno
    if (mes == 12 and dia >= 21) or mes in (1, 2) or (mes == 3 and dia < 21):
        estacion = "invierno"
    # si el mes es 3 y el dia mayor o igual a 21, o mes entre 4 y 5, o mes 6 y dia menor a 21 sera primavera
    elif (mes == 3 and dia >= 21) or mes in (4, 5) or (mes == 6 and dia < 21):
        estacion = "primavera"
    # si el mes es 6 y el dia mayor o igual a 21, o mes entre 7 y 8, o mes 9 y dia menor a 21 sera verano    
    elif (mes == 6 and dia >= 21) or mes in (7, 8) or (mes == 9 and dia < 21):
        estacion = "verano"
    # si el mes es 9 y el dia mayor o igual a 21, o mes entre 10 y 11, o mes 12 y dia menor a 21 sera otoño
    else:
        estacion = "otoño"

# Hemisferio Sur
elif hemisferio == "S":  #
    # si el mes es 12 y el dia mayor o igual a 21, o mes entre 1 y 2, o mes 3 y dia menor a 21 sera verano
    if (mes == 12 and dia >= 21) or mes in (1, 2) or (mes == 3 and dia < 21):
        estacion = "verano"
    # si el mes es 3 y el dia mayor o igual a 21, o mes entre 4 y 5, o mes 6 y dia menor a 21 sera otoño
    elif (mes == 3 and dia >= 21) or mes in (4, 5) or (mes == 6 and dia < 21):
        estacion = "otoño"
     # si el mes es 6 y el dia mayor o igual a 21, o mes entre 7 y 8, o mes 9 y dia menor a 21 sera invierno
    elif (mes == 6 and dia >= 21) or mes in (7, 8) or (mes == 9 and dia < 21):
        estacion = "invierno"
    # si el mes es 9 y el dia mayor o igual a 21, o mes entre 10 y 11, o mes 12 y dia menor a 21 sera primavera
    else:
        estacion = "primavera"
# Imprimimos el resultado
print(f"Te encuentras en {estacion}.")

                        
    


