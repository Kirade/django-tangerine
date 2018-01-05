from django.test import TestCase

from website.models import Product


class ProductAttributeTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Product.objects.create(title="test")

    def setUp(self):
        self.product = Product.objects.get(id=1)

    def test_title_label(self):
        field_label = self.product._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_description_label(self):
        field_label = self.product._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_image_label(self):
        field_label = self.product._meta.get_field('image').verbose_name
        self.assertEqual(field_label, 'image')

    def test_price_label(self):
        field_label = self.product._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_stock_left_label(self):
        field_label = self.product._meta.get_field('stock_left').verbose_name
        self.assertEqual(field_label, 'stock left')

    def test_title_max_length(self):
        max_length = self.product._meta.get_field('title').max_length
        self.assertEqual(max_length, 50)

    def test_string_representation(self):
        """
        __str__ function test for Product Model
        """
        product = Product(title="String Test")
        self.assertEqual(str(product), product.title)