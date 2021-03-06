"""forms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from todo import views as todo_views
from accounts import views as account_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', todo_views.index, name = 'index'),
    url(r'^login', account_views.login, name='login'),
    url(r'^logout', account_views.logout, name='logout'),
    url(r'^todo/new/', todo_views.new_todo_item, name = 'new_todo'),
    url(r'^register/$', account_views.register, name = 'register'),
]
