""" Módulo contiene funciones de CRUD"""
from .models import exists, get_all, contacts
from utils.datetime_utils import get_timestamp

def add_contact(cedula, nombres, celular):
    if exists(cedula):
        return(False, "Existe un contacto con esa cédula.")
    contacts[cedula] = {
        "nombres" : nombres,
        "celular" : celular,
        "cedula" : cedula,
        "fecha" : get_timestamp()
    }
    return (True, "¡Agregado con éxito!")

def get_contact(cedula):
    if not exists(cedula):
        return (False, "Error: El contacto no existe.")
    # print(contacts[cedula])
    print("\nDato encontrado: ")
    for clave, valor in contacts[cedula].items():
        print(f"{clave} -> {valor}")
    return (True, "\nExito: Contacto encontrado")

def update_contact(cedula, nombres=None, celular=None):
    if not exists(cedula):
        return (False, "Error: El contacto no existe.")
    if nombres:
        contacts[cedula]["nombres"] = nombres
    if celular:
        contacts[cedula]["celular"] = celular
    return (True, "¡Modificado con éxito!")

def delete_contact(cedula):
    if not exists(cedula):
        return (False, "Error: No existe el contacto para eliminar.")
    del contacts[cedula]
    return (True, "¡Eliminado con éxito.!")

if __name__ == '__main__':
    print(f"\nDiccionario inicial: {contacts}")
    print(f"\nAgregar: {add_contact('0123456789', 'Liss', '0999999999')}")
    print(f"\nBuscar: {get_contact('0123456789')}")
    print(f"\nModificar: {update_contact('0123456789', 'Heymi Liseth')} ")
    #print(delete_contact("0123456789"))
    print("Diccionario actual: ", contacts)
