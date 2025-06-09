from ecommerce_console_JOSESIAVICHAY0943357644.models import Producto
import pytest
from managers.product_manager import ProductManager

@pytest.fixture(autouse=True)
def reset_id_counter():
    Producto._id_counter = 1

@pytest.fixture
def gestor():
    return ProductManager()

def test_crear_producto(gestor):
    producto = gestor.create("Teclado", 50.0, 10)
    assert producto.nombre == "Teclado"
    assert producto.precio == 50.0
    assert producto.stock == 10

def test_leer_producto(gestor):
    producto = gestor.create("Mouse", 20.0, 5)
    resultado = gestor.read(producto.id)
    assert resultado == producto

def test_actualizar_producto(gestor):
    producto = gestor.create("Pantalla", 100.0, 7)
    gestor.update(producto.id, precio=120.0)
    assert producto.precio == 120.0

def test_eliminar_producto(gestor):
    producto = gestor.create("Cable", 10.0, 50)
    resultado = gestor.delete(producto.id)
    assert resultado is True
    assert gestor.read(producto.id) is None

def test_bulk_update(gestor):
    p1 = gestor.create("Prod1", 10, 1)
    p2 = gestor.create("Prod2", 20, 2)
    gestor.bulk_update([p1.id, p2.id], stock=100)
    assert p1.stock == 100
    assert p2.stock == 100

def test_bulk_delete(gestor):
    p1 = gestor.create("Prod3", 30, 3)
    p2 = gestor.create("Prod4", 40, 4)
    resultado = gestor.bulk_delete([p1.id, p2.id])
    assert p1.id in resultado
    assert p2.id in resultado
