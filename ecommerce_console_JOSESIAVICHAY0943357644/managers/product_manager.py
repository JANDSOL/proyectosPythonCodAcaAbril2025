import logging
from models import Producto

logger = logging.getLogger(__name__)

class ProductManager:
    def __init__(self):
        self.productos = []

    def create(self, nombre, precio, stock):
        producto = Producto(nombre, precio, stock)
        self.productos.append(producto)
        logger.info(f"Producto creado: {producto}")
        return producto

    def read(self, producto_id):
        for p in self.productos:
            if p.id == producto_id:
                logger.info(f"Producto consultado: {p}")
                return p
        logger.warning(f"Producto con ID {producto_id} no encontrado.")
        return None

    def update(self, producto_id, nombre=None, precio=None, stock=None):
        producto = self.read(producto_id)
        if producto:
            if nombre: producto.nombre = nombre
            if precio: producto.precio = precio
            if stock: producto.stock = stock
            logger.info(f"Producto actualizado: {producto}")
            return producto
        logger.error(f"No se pudo actualizar el producto con ID {producto_id}")
        return None

    def bulk_update(self, ids, nombre=None, precio=None, stock=None):
        actualizados = []
        for pid in ids:
            prod = self.update(pid, nombre, precio, stock)
            if prod:
                actualizados.append(prod)
        logger.info(f"Productos actualizados masivamente: {actualizados}")
        return actualizados

    def delete(self, producto_id):
        producto = self.read(producto_id)
        if producto:
            self.productos.remove(producto)
            logger.info(f"Producto eliminado: {producto}")
            return True
        logger.error(f"No se pudo eliminar el producto con ID {producto_id}")
        return False

    def bulk_delete(self, ids):
        eliminados = []
        for pid in ids:
            if self.delete(pid):
                eliminados.append(pid)
        logger.info(f"Productos eliminados masivamente: {eliminados}")
        return eliminados
