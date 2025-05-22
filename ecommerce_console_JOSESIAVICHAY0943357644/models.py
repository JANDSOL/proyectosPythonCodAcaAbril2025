class Producto:
    _id_counter = 1

    def __init__(self, nombre, precio, stock):
        self.id = Producto._id_counter
        Producto._id_counter += 1
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
