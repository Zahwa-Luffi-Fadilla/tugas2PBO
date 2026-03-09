import unittest
from product import Product

class TestProduct(unittest.TestCase):

    def test_tambah_stok(self):
        p = Product(1, "Laptop", 10000000, 5)
        p.tambah_stok(3)
        self.assertEqual(p.get_stok(), 8)

    def test_kurangi_stok(self):
        p = Product(1, "Laptop", 10000000, 5)
        p.kurangi_stok(2)
        self.assertEqual(p.get_stok(), 3)

    def test_diskon(self):
        p = Product(1, "Laptop", 10000000, 5)
        harga_diskon = p.hitung_diskon(10)
        self.assertEqual(harga_diskon, 9000000)

    def test_set_harga(self):
        p = Product(1, "Laptop", 10000000, 5)
        p.set_harga(8000000)
        self.assertEqual(p.get_harga(), 8000000)

if __name__ == "__main__":
    unittest.main()