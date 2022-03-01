from unicodedata import name
from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'socketApp'

urlpatterns = [
  path('', views.index, name='index'),
  path('chatRoom/<room_name>', views.chat, name='chat'),
]