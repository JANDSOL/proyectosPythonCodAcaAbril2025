'''
menú en consola que llama a ProductManager para realizar 6 operaciones (1. Crear producto,
2. Leer producto, 3. Actualizar producto,
4. Actualizar múltiples productos, 5. Eliminar producto, 6. Eliminar múltiples productos) y 7. Para salir del menú.

'''

from managers import  product_manager

while True:
    print("==================================")
    print("1. Crear Producto")
    print("2. Leer Producto")
    print("3. Actualizar Producto")
    print("4. Actualizar multiples prodcutos")
    print("5. Eliminar prodcuto")
    print("6. Eliminar todo el inventario")
    print("7. Ver todo el inventario")
    print("8. Salir del Menu")

    choice=input("Elige una opción: ").lower()
    try:
        if choice == '1' or choice == 'crear producto':
            try:
                nombre=input("Ingrese el nombre del producto: ")
                precio=float(input("Ingrese el precio del producto: "))
                stock=int(input("Ingrese el stock del producto: "))
                producto=(product_manager.create(nombre, precio, stock))
                print("Producto creado correctamente:")
                print(producto)
            except Exception as e:
                print(e)
        elif choice == '2' or choice == 'leer producto':
            product_manager.read()
        elif choice == '3' or choice == 'actualizar producto':
            product_manager.update()
        elif choice == '4' or choice == 'actualizar multiples productos':
            product_manager.bulk_update()
        elif choice == '5' or choice == 'eliminar producto':
            product_manager.delete()
        elif choice == '6' or choice == 'eliminar todo el inventario':
            product_manager.bulk_delete()
        elif choice == '7' or choice == 'ver todo el inventario':
            product_manager.ver_iventario()
        elif choice == '8' or choice == 'salir':
            print("Gracias por usar el programa")
            break
        else:
            print("Error, opcion no disponible")
            pass
    except Exception as e:
        print(e)