from gestor_contactos.crud import add_contact, get_contact, update_contact, delete_contact
from gestor_contactos.models import get_all

def show_menu():
    print("\n--- Gestor de Contactos ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Ver todos")
    print("6. Salir")

def run():
    while True:
        show_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            cedula = input("Cédula: ")
            nombres = input("Nombres: ")
            celular = input("Celular: ")
            ok, msg = add_contact(cedula, nombres, celular)
            print(msg)

        elif opcion == "2":
            cedula = input("Cédula: ")
            ok, result = get_contact(cedula)
            print(result if ok else f"Error: {result}")

        elif opcion == "3":
            cedula = input("Cédula: ")
            nombres = input("Nuevos nombres (Enter para omitir): ")
            celular = input("Nuevo celular (Enter para omitir): ")
            nombres = nombres if nombres else None
            celular = celular if celular else None
            ok, msg = update_contact(cedula, nombres, celular)
            print(msg)

        elif opcion == "4":
            cedula = input("Cédula: ")
            ok, msg = delete_contact(cedula)
            print(msg)

        elif opcion == "5":
            for cedula, datos in get_all():
                print(f"{cedula}: {datos}")
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")
