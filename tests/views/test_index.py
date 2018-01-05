from django.test import TestCase
from django.urls import reverse


class IndexViewTest(TestCase):

    def test_status_code(self):
        """
        Test page status code
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
