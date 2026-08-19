# Colocamos variables con espacio vacios y por separado para evitar usar listas []
# Lunes 4 turnos
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
# Martes 3 turnos
martes1 = ""
martes2 = ""
martes3 = ""

# En un bucle, pedimos que se ingrese el nombre con "title" para que la inicial la convierta en mayuscula
# Ademas usamos "isalpha" para que solo acepte letras y no otros caracteres
while True:
        operador = input("\nPor Favor, ingrese el nombre del operador: ").title()
        if operador.isalpha():
            # Usamos un mensaje de bienvenida para el operador
            print(f"\nBienvenido {operador}, elija una opcion")
            break
        # Error para el ingreso de caracteres que no sean letras
        else:
            print("\nError: Debe ingresar solo su nombre.")
# Imprimimos el menu para el operador
while True:
    print("\n    -----Menu-----")
    print("1) Reservar turno")
    print("2) Cancelar turno")
    print("3) Ver agenda del dia")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")

    opcion = input("\nOpción: ")
    # Colocamos que la opcion sea un numero entero y no otro caracter
    if not opcion.isdigit():
                print("\nError: ingrese un número válido.")
                continue
    opcion = int(opcion)
    
    
    # Validamos el rango de la opcion con numero mayor a 1 y menor a 5
    if opcion < 1 or opcion > 5:
        # Caso contrario lanzara el siguiente error
        print("\nError: opción fuera de rango (1 al 5).")
        continue

    # Opcion 1    
    if opcion == 1:
        while True:
            # Bucle con 2 opciones
            print("\n1) Turno Lunes")
            print("2) Turno Martes")
            # Las opciones a elegir son 1 y 2
            dia = input("\nElija un dia para reservar: ")
            if not dia.isdigit():
                # Si no coloca los numeros 1 y 2 dara error
                print("Error: ingrese un numero.")
                continue
            # Numero entero
            dia = int(dia)
            # menor a 1 o mayor a 2 sera no valido
            if dia < 1 or dia > 2:
                print("\nDia no valido (elija 1 o 2)")
                continue
            
            if dia == 1:
                # SElecciono dia 1 (Lunes)
                # Solicitara el nombre del cliente (solo letras) que haya quedado guardado en uno de los 4 espacios vacios del lunes
                nombre = input("\nNombre de la persona: ").title()
                if not nombre.isalpha():
                    print("\nError: ingrese solo letras.")
                elif lunes1 == "":
                    lunes1 = nombre
                    print(f"\nTurno de {nombre} reservado para el día lunes.")
                elif lunes2 == "":
                    lunes2 = nombre
                    print(f"\nTurno de {nombre} reservado para el día lunes.")
                elif lunes3 == "":
                    lunes3 = nombre
                    print(f"\nTurno de {nombre} reservado para el día lunes.")
                elif lunes4 == "":
                    lunes4 = nombre
                    print(f"\nTurno de {nombre} reservado para el día lunes.")

                # En caso de tener todos los espacios ocupados dara el siguiente mensaje    
                else:
                    print("\nNo hay cupos disponibles para el lunes.")     
                    break
                print("\n¿Desea realizar otra consulta?")       
                break

            elif dia == 2:
                # SElecciono dia 2 (Martes)
                # Solicitara el nombre del cliente (solo letras) que haya quedado guardado en uno de los 3 espacios vacios del martes
                nombre = input("\nNombre de la persona: ").title()
                if not nombre.isalpha():
                    print("\nError: ingrese solo letras.")
                elif martes1 == "":
                    martes1 = nombre
                    print(f"\nTurno de {nombre} reservado para el día martes.")
                elif martes2 == "":
                    martes2 = nombre
                    print(f"\nTurno de {nombre} reservado para el día martes.")
                elif martes3 == "":
                    martes3 = nombre
                    print(f"\nTurno de {nombre} reservado para el día martes.")

                # En caso de tener todos los espacios ocupados dara el siguiente mensaje    
                else:
                    print("\nNo hay cupos disponibles para el martes.")
                    break
                print("\n¿Desea realizar otra consulta?")            
                break 

    # Opcion 2                    
    if opcion == 2:
        while True:
            # Bucle donde seleccionamos el dia a cancelar el turno
            print("\n1) Turno Lunes")
            print("2) Turno Martes")
            # Solo podemos ingresar numeros (1 y 2)
            dia = input("\nElija el día del turno a cancelar: ")
            if not dia.isdigit():
                    print("\nError: ingrese un número (1 o 2).")
                    continue
            
            # Se debe seleccionar un numero entero que no sea menor a 1 y mayor a 2, sino no sera valido
            dia = int(dia)
            if dia < 1 or dia > 2:
                print("\nDía no válido. Elija 1 o 2.")
                continue 

            # Solicitamos en el siguiente bucle el nombre de la persona a cancelar el turno
            while True:        
                nombre = input("\nIngrese el nombre del turno a cancelar: ").title()
                # Solo se aceptaran letras
                if nombre.isalpha():
                    break
                else:
                    print("\nError: ingrese solo letras.")
            # Si un nombre coincide con lo agendado en alguno de los 4 espacios del lunes lo remplazara por un espacio vacio
            if dia == 1:
                if lunes1 == nombre:
                    lunes1 = ""
                    print("\nTurno cancelado correctamente.")
                elif lunes2 == nombre:
                    lunes2 = ""
                    print("\nTurno cancelado correctamente.")
                elif lunes3 == nombre:
                    lunes3 = ""
                    print("\nTurno cancelado correctamente.")
                elif lunes4 == nombre:
                    lunes4 = ""
                    print("\nTurno cancelado correctamente.")
                # Si el nombre no coincide
                else:
                    print("\nNo se encontró un turno para ese paciente.")
                print("\n¿Desea realizar otra consulta?")            
                break  
                          
                  
            # Si un nombre coincide con lo agendado en alguno de los 3 espacios del martes lo remplazara por un espacio vacio        
            elif dia == 2:
                if martes1 == nombre:
                    martes1 = ""
                    print("\nTurno cancelado correctamente.")
                elif martes2 == nombre:
                    martes2 = ""
                    print("\nTurno cancelado correctamente.")
                elif martes3 == nombre:
                    martes3 = ""
                    print("\nTurno cancelado correctamente.")
                # Si el nombre no coincide    
                else:
                    print("\nNo se encontró un turno para ese paciente.")
                    
                print("\n¿Desea realizar otra consulta?")            
                break  

    # Opcion 3                
    elif opcion == 3:
        # se hara un bucle que mostrara la agenda del dia seleccionado
        while True:
            print("\n1) Lunes")
            print("2) Martes")

            dia = input("\nElija el día: ")
            # Solo se puede ingresar numeros, de lo contrario el siguiente error
            if not dia.isdigit():
                print("\nError: ingrese un número válido.")
                continue

            # Se tendra que colocar un numero entero que no sea menor a 1 ni mayor a 2
            dia = int(dia)
            if dia < 1 or dia > 2:
                print("\nError: elija 1 para Lunes o 2 para Martes.")
                continue
            
            if dia == 1:
                print("\n--- AGENDA DEL LUNES ---")
                # Si lunes1 no está vacío, mostrar el nombre. Si está vacío, mostrar "Libre".
                print(f"Turno 1: {lunes1 if lunes1 != '' else 'Libre'}")
                # Si lunes2 no está vacío, mostrar el nombre. Si está vacío, mostrar "Libre".
                print(f"Turno 2: {lunes2 if lunes2 != '' else 'Libre'}")
                # Si lunes3 no está vacío, mostrar el nombre. Si está vacío, mostrar "Libre".
                print(f"Turno 3: {lunes3 if lunes3 != '' else 'Libre'}")
                # Si lunes4 no está vacío, mostrar el nombre. Si está vacío, mostrar "Libre".
                print(f"Turno 4: {lunes4 if lunes4 != '' else 'Libre'}")
                break
            

            elif dia == 2:
                print("\n--- AGENDA DEL MARTES ---")
                # Si martes1 no está vacío, mostrar el nombre. Si está vacío, mostrar "Libre".
                print(f"Turno 1: {martes1 if martes1 != '' else 'Libre'}")
                # Si martes2 no está vacío, mostrar el nombre. Si está vacío, mostrar "Libre".
                print(f"Turno 2: {martes2 if martes2 != '' else 'Libre'}")
                # Si martes3 no está vacío, mostrar el nombre. Si está vacío, mostrar "Libre".
                print(f"Turno 3: {martes3 if martes3 != '' else 'Libre'}")
                break  
            print("\n¿Desea realizar otra consulta?")               
            break  

    # Opcion 4
    elif opcion == 4:

        print("\n========== RESUMEN GENERAL ==========")

        print("\n--- LUNES ---")
        # Si lunes1,2,3,4 no está vacío, mostrar el nombre. Si está vacío, mostrar "Libre".
        print(f"Turno 1: {lunes1 if lunes1 != '' else 'Libre'}")
        print(f"Turno 2: {lunes2 if lunes2 != '' else 'Libre'}")
        print(f"Turno 3: {lunes3 if lunes3 != '' else 'Libre'}")
        print(f"Turno 4: {lunes4 if lunes4 != '' else 'Libre'}")

        print("\n--- MARTES ---")
        # Si martes1,2,3 no está vacío, mostrar el nombre. Si está vacío, mostrar "Libre".
        print(f"Turno 1: {martes1 if martes1 != '' else 'Libre'}")
        print(f"Turno 2: {martes2 if martes2 != '' else 'Libre'}")
        print(f"Turno 3: {martes3 if martes3 != '' else 'Libre'}")

        print("====================================")
    # Opcion 5
    elif opcion == 5:
        # Se cierra el sistema y dara un mensaje de despedida
        print(f"\nSistema cerrado. ¡Hasta luego {operador}!")
        break                    









                 
                                        










                

                    



