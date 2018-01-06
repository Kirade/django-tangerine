from django.test import TestCase
from django.urls import reverse

from .functions import create_product_model


class ProductDetailViewTest(TestCase):

    def setUp(self):
        product = create_product_model()
        self.response = self.client.get(reverse('product-detail', args=(product.id,)))

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


"""
Test 해야할 것들

바로 구매 혹은, 장바구니 선택했을때 이동할 페이지들 만든 후

해당 페이지로 리다이렉트가 정상적으로 진행되는지
-> 로그인시 정상진행
-> 미 로그인시 로그인 페이지 진입 후 로그인 성공하면 해당페이지 리다이렉션
"""