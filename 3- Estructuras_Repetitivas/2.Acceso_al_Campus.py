# Dejamos acentadas las variables
usuario_correcto = "alumno"
contraseña_correcta = "python123"

intentos = 0
acceso = False
print("    ========CAMPUS VIRTUAL=========")
print("Por Favor, ingrese su usuario y contraseña")
print("Recuerde que solo tiene un limite de 3 intentos")
# Comenzamos con un bucle while donde solo permita 3 intentos
while intentos < 3:
    print(f"\nIntento {intentos + 1}/3")

    usuario = input("Usuario: ")
    contraseña = input("Clave: ")
    # Si el usuario y la contraseña son correctos concedera el acceso
    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        print("\nAcceso concedido.")
        acceso = True
        break
    # Si el usuario o contraseña son incorrectos mostrara el siguiente mensaje
    else:
        print("\nError: credenciales inválidas.")
    # Cada intento sumara al contador
    intentos += 1

# Si falla los 3 intentos bloqueara la cuenta
if acceso == False:
    print("\nCuenta bloqueada.")

else:
    # MENÚ
    while True:
        print("\n===MENU SEGURO===")
        print("\n1) Estado")
        print("2) Cambiar clave")
        print("3) Mensaje")
        print("4) Salir")

        opcion = input("\nOpción: ")

        # Validar que sea número entero 
        if not opcion.isdigit():
            print("\nError: ingrese un número válido.")
            continue

        opcion = int(opcion)

        # Validar rango de opciones entre 1 y 4
        if opcion < 1 or opcion > 4:
            # Colocar un numero menor a 1 o mayor a 4 dara error
            print("\nError: opción fuera de rango.")
            continue

        # Opción 1
        if opcion == 1:
            print("\nEstado: Inscripto")

        # Opción 2
        elif opcion == 2:
            # Colocamos un bucle donde solo deje avanzar con una clave minima de 6 caracteres
            while True:
                nueva_clave = input("\nNueva clave: ")

                if len(nueva_clave) < 6:
                    print("\nError: mínimo 6 caracteres.")
                else:
                    break
            # Confirmamos la nueva clave            
            confirmacion = input("\nConfirmar nueva clave: ")

            if nueva_clave == confirmacion:
                clave_correcta = nueva_clave
                print("\nClave cambiada correctamente.")
            else:
                print("\nError: las claves no coinciden.")

        # Opción 3
        # Imprimimos un mensaje motivacional
        elif opcion == 3:
            print("\n¡Vos podés lograrlo, seguí adelante!")

        # Opción 4
        # Finalizamos la sesion
        elif opcion == 4:
            print("\nSesión finalizada.")
            break