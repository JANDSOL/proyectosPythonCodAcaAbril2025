from gestor_contactos.models import contacts
from utils.datetime_utils import get_timestamp
# from utils import datetime_utils

def add_contacts(cedula,nombre,apellido,celular):
    for contacto in contacts:
        if contacto['cedula'] == cedula:
            print("Ya existe un contacto con esa cédula.")
            return
    contacts_nuevos={
        'cedula':cedula,
        'nombre':nombre,
        'apellido':apellido,
        'celular':celular,
        'fecha_creacion':get_timestamp(),
        }
    contacts.append(contacts_nuevos)
    print(f"Contacto agregado exitosamente: {contacts_nuevos}")

def get_contact(cedula):
    for contacto in contacts:
        if contacto['cedula'] == cedula:
            print("Información del contacto:")
            print(f"Cédula: {contacto['cedula']}")
            print(f"Nombre: {contacto['nombre']}")
            print(f"Apellido: {contacto['apellido']}")
            print(f"Celular: {contacto['celular']}")
            return (True, "Completado")
    print("No se encontró un contacto con esa cédula.")

def update_contact(cedula,nombre=None,celular=None,apellido=None):
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
            return (True, "Completado")
    print("No se encontro un contacto con esa cédula")

def delete_contact(cedula):
    for contacto in contacts:
        if contacto['cedula'] == cedula:
            contacts.remove(contacto)
            return
    print("No se encontro un contacto con esa cédula")
