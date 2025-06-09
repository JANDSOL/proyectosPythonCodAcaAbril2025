from managers.product_manager import ProductManager

pm = ProductManager()

def menu():
    while True:
        print("\n1. Crear producto")
        print("2. Leer producto")
        print("3. Actualizar producto")
        print("4. Actualización masiva")
        print("5. Eliminar producto")
        print("6. Eliminación masiva")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))
            id_ = pm.create(nombre, precio, stock)
            print(f"Producto creado con ID: {id_}")
        elif opcion == "2":
            id_ = int(input("ID del producto: "))
            print(pm.read(id_))
        elif opcion == "3":
            id_ = int(input("ID del producto: "))
            nombre = input("Nuevo nombre (enter para omitir): ") or None
            precio = input("Nuevo precio (enter para omitir): ")
            precio = float(precio) if precio else None
            stock = input("Nuevo stock (enter para omitir): ")
            stock = int(stock) if stock else None
            pm.update(id_, nombre, precio, stock)
        elif opcion == "4":
            updates = {
                1: {"precio": 99.9},
                2: {"stock": 100}
            }
            pm.bulk_update(updates)
        elif opcion == "5":
            id_ = int(input("ID a eliminar: "))
            pm.delete(id_)
        elif opcion == "6":
            ids = input("IDs a eliminar separados por coma: ").split(",")
            ids = [int(i) for i in ids]
            pm.bulk_delete(ids)
        elif opcion == "7":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()