from gestor_contactos.models import get_all, exists
from gestor_contactos.crud import add_contacts,get_contact,delete_contact,update_contact

def show_menu():
    print("1. Añadir contacto")
    print("2. Mostrar informacion del contacto")
    print("3. Eliminar contacto")
    print("4. Ver todos los contactos")
    print("5. Comprobar si el contacto existe")
    print("6. Actualizar informacion del contacto")
    print("7. Salir del Menu")
def run():
    while True:
        show_menu()
        choice=(input("Elija una opcion: ")).strip().lower()
        if choice == '1' or choice == "añadir contacto":
            cedula=input("Ingrese la cédula del contacto: ")
            nombre=input("Ingrese el nombre del contacto: ")
            apellido=input("Ingrese el apellido del contacto: ")
            celular=input("Ingrese el número celular del contacto: ")
            exito,mensaje=add_contacts(cedula,nombre,apellido,celular)
            print(exito,mensaje)
        elif choice == '2' or choice == "mostrar informacion del contacto":
            cedula=input("Ingrese la cédula del contacto: ")
            exito,mensaje=get_contact(cedula)
            print(exito,mensaje)
        elif choice == '3' or choice == "eliminar contacto":
            cedula=input("Ingrese la cédula del contacto: ")
            exito,mensaje=delete_contact(cedula)
            print(exito,mensaje)
        elif choice == '4' or choice == "ver todos los contactos":
            exito,mensaje=get_all()
            print(exito,mensaje)
        elif choice == '5' or choice == "comprobar si el contacto existe":
            cedula=input("Ingrese la cédula del contacto: ")
            exito,mensaje=(exists(cedula))
            print(exito,mensaje)
        elif choice == '6' or choice == "actualizar informacion":
            cedula=input("Ingrese la cédula del contacto: ")
            exito,mensaje=update_contact(cedula)
            print(exito,mensaje)
        elif choice == '7' or choice == "salir":
            print("Has salido del menu")
            break
        else:
            print("Opcion invalida intente de nuevo")