from django.test import TestCase

from website.models import Product


class ProductAttributeTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Product.objects.create(title="test")

    def setUp(self):
        self.product = Product.objects.get(id=1)

    def test_field_label(self):
        """
        Test Product model's field label
        """
        field_label = self.product._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')
        field_label = self.product._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')
        field_label = self.product._meta.get_field('image').verbose_name
        self.assertEqual(field_label, 'image')
        field_label = self.product._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')
        field_label = self.product._meta.get_field('stock_left').verbose_name
        self.assertEqual(field_label, 'stock left')

    def test_field_max_length(self):
        """
        Test Product model's field max_length
        """
        max_length = self.product._meta.get_field('title').max_length
        self.assertEqual(max_length, 50)

    def test_string_representation(self):
        """
        __str__ function test for Product Model
        """
        product = Product(title="String Test")
        self.assertEqual(str(product), product.title)