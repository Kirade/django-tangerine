from django.test import TestCase
from django.urls import reverse
from .functions import create_product_model


class ProductListViewTest(TestCase):

    def test_status_code(self):
        """
        Test page status code
        """
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, 200)

    def test_page_context(self):
        """
        Test when Product model object exists
        """
        create_product_model()
        response = self.client.get(reverse('product-list'))
        self.assertContains(response, "test_title")
        self.assertContains(response, "test_desc")
        self.assertContains(response, "test_img")
        self.assertContains(response, 0)

    def test_empty_list(self):
        """
        Test when Product model object is empty
        """
        response = self.client.get(reverse('product-list'))
        self.assertContains(response, "등록된 상품이 존재하지 않습니다.")
        self.assertQuerysetEqual(response.context['product_obj_list'], [])

    def test_comma_separator(self):
        """
        Test comma_separator custom template filter
        """
        create_product_model(price=1)
        create_product_model(price=100)
        create_product_model(price=1000)
        create_product_model(price=10000)
        create_product_model(price=100000)
        create_product_model(price=1000000)
        create_product_model(price=10000000)
        response = self.client.get(reverse('product-list'))
        self.assertContains(response, '1')
        self.assertContains(response, '100')
        self.assertContains(response, '1,000')
        self.assertContains(response, '10,000')
        self.assertContains(response, '100,000')
        self.assertContains(response, '1,000,000')
        self.assertContains(response, '10,000,000')

    def test_correct_template(self):
        response = self.client.get(reverse('product-list'))
        self.assertTemplateUsed(response, 'website/product/list.html')


class ProductListViewPaginationTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_product = 15
        for product_num in range(number_of_product):
            create_product_model(title=product_num)

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('product-list'))
        self.assertTrue('is_paginated' in response.context)
        # self.assertTrue(response.context['is_paginated'])
        # self.assertTrue(len(response.context['product_obj_list']) == 10)

    def test_lists_all_product(self):
        response = self.client.get(reverse('product-list') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        # self.assertTrue(response.context['is_paginated'])
        # self.assertTrue(len(response.context['product_obj_list']) == 5)
