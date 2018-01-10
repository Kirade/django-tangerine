from django.test import TestCase
from website.forms import RegisterForm


class RegisterFormTest(TestCase):

    def setUp(self):
        self.form = RegisterForm()

    # def test_username_label(self):
    #     # self.assertTrue(self.form.fields['username'].label == 'username')
    #     max_length = self.form.fields['username'].max_length
    #     self.assertEqual(max_length, 150)
    #
    # def test_password1_label(self):
    #     self.assertTrue(self.form.fields['password1'].label == 'Password')
    #
    # def test_password2_label(self):
    #     self.assertTrue(self.form.fields['password2'].label == 'Password Confirmation')
    #
    # def test_email_label(self):
    #     self.assertTrue(self.form.fields['email'].label == 'Email')
    #
    # def test_full_name_label(self):
    #     self.assertTrue(self.form.fields['full_name'].label == 'Full name')
    #
    # def test_address_label(self):
    #     self.assertTrue(self.form.fields['address'].label == 'Address')
    #
    # def test_phone_number_label(self):
    #     self.assertTrue(self.form.fields['phone_number'].label == 'Phone number')
    #
    # def test_subscribe_label(self):
    #     self.assertTrue(self.form.fields['subscribe'].label == 'Subscribe')