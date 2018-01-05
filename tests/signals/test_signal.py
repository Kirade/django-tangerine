from django.test import TestCase
from django.contrib.auth.models import User

from website.models import Profile


class TestSignal(TestCase):

    def test_create_user_profile(self):
        """
        Test whether user model creation makes connected profile object
        """
        user = User.objects.create(username='test_user')
        profile = Profile.objects.get(user_id=user.id)
        self.assertIsNotNone(profile)

    # def test_product_image_delete(self):
    #     product = Product.objects.create(title='test_title',
    #                                      description='test_desc',
    #                                      image='test_image', )