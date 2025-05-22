import pytest
from managers.product_manager import ProductManager

def test_create_and_read():
    pm = ProductManager()
    id_ = pm.create("Producto1", 10.0, 5)
    producto = pm.read(id_)
    assert producto["nombre"] == "Producto1"

def test_update():
    pm = ProductManager()
    id_ = pm.create("Producto2", 20.0, 3)
    result = pm.update(id_, precio=25.0)
    assert result
    assert pm.read(id_)["precio"] == 25.0

def test_delete():
    pm = ProductManager()
    id_ = pm.create("Producto3", 30.0, 7)
    assert pm.delete(id_)
    assert pm.read(id_) is None
