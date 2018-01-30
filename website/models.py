from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Order(models.Model):
    product = models.CharField(max_length=20)
    count = models.PositiveIntegerField()
    name = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=20)

    def __str__(self):
        return_string = self.name + " 님의 주문 " + str(timezone.now())
        return return_string
