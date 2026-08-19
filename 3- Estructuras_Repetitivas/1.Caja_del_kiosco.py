# Colocamos un cartel de bienvendida
print("\n================================")
print('Bienvenido al Kiosco "El Campus"')
print("================================")

#Comenzamos con bucles infinitos anidados
while True:
    # Dejamos acentadas las siguientes variables
    cantidad = 0
    precio = 0
    total_con_descuentos = 0
    total_sin_descuentos = 0
    productos = ""

    # Colocamos un bucle interno en el que al pedir el nombre solo se acepten letras
    while True:
        nombre = input("\nPor Favor, ingrese su nombre: ").title()
        if nombre.isalpha():
            break
        # En caso de ingresar carcteres erroneos mostrara el siguiente mensaje
        else:
            print("\nError: Debe ingresar solo su nombre.")

    # Colocamos un saludo para el cliente       
    print(f"\nHola {nombre}, hoy tenemos productos que tienen un 10% de descuento")
    # Utilizamos otro bucle infinito para colocar la cantidad de productos y solo se acepten numeros enteros mayor que 0
    while True:
        cantidad = input("\nPor favor ingrese la cantidad de productos a comprar: ")
        if cantidad.isdigit() and int(cantidad) > 0:
            cantidad = int(cantidad)
            break
        # Si se usan caracteres erroneos mostrara el siguiente mensaje
        else:
            print("\nError: Ingrese un numero entero positivo.")       
    # Usamos un for para guardar la cantidad de productos
    for i in range(cantidad):
        print(f"\nProducto {i + 1}")

        # Pedimos el precio de forma que solo se ingresen numeros enteros mayores que 0
        while True:
            precio = input("\nIngrese el precio del producto: ")
            if precio.isdigit() and int(cantidad) > 0:
                precio = int(precio)
                break
            # Si no ingresa numeros mostrara el siguiente mensaje
            else:
                print("\nError: Solo ingrese numeros enteros. ")

        # total_sin_descuentos = total_sin_descuentos + precio
        total_sin_descuentos += precio
        
        # Pedimos el descuento
        while True:
            descuento = input("\n¿Su producto tiene descuento? (S/N): ")
            # Usamos .lower() para poner los caracteres en mayusculas
            # Si la respuesta es "S" calculamos el 10% haciendo precio x 0.90 que nos mostraria el 90% del precio
            if descuento.lower() == "s":
                precio_con_descuento = precio * 0.90
                break
            # Si la respues es "N" se mantendra el mismo precio
            elif descuento.lower() == "n":
                precio_con_descuento = precio
                break
            else:
                # Solo se podra ingresar S o N
                print("\nError: ingrese 'S' para si o 'N' para no .")

        # total_con_descuentos = total_con_descuentos + precio_con_descuento            
        total_con_descuentos += precio_con_descuento
        # Realizamos un linea donde imprima productos por separado con su correspondiente precio y descuento
        productos += f"Producto {i + 1} - Precio: {precio} - Descuento (S/N): {descuento}\n"   
    # Calculamos el Ahorro y Promedio    
    ahorro = total_sin_descuentos - total_con_descuentos
    promedio = total_con_descuentos / cantidad                
     
    # Imprimimos los resultados
    print("\n=============================================")
    print("    ------ RESUMEN DE LA COMPRA ------")
    print(f"Cliente: {nombre}")
    print(f"Cantidad de productos: {cantidad}")
    print(f"{productos}")
    print(f"Total sin descuentos: ${total_sin_descuentos}")
    print(f"Total con descuentos: ${total_con_descuentos:.2f}")
    print(f"Ahorro total: ${ahorro:.2f}")
    print(f"Promedio por producto: ${promedio:.2f}")
    print("=============================================")

    # Colocamos otro bucle para continuar comprando o retirarse
    while True:
            continuar = input(f"\n{nombre}, ¿Desea realizar otra compra? (S/N): ")
            # Si responde "S" comenzara el programa desde el inicio de compras
            if continuar.lower() == "s":
                break
            # Si la respuesta es "N" mostrara un saludo de despedida
            elif continuar.lower() == "n":
                print(f"\nHasta luego {nombre}, que tenga un buen dia.")
                break
            # Si se colocan otros caracteres no permitidos imprimira lo siguiente
            else:
                print("\nError: ingrese 'S' para si o 'N' para no .")
    # Si la respuesta es "N" se da por finalizado el bucle            
    if continuar.lower() == "n":
        break    
            
    

    
        


            
            
    



