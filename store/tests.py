from django.test import TestCase
from .models import Product

class ProductTestCase(TestCase):
    def test_create_product(self):
        product = Product.objects.create(name="Test", description="desc", price=99.99)
        self.assertEqual(product.name, "Test")

