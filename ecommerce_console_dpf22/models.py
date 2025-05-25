#- models.py: define la clase Producto con un atributo id que será autoincremental (que empiece con 1), nombre, precio y stock.
class Producto:
    id=1

    def __init__(self, nombre,precio,stock):
        self.id = Producto.id
        Producto.id += 1
        self.nombre=nombre
        self.precio=precio
        self.stock=stock

    def info_producto(self):
        return f" Id: {self.id}\n Producto: {self.nombre}\n precio: ${self.precio}\n Stock: {self.stock} unidades"

