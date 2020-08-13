"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import appname.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', appname.views.main, name='main'),
    path('create', appname.views.create, name='create'),
    path('update/<int:pk>', appname.views.update, name='update'),
    path('delete/<int:pk>', appname.views.delete, name='delete'),
    path('', appname.views.signin, name='signin'),
    path('signup', appname.views.signup, name='signup'),
    path('comment/<int:post_id>', appname.views.comment, name='comment'),
    path('hashtag/<str:hashtag_name>', appname.views.hashtag, name='hashtag'),
    path('like/<int:pk>', appname.views.like, name='like'),
    path('mypage/<int:user_id>', appname.views.mypage, name='mypage'),

    path('', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

