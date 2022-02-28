from unicodedata import name
from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'firstApp'

urlpatterns = [
  path('', views.index, name='index'),
]