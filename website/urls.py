from django.urls import path
from django.contrib.auth import views as auth_views
from tangerine import settings
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('order-new/',
         views.order_new,
         name='order-new'),

]
