from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]