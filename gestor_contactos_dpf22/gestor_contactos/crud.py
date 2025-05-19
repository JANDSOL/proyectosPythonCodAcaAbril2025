from gestor_contactos.models import contacts
from utils.datetime_utils import get_timestamp
# from utils import datetime_utils

def add_contacts(cedula,nombre,apellido,celular)->tuple[bool,str]:
    for contacto in contacts:
        if contacto['cedula'] == cedula:
            return False, "Ya existe un contacto con esa cédula."
        
    contacts_nuevos={
        'cedula':cedula,
        'nombre':nombre,
        'apellido':apellido,
        'celular':celular,
        'fecha_creacion':get_timestamp(),
        }
    
    contacts.append(contacts_nuevos)
    return True, f"Contacto agregado exitosamente: {contacts_nuevos}"
    

def get_contact(cedula)->tuple[bool,str]:
    for contacto in contacts:
        if contacto['cedula'] == cedula:
            print("Información del contacto:")
            print(f"Cédula: {contacto['cedula']}")
            print(f"Nombre: {contacto['nombre']}")
            print(f"Apellido: {contacto['apellido']}")
            print(f"Celular: {contacto['celular']}")
            return True, "Completado"
    return False,f"No se encontró un contacto con esa cédula."


def update_contact(cedula,nombre=None,celular=None,apellido=None)->tuple[bool,str]:
    for contacto in contacts:
        if contacto['cedula'] == cedula:
            nuevo_valor=input("Ingrese el nuevo valor: ")
            contacto['cedula'] = nuevo_valor
            print(f"Contacto Actualizado:")
            print("Información del contacto:")
            print(f"Cédula: {contacto['cedula']}")
            print(f"Nombre: {contacto['nombre']}")
            print(f"Apellido: {contacto['apellido']}")
            print(f"Celular: {contacto['celular']}")
            return True, "Completado"
    return False, "No se encontro un contacto con esa cédula"

def delete_contact(cedula) ->tuple[bool,str]:
    for contacto in contacts:
        if contacto['cedula'] == cedula:
            contacts.remove(contacto)
            return True, "Contacto Eliminado"
    return False,"No se encontro un contacto con esa cédula"

