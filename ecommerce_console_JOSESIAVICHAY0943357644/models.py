class Producto:
    _id_counter = 1

    def __init__(self, nombre, precio, stock):
        self.id = Producto._id_counter
        Producto._id_counter += 1
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        
    def __repr__(self):
        return f"<Producto id={self.id}, nombre={self.nombre}, precio={self.precio}, stock={self.stock}>"
