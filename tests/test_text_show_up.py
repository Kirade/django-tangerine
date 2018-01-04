from django.test import TestCase, Client
from django.contrib.auth.models import User

from website.models import Board


class ShowUpTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username="test_user")

    def test_board_show_up(self):
        Board.objects.create(title="test", text="text", writer=self.user)
        response = self.client.get('/board/')
        self.assertContains(response, "test")
        self.assertContains(response, "text")
        self.assertContains(response, "test_user")

"""
PAGE SHOW UP 추가
"""