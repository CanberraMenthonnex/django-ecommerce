from unicodedata import name
from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'firstApp'

urlpatterns = [
  path('', views.index, name='index'),
  path('createQuestion/', views.formView, name='formView'),
  path('listQuestion/', views.listView, name='listView'),
  path('updateQuestion/<id>', views.updateView, name='updateView'),
  path('deleteQuestion/<id>', views.deleteView, name='deleteView'),
]