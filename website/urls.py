from django.urls import path
from django.contrib.auth import views as auth_views
from tangerine import settings
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('intro/', views.IntroView.as_view(), name='intro'),
    path('product/', views.ProductListView.as_view(), name='product-list'),
    path('product/detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('board/', views.BoardListView.as_view(), name='board-list'),
    path('board/detail/<int:pk>/', views.BoardDetailView.as_view(), name='board-detail'),
    path('board/new/', views.BoardCreateView.as_view(), name='board-new'),
    path('board/<int:pk>/edit/', views.BoardUpdateView.as_view(), name='board-edit'),
    path('order/', views.OrderView.as_view(), name='order'),
    path('faq/', views.FaqView.as_view(), name='faq'),
    path('register/terms/', views.RegisterTermsView.as_view(), name='register-terms'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('registration/login/',
         auth_views.login,
         name='login',
         kwargs={'template_name': 'website/registration/login.html', }),
    path('registration/logout/',
         auth_views.logout,
         name='logout',
         kwargs={'next_page': settings.LOGOUT_REDIRECT_URL, }),
    path('registration/<int:pk>/mypage/',
         views.UserChangeView.as_view(),
         name='mypage', ),
    path('registration/changesuccess/',
         views.ChangeSuccessView.as_view(),
         name='change_success'),
]
