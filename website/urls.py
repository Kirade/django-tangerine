from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('intro/', views.IntroView.as_view(), name='intro'),
    path('product/', views.ProductListView.as_view(), name='product-list'),
    path('board/', views.BoardListView.as_view(), name='board-list'),
    path('board/detail/<int:pk>/', views.BoardDetailView.as_view(), name='board-detail'),
    path('board/new/', views.board_new, name='board-new'),
    path('board/<int:pk>/edit/', views.board_edit, name='board-edit'),
    path('order/', views.order, name='order'),
    path('faq/', views.faq, name='faq'),
]
