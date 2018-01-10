from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class BoardCreateViewTest(TestCase):

    def setUp(self):
        User.objects.create_user(username="test_user", password="1234")

    def check_same_user(self):
        """
        Test author name is same as logged in user
        """
        self.client.login(username='test_user', password='1234')
        response = self.client.get(reverse('board-new'))
        self.assertEqual(str(response.context['user']), 'test_user')
