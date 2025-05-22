# import sys
# import os
# # Agregar el directorio del proyecto al sys.path para que Python pueda encontrar el paquete
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


""" Módulo de menú y flujo principal."""
from .crud import add_contact, get_contact, update_contact, delete_contact
from .models import contacts, exists, get_all


def show_menu():
    """ Función que muestra las opciones del menú"""
    print("\nGESTOR DE CONTACTOS")
    print("-"*40)
    print("Opciones:")
    print("1. Agregar contacto")
    print("2. Modificar contacto")
    print("3. Eliminar contacto")
    print("4. Buscar contacto")
    print("5. Ver contactos")
    print("6. Salir.")
    print("-"*40)


def run():
    while True:
        show_menu()
        opc = input("Seleccione una opción: ")

        if opc == "1": #AGREGAR
            
            print("\nComplete los campos:")
            cedula = input(" Cédula: ")
            nombres = input(" Nombres: ").title()
            celular = input(" Celular: ")
            state , mesagge = add_contact(cedula, nombres, celular)
            print(mesagge)

        elif opc == "2": #MODIFICAR
            print("\nComplete los campos:(Si no desea modifcar precione ENTER.)")
            cedula = input(" Buscar por cédula: ")
            nombres = input(" Modifique nombres: ").title()
            celular = input(" Modifique celular: ")
            state, mesagge = update_contact(cedula, nombres, celular)
            print(mesagge)

        elif opc == "3": #ELIMINAR
            print("\nComplete los campos:")
            cedula = input(" Eliminar por Cédula: ")
            state, mesagge = delete_contact(cedula)
            print(mesagge)

        elif opc == "4": #BUSCAR
            print("\nComplete el campo:")
            cedula = input("Buscar por Cedula: ")
            state, mesagge = get_contact(cedula)
            print(mesagge if state else f"Error:{mesagge}")

        elif opc == "5": #LISTAR
            for cedula, data in get_all().items():
                print(f"El usuario con cédula: {cedula} tiene los siguientes datos: \n- Nombres: {data['nombres']} \n- Celular: {data['celular']} \n- Fecha: {data['fecha']}")

        elif opc == "6": #SALIR
            print("¡Saliste del programa.!")
            break

        else:
            print("Error: Opción incorrecta. Ingrese una opción válida.")


if __name__ == "__main__":
    #show_menu()
    print(run())
    #print(contacts)


