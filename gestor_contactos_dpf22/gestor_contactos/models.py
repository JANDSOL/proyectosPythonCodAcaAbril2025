# from utils import datetime_utils
contacts=[
    
]
def exists(cedula)->tuple[bool,str]:
    for contacto in contacts:
        if contacto['cedula'] == cedula:
            return True, "El contacto existe"
    return False, "El contacto no existe"
    
def get_all()->tuple[bool,str]:
    for contacto in contacts:
        print('=============Contacto================')
        for clave,valor in contacto.items():
            print (f"{clave}:{valor}")
        return True, "Contacto Mostrado"
    return False,"No hay contactos"