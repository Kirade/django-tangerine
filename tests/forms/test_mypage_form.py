from django.test import TestCase
from website.forms import MyPageForm


class MyPageFormTest(TestCase):

    def setUp(self):
        self.form = MyPageForm()
