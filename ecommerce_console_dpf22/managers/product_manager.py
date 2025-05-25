#- product_manager.py: implementa los de métodos create, read, update, bulk_update 
# (actualización masiva), delete y bulk_delete (eliminación masiva), con logging.
from models import Producto

inventory={}

def create(nombre,precio,stock):
    producto = Producto(nombre, precio, stock)
    inventory[producto.id] = producto
    return Producto.info_producto(producto)

def read():
    try:
        choice = int(input("Introduce el Id del producto del que quieres información: "))
    except ValueError:
        return "Por favor, introduce un número válido."

    if choice in inventory:
        producto = inventory[choice]
        print(Producto.info_producto(producto)) 
    else:
        print("Id no encontrado.")

def update():
    question_id=int(input("Introduce el Id del producto que quieres actualizar su información: "))
    if question_id in inventory:
        producto = inventory[question_id]

        nuevo_precio = float(input("Nuevo precio: "))
        nuevo_stock = int(input("Nuevo stock: "))       

        producto.precio=nuevo_precio
        producto.stock=nuevo_stock

        print(producto.info_producto())

        return ("Producto actualizado correctamente.")
    else:
        print ("Producto no encontrado.")
        return

def bulk_update():
    try:
        descuento=int(input("Porcentaje de descuento que quieres colocar sobre los productos: "))
    except ValueError:
        return "Introduce un número válido"
    
    for producto in inventory.values():
        producto.precio = producto.precio * (1 - descuento / 100)
    return f"El descuento del {descuento}% ha sido aplicado en todos los productos"

def delete():
    question_id=int(input("Digita el numero de Id del producto que quieres eliminar: "))
    if question_id in inventory:
        del inventory[question_id]
        return f"El producto ha sido eliminado"
    else:
        return f"No existe el id ingresado"

def bulk_delete():
    choice=input("Escribe 'De Acuerdo' si Estas seguro de querer borrar todo el contenido del inventario? ")
    if choice == "De Acuerdo":
        return inventory.clear()
    else:
        return ("El inventario se mantiene igual")

def ver_iventario():
    if not inventory:
        print("El inventario está vacío.")
        return

    for producto in inventory.values():
        print(producto.info_producto())
        print("-" * 20)