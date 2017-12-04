from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^intro/', views.intro, name='intro'),
    url(r'^board/', views.board_list, name='board_list'),
    url(r'^board/detail/(?P<pk>\d+)/$', views.board_detail, name='board_detail'),
    url(r'^board/new/$', views.board_new, name='board_new'),
    url(r'^board/(?P<pk>\d+)/edit/$', views.board_edit, name='board_edit'),
    url(r'^order/', views.order, name='order'),
    url(r'^faq/', views.faq, name='faq'),
]
