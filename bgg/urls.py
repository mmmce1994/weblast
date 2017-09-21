"""bgg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from BonaB import views


router = routers.DefaultRouter()
router.register(r'cryptocurrencies', views.CryptoCurrencyViewSet)
router.register(r'fullnodes', views.FullNodeViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^admin/$', views.dashboard),
    url(r'^$', views.login),
    url(r'^status/', views.status),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/list/', views.list_cc),
    url(r'^logout/', views.logout),
    url(r'^admin/newCC', views.newCC),

]
