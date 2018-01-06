from django.test import TestCase
from website.models import Profile
from django.contrib.auth.models import User


class ProfileAttributeTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="test_user")

    def setUp(self):
        self.profile = Profile.objects.get(user_id=1)

    def test_user_label(self):
        """
        Test Profile model's field label
        """
        field_label = self.profile._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')
        field_label = self.profile._meta.get_field('address').verbose_name
        self.assertEqual(field_label, 'address')
        field_label = self.profile._meta.get_field('phone_number').verbose_name
        self.assertEqual(field_label, 'phone number')
        field_label = self.profile._meta.get_field('full_name').verbose_name
        self.assertEqual(field_label, 'full name')
        field_label = self.profile._meta.get_field('subscribe').verbose_name
        self.assertEqual(field_label, 'subscribe')

    def test_address_max_length(self):
        """
        Test Profile model's field max_length
        """
        max_length = self.profile._meta.get_field('address').max_length
        self.assertEquals(max_length, 200)
        max_length = self.profile._meta.get_field('phone_number').max_length
        self.assertEquals(max_length, 20)
        max_length = self.profile._meta.get_field('full_name').max_length
        self.assertEquals(max_length, 20)

    def test_string_representation(self):
        """
        __str__ function test for Profile Model
        """
        user_obj = User(username="String Test")
        profile = Profile(user=user_obj)
        self.assertEqual(str(profile), profile.user.username)