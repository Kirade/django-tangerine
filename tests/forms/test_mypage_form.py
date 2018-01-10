from django.test import TestCase
from website.forms import MyPageForm


class MyPageFormTest(TestCase):

    def setUp(self):
        self.form = MyPageForm()

    def test_form_label(self):
        """
        Test form label value
        """
        # self.assertTrue(self.form.fields['username'].label)
        # self.assertTrue(self.form.fields['email'].label == 'Email Address')

