from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import Product, Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    instance.profile.save()


@receiver(pre_delete, sender=Product)
def delete_product_image(sender, instance, using, **kwargs):
    instance.image.delete()