from django.test import TestCase
from django.urls import reverse

from .functions import create_product_model


class ProductDetailViewTest(TestCase):

    def setUp(self):
        self.product = create_product_model()
        self.response = self.client.get(reverse('product-detail', args=(self.product.id,)))

    def test_status_code(self):
        """
        Test page status code
        """

        self.assertEqual(self.response.status_code, 200)

    def test_page_context(self):
        """
        Test when Product model object exists
        """
        self.assertContains(self.response, "test_title")
        self.assertContains(self.response, "test_desc")
        self.assertContains(self.response, "test_img")
        self.assertContains(self.response, 0)
