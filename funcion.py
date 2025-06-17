import os

# Requisitos del Proyecto
# La aplicación debe permitir al usuario:
# 1.	Agregar un contacto: nombre, teléfono, email.
# 2.	Listar contactos: mostrar todos los contactos guardados.
# 3.	Buscar un contacto por nombre.
# 4.	Eliminar un contacto.
# 5.	Salir del programa.
# Debe usarse un menú para navegar entre estas opciones.
# La estructura de datos puede ser una lista de diccionarios.
# ________________________________________
# Organización del Trabajo
# •	El repositorio debe ser creado por uno de los integrantes del grupo y compartido con los otros.
# •	Todos deben clonar el repositorio en su computadora local.
# •	Cada alumno trabajará en una rama propia (ejemplo: rama-juan, rama-maria, rama-carlos).
# •	Cada uno será responsable de una parte del programa:
# o	Alumno 1: Función para agregar y mostrar contactos.
# o	Alumno 2: Función para buscar y eliminar contactos.
# o	Alumno 3: Estructura del menú principal y control de flujo del programa.

while True:
    os.system("cls")
    print("1) Agregar un contacto: nombre, teléfono, email")
    print("2) Listar contactos: mostrar todos los contactos guardados")
    print("3) Buscar un contacto por nombre")
    print("4) Eliminar un contacto")
    print("5) Salir del programa")
    try:
        opcion=int(input("ingrese opcion"))
        if opcion== 1:
            os.system("cls")
        
        elif opcion== 2:
            os.system("cls")
        
        elif opcion== 3:
            os.system("cls")
        
        elif opcion== 4:
            os.system("cls")
        
        elif opcion== 5:
            os.system("cls")
            print("adios")
            break
        else:
            print("opcion no existe")
                
        
    except:
        print("ingrese un numero")