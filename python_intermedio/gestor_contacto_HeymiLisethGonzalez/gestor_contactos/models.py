""" Modulo almacena los datos de los contactos. """
import datetime


#contacts = {"nombres":"Heymi Liseth", "cedula": "123", "celular":"0981990422", "fecha": datetime.date.today()}

# Diccionario para almacenar los contactos.
contacts = {}

def exists(cedula):
    """ Función para saber si la cédula ya existe. """
    return cedula in contacts

def get_all():
    """ Función para mostrar todos los items del dicc """
    return contacts

if __name__ == "__main__":
    print(contacts)
    print(exists('1208928411'))
    print(get_all())