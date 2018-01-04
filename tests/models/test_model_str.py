from django.test import TestCase
from django.contrib.auth.models import User

from website.models import Board, Profile, Product


class BoardModelTest(TestCase):

    def test_string_representation(self):
        """
        __str__ function test for Board Model
        """
        board = Board(title="String Test")
        self.assertEqual(str(board), board.title)


class ProfileModelTest(TestCase):

    def test_string_representation(self):
        """
        __str__ function test for Profile Model
        """
        user_obj = User(username="String Test")
        profile = Profile(user=user_obj)
        self.assertEqual(str(profile), profile.user.username)


class ProductModelTest(TestCase):

    def test_string_representation(self):
        """
        __str__ function test for Product Model
        """
        product = Product(title="String Test")
        self.assertEqual(str(product), product.title)