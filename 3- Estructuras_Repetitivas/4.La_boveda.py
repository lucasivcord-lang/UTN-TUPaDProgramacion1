while True:
    # Dejamos acentadas las variables
    energia = 100
    tiempo = 12
    cerraduras_abiertas = 0
    alarma = False
    codigo_parcial = ""
    forzar_seguidas = 0   

    while True:
        # En un bucle, pedimos que se ingrese el nombre con "title" para que la inicial la convierta en mayuscula
        # Ademas usamos "isalpha" para que solo acepte letras y no otros caracteres
        nombre = input("\nIngrese el nombre del agente: ").title()
        if not nombre.isalpha():
            print("\nPor Favor, ingrese un nombre. ")
            continue
        break
    # Imprimimos un mensaje de bienvenida
    print(f'\nBienvendio, agente {nombre} a Escape Room "La Bóveda"')
    print("Tenés que abrir las 3 cerraduras antes de quedarte sin energía o tiempo.")
    print("Comenzaras con 100 de eneriga y 12 de tiempo")

    # El bucle seguira funcionando siempre y cuando
    # La energia sea mayor a 0
    # El tiempo sea mayor a 0
    # Tiene que haber menos de 3 cerraduras abiertas
    # La alarma tiene que estar apagada (False)

    while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma == True and tiempo <= 3):

        # Imprimimos el estado del juego
        print("\n===================================")
        print("           ESTADO DEL JUEGO")
        print("===================================")
        print(f"Energía: {energia}")
        print(f"Tiempo: {tiempo}")
        print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
        print(f"Código parcial: {codigo_parcial}")
        print(f"Alarma: {'ACTIVADA' if alarma else 'DESACTIVADA'}")
        # Imprimimo las opciones seleccionables
        print("\n===================================")
        print("\n-----Opciones-----")
        print("1) Forzar cerradura.")
        print("2) Hackear panel.")
        print("3) Descansar.")

        # Colocamos un bucle donde seleccionesmos una de las 3 opciones
        while True:
            opcion = input("\nElija una opción: ")
            # La opcion debe ser un numero entero
            if opcion.isdigit():
                opcion = int(opcion)
                # Debe ser mayor o igual a 1 o menor o igual a 3
                if opcion >= 1 and opcion <= 3:
                    break
                # Si se colocan caracteres quu no sean los numeros acordados dara error
                else:
                    ("\nError: ingrese un número válido.")
            else:
                print("\nError: ingrese un número válido.")

        # Opcion 1
        if opcion == 1:
            # -20 de energia
            energia -= 20
            # -2 de tiempo
            tiempo -= 2
            # Sumamos un intento de forzar cerraduras
            forzar_seguidas += 1

            # Imprimimos los resultados
            print("\nForzando cerradura...")
            print("Energía -20")
            print("Tiempo -2")

            # Regla anti-spam, si la cerradura se fuerza 3 veces seguidas activara la alarma
            if forzar_seguidas == 3:
                print("\n¡La cerradura se trabó!")
                print("¡Alarma activada!")
                alarma = True
            

            else:
                # Riesgo de alarma si la energia es menor a 40
                if energia < 40:
                    while True:
                        numero = input("\nRiesgo de alarma. Elija un número del 1 al 3: ")
                        # Solo se puede elegir un numero entre 1 o 3
                        if numero.isdigit():
                            numero = int(numero)
                            if numero >= 1 and numero <= 3:
                                break
                            # Error por colocar caracteres o numeros fuera del rango
                            else:
                                print("\nError: ingrese un número entre 1 y 3.")
                        else:
                            print("\nError: ingrese un número válido.")

                    if numero == 3:
                        alarma = True
                        print("\n¡Elegiste 3! La alarma se activó.")

                    else:
                        # Se suma un intento de cerradura abiera
                        cerraduras_abiertas += 1
                        print("\n¡Cerradura abierta!")

                # Se suma un intento de cerradura abiera
                else:
                    cerraduras_abiertas += 1
                    print("\n¡Cerradura abierta!")
                        
        # Opcion 2
        elif opcion == 2:
            # Hackear el panel
            # -10 de energia
            energia -= 10
            # -3 de tiempo
            tiempo -= 3

            # Se corta la racha de forzar
            forzar_seguidas = 0

            print("\nHackeando panel...")
            # Si codigo_parcial >= 8, se abre automáticamente 1 cerradura si todavía faltan.
            for i in range(4):
                codigo_parcial += "A"
                print(f"Paso {i + 1}/4 - Código: {codigo_parcial}")
            # Si codigo parcial mayor o igual a 8 y cerraduras abiertas es menor a 3 se completa el codigo
            if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("\n¡Código completado! Se abrió una cerradura.")
            # Caso contrario dara el siguiente mensaje
            else:
                print("\nEl código todavía no es suficiente para abrir otra cerradura.")

        # Opcion 3
        elif opcion == 3:
            # Descansar
            forzar_seguidas = 0

            # + 15 de energia
            energia += 15
            # Energia maxima 100
            if energia > 100:
                energia = 100
            # -1 de tiempo
            tiempo -= 1

            # Imprimimos los resultados
            print("\nDescansando...")
            print("Energía +15")
            print("Tiempo -1")

            # Activacion de la alarma
            if alarma == True:
                energia -= 10
                print("\n¡La alarma está activa! Energía extra -10.")
                        
    # ===================================
    # FIN DEL JUEGO
    # ===================================
    # Si las cerraduras se abren 3 veces (No seguidas)
    if cerraduras_abiertas == 3:
        print("\n===================================")
        print("          ¡VICTORIA!")
        print("===================================")
        print("¡Abriste las 3 cerraduras!")

    # Si suena la alarma y el tiempo es menor o igual a 3 o la cerradura se abre menos de 3 veces
    elif alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
        print("\n===================================")
        print("      ¡SISTEMA BLOQUEADO!")
        print("===================================")
        print("La alarma bloqueó la bóveda.")
        print("DERROTA.")

    # Si la energia o el tiempo son menor o igual a 0
    elif energia <= 0 or tiempo <= 0:
        print("\n===================================")
        print("           ¡DERROTA!")
        print("===================================")
        print("Te quedaste sin energía o sin tiempo.")

# =================================== 
#           VOLVER A JUGAR 
# ===================================
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