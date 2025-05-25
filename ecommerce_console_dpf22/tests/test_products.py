import unittest
from managers import product_manager
from models import Producto

class TestProductManager(unittest.TestCase):

    def setUp(self):
        product_manager.inventory.clear()

    def test_add_product(self):
        result = product_manager.create("Lapiz", 100, 10)
        self.assertIn("Lapiz", result)
        self.assertEqual(len(product_manager.inventory), 1)

    def test_update_product(self):
        product_manager.create("Cuaderno", 50, 20)
        producto_id = list(product_manager.inventory.keys())[0]
        product_manager.inventory[producto_id].precio = 60
        product_manager.inventory[producto_id].stock = 25
        self.assertEqual(product_manager.inventory[producto_id].precio, 60)
        self.assertEqual(product_manager.inventory[producto_id].stock, 25)

    def test_bulkupdate_product(self):
        product_manager.create("Regla", 40, 5)
        product_manager.create("Compás", 60, 7)
        for producto in product_manager.inventory.values():
            producto.precio = producto.precio * 0.5
        precios = [producto.precio for producto in product_manager.inventory.values()]
        self.assertEqual(precios, [20, 30])

    def test_delete_product(self):
        product_manager.create("Tijeras", 30, 10)
        producto_id = list(product_manager.inventory.keys())[0]
        del product_manager.inventory[producto_id]
        self.assertEqual(len(product_manager.inventory), 0)

    def test_bulkdelete_product(self):
        product_manager.create("Calculadora", 200, 4)
        product_manager.create("Esfero", 20, 50)
        product_manager.inventory.clear()
        self.assertEqual(len(product_manager.inventory), 0)

if __name__ == '__main__':
    unittest.main()
