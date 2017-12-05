'''
Django 2.0 changes

 path : 정규식 표현이 아닌 url resolver
 re_path : 기존의 정규식으로 표현하는 url() 메소드의 기능을 수행한다.
'''

from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('registration/login/', auth_views.login, name='login', kwargs={'template_name': 'website/registration/login.html', }),
    path('registration/logout/', auth_views.logout, name='logout', kwargs={'next_page': settings.LOGOUT_REDIRECT_URL, }),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
