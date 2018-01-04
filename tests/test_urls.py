from django.test import TestCase


class UrlAccessTests(TestCase):

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    """
    Add More Url Access Test Cases!
    """