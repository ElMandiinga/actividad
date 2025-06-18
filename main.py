import os
from funcion import *
os.system("cls")


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
           
    