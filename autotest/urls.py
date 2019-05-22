"""autotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from apitest import views #加入引用
from product import proviews
from bug import bugviews
from set import setviews
from apptest import appviews
from webtest import webviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test), #加入关联路径及函数
    path('login/', views.login),
    path('home/',views.home),    #进入home
    path('logout/', views.logout),
    path('product_manage/',proviews.product_manage),
    path('apis_manage/', views.apis_manage),
    path('apitest_manage/', views.apitest_manage),
    path('apistep_manage/', views.apistep_manage,name='apistep_manage'),
    path('bug_manage/', bugviews.bug_manage),
    path('set_manage/',setviews.set_manage),
    path('user/', setviews.set_user),
    path('appcase_manage/', appviews.appcase_manage),
    path('appcasestep_manage/', appviews.appcasestep_manage,name='appcasestep_manage'),
    path('webcase_manage/', webviews.webcase_manage),
    path('webcasestep_manage/', webviews.webcasestep_manage,name='webcasestep_manage'),
    path ('test_report/', views.test_report),
    path('apptest_report/', appviews.apptest_report),
    path('left/', views.left),
    path ('apisearch/', views.apisearch),
    path ('setsearch/', setviews.setsearch),
    path ('productsearch/', proviews.productsearch),
    path ('apissearch/', views.apissearch),
    path('apistepsearch/', views.apistepsearch),
    path ('bugsearch/', bugviews.bugsearch),
    path('appsearch/', appviews.appsearch),
    path('appstepsearch/', appviews.appstepsearch),
    path('websearch/', webviews.websearch),
    path('webstepsearch/', webviews.webstepsearch),
    path ('usersearch/', setviews.usersearch),
    path ('welcome/', views.welcome),



]
