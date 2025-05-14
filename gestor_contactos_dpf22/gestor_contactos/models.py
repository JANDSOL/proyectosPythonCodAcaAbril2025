# from utils import datetime_utils
contacts=[
    
]
def exists(cedula):
    for contacto in contacts:
        if contacto['cedula'] == cedula:
            return True
    return False
    
def get_all():
    for contacto in contacts:
        print('=============Contacto================')
        for clave,valor in contacto.items():
            print (f"{clave}:{valor}")
            return True, "Completado"
    return False, "No se encontraron contactos"