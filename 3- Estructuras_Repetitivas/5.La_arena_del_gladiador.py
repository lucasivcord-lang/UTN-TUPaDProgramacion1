
# Iniciamos con un bucle while donde pediremos un nombre y solo se puedan ingresar letras
while True:
    # Acentamos las variables a utilizar
    vida_gladiador = 100 
    vida_enemigo = 100 
    pociones = 3 
    ataque_pesado = 15
    daño_enemigo = 12 
    turno_gladiador = True

    while True:
        nombre = input("\nIngrese el nombre del gladiador: ").title()
        if nombre.isalpha():
            print(f'\nBienvenido {nombre} a La Arena')
            break
        else:    
            print("\nError: Solo se permiten letras")

    print("\n ====== INICIO DEL COMBATE =======")
    # Mientras la vida del gladiador y el enemigo sea mayor a cero, seguira el bucle
    while vida_gladiador > 0 and vida_enemigo > 0:
        # Turno del gladiador
        if turno_gladiador == True:
            # Estadisticas del gladiador y el enemigo
            print("\n-----------------------------------")
            print(f"{nombre} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo})")
            print(f"Pociones: {pociones}")
            print("-----------------------------------")
            # Opciones de combate
            print("\nElige acción:")
            print("1) Ataque Pesado")
            print("2) Ráfaga Veloz")
            print("3) Curar")
            

            # Validamos la opcion
            while True:
                opcion = input("Opción: ")
                # La opcion debe ser solo numeros
                if not opcion.isdigit():
                    print("\nError: Ingrese un número válido.")
                    continue

                # La opcion debe ser un numero entero entre 1 y 3
                opcion = int(opcion)
                if opcion < 1 or opcion > 3:
                    print("\nError: Elija una opción entre 1 y 3.")
                    continue
                break

            # Opcion 1: Ataque pesado
            if opcion == 1:
                # Si la vida del enemigo es menor a 20 puntos
                if vida_enemigo < 20:
                    daño = ataque_pesado * 1.5
                    # El jugador realiza un "Golpe Crítico" multiplicando su daño base por 1.5
                    print("\n¡GOLPE CRÍTICO!")

                # Si la vida del enemigo es mayor a 20 puntos el golpe sera basico
                else:
                    daño = ataque_pesado
                vida_enemigo -= daño
                print(f"\n¡Atacaste al enemigo por {daño} puntos de daño!")

            # Opcion 2: Rafaga veloz
            elif opcion == 2:
                print("\n¡Inicias una rafaga de golpes!")
                for i in range(3):
                # inicias una rafaga de 3 golpes que quitan 5 puntos cada uno
                    vida_enemigo -= 5
                    print("\n> Golpe conectado por 5 de daño")

            # Opcion 3: Curar
            elif opcion == 3:
                # Tienes 3 pociones
                if pociones > 0:
                    # Mientas las pociones sean mayores a 0 el gladiador puede curarse 30 puntos
                    vida_gladiador += 30
                    pociones -= 1

                    # La vida no puede superar 100 puntos (maximo permitido)
                    if vida_gladiador > 100:
                        vida_gladiador = 100
                    print("\n¡Te has curado 30 puntos!")
                    print(f"Vida actual: {vida_gladiador}")
                else:
                    # Pociones = 0
                    print("\n¡No quedan pociones!")       

            # Comprobar si el enemigo sigue vivo
            if vida_enemigo <= 0:
                break

            # Turno del enemigo
            turno_gladiador = False
        if turno_gladiador == False:
            vida_gladiador -= daño_enemigo
            print(f"\n¡El enemigo te ataco por {daño_enemigo} puntos de daño!")
            # Volver al turno del jugador
            turno_gladiador = True
        print("\n  ====== NUEVO TURNO ======")     
    # FIN DEL JUEGO
    print("\n===================================")
    if vida_gladiador > 0:
        print(f"\n¡VICTORIA! {nombre} ha ganado la batalla.")
    else:
        print("\nDERROTA. Has caído en combate.")
    print("===================================")

    while True: 
        continuar = input("\n¿Desea volver a jugar? (S/N): ").lower()
        if continuar == "s": 
            print("\n¡Comenzando una nueva partida!") 
            break
                        
        elif continuar == "n": 
            print("\nGracias por jugar. ¡Hasta la próxima!") 
            exit()
        # Si se colocan otros caracteres no permitidos imprimira lo siguiente
        else:
            print("\nError: ingrese 'S' para si o 'N' para no .")






















