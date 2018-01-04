from django.test import TestCase
from django.contrib.auth.models import User

from website.models import Profile
from website.forms import RegisterForm



class ProfileTestCase(TestCase):
    """
    Create User model instance to test whether Profile model attribute 'user'
    references User model properly or not.


    """
    def setUp(self):
        user_obj = User.objects.create_user('test_id', 'test@email', 'testpass')
        Profile(user=user_obj)

    def test_create_profile(self):
        user = User.objects.get(username='test_id')
        profile = Profile.objects.get(user_id=user.id)
        self.assertEqual(user, profile.user)
        self.assertEqual(user.username, profile.user.username)
        self.assertEqual(user.password, profile.user.password)
        self.assertEqual(user.email, profile.user.email)
