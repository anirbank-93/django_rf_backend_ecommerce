from django.test import TestCase
from datetime import datetime

from product.models import Product, ProductCategory

class ProductModelTest(TestCase):
    def test_create_product(self):
        # Create a category instance
        category = ProductCategory.objects.create(name="Test Category")

        # Now create the product with the category instance
        name = "Test Product 1"
        description = "This is the first test product created..."

        product = Product.objects.create(name=name,description=description,category=category)

        self.assertEqual(product.name, name)
        self.assertEqual(product.description, description)
        self.assertIsNotNone(product.inventory_count)
        self.assertIsInstance(product.inventory_count, int)
        self.assertIsNotNone(product.created_at)
        self.assertIsInstance(product.created_at, datetime)
        self.assertIsNotNone(product.updated_at)
        self.assertIsInstance(product.updated_at, datetime)
        self.assertEqual(product.category, category)