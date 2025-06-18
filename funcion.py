def agregar(nombres, correos, telefonos):
    while True:
        nombre = input("Ingrese el nombre\n") 
        if len(nombre) > 2:
            nombres.append(nombre)
            print("Nombre ingresado satisfactoriamente")
            break
        else:
            print("El nombre ingresado no cumple con los requisitos")
    while True:
        correo = input("Ingrese su correo electrónico")
        if len(correo) > 4 and "@" in correo:
            correos.append(correo)
            print("Correo electrónico agregado exitosamente")
            break
        else:
            print("Correo electrónico ingresado inválido")        
    while True:
        try:
            telefono = (input("Ingrese el numero celular de 8 digitos\n"))
            if  len(telefono) == 8: 
                telefono = int(telefono)
                telefonos.append(telefono)
                print("Número telefónico ingresado satisfactoriamente")
                break
            else:
                ("Número ingresado es inválido")            
        except:
            print("El número de teléfono debe ser números enteros y de 8 digitos")