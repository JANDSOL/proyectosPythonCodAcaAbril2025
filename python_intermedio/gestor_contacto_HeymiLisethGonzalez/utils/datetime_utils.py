""" Módulo que tendrá funcion de fecha."""
from datetime import datetime

def get_timestamp():
    """ Función para obtener la fecha y hora actual."""
    return datetime.now().strftime("%d/%m/%y %H:%M:%S")


#print(get_timestamp())