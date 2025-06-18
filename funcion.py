import os

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
def mostrar(nombres, correos, telefonos):
    if len(nombres)>0:
        for x in range(len(nombres)):
            print(f"{x+1}- nombre: {nombres[x]} correo: {correos[x]} telefono: {telefonos[x]}") 
    else:
        print("no hay nada en la lista")

def buscar_contacto(lista): 

    if len(lista)>0: 
        while True: 
            nombre_buscar=input("Ingrese el nombre del contacto que desea buscar \n") 
            if len(nombre_buscar)>2: 
                for x,contacto in enumerate(lista): 
                    if nombre_buscar in contacto:  
                       print(f"{x+1}- Nombre: {contacto}") 
                break 
            else: 
                print("El campo debe ser completado con más de 2 caracteres") 
    else: 
        print("No se puede encontrar contactos registrados") 

def eliminar_contacto(lista): 
    if len(lista)>0: 
        for x,contacto in enumerate(lista): 
            print(f"{x+1}- Nombre: {contacto}")      
        while True: 
            try: 
                eliminar=int(input("¿Cuál número telefónico desea eliminar?")) 
                if eliminar>0 and eliminar<=len(lista): 
                    lista.pop(eliminar-1) 
                    break 
                else: 
                    print("Número telefónico de contacto no encontrado") 
            except: 
                print("Debe ingresar un valor numérico") 
    else: 

        print("No aparecen contactos registrados") 
def main(): 
    contactos=[] 
    emails=[] 
    telefonos=[] 

    while True:  
        print("-- Menú de Gestión de Contactos --") 
        print("1. Agregar un contacto") 
        print("2. Listar contactos") 
        print("3. Buscar un contacto por nombre") 
        print("4. Eliminar un contacto") 
        print("5. Salir del programa")
        opcion = input("Elija una opción:").strip()
        if opcion == '1': 
            agregar(contactos, emails, telefonos) 
            os.system("cls")    
        elif opcion == '2': 
            mostrar(contactos, emails, telefonos) 
            os.system("cls")  
        elif opcion == '3': 
            buscar_contacto(contactos) 
            os.system("cls")  
        elif opcion == '4': 
            eliminar_contacto(contactos) 
            os.system("cls")  
        elif opcion == '5': 
            print("Gracias, adiós") 
            os.system("cls")  
            break   
        else: 
            print("Ingrese una Opción valida.")