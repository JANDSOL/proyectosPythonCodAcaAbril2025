from models import Producto
from logging_config import setup_logger

logger = setup_logger()

class ProductManager:
    def __init__(self):
        self.productos = {}

    def create(self, nombre, precio, stock):
        producto = Producto(nombre, precio, stock)
        self.productos[producto.id] = producto
        logger.info(f"Producto creado: {vars(producto)}")
        return producto.id

    def read(self, id_):
        producto = self.productos.get(id_)
        if producto:
            return vars(producto)
        logger.error(f"Producto no encontrado: ID {id_}")
        return None

    def update(self, id_, nombre=None, precio=None, stock=None):
        producto = self.productos.get(id_)
        if not producto:
            logger.error(f"No se puede actualizar, producto no encontrado: ID {id_}")
            return False
        if nombre: producto.nombre = nombre
        if precio: producto.precio = precio
        if stock: producto.stock = stock
        logger.info(f"Producto actualizado: {vars(producto)}")
        return True

    def bulk_update(self, updates):
        for id_, cambios in updates.items():
            self.update(id_, **cambios)

    def delete(self, id_):
        if self.productos.pop(id_, None):
            logger.info(f"Producto eliminado: ID {id_}")
            return True
        logger.error(f"No se puede eliminar, producto no encontrado: ID {id_}")
        return False

    def bulk_delete(self, ids):
        for id_ in ids:
            self.delete(id_)
