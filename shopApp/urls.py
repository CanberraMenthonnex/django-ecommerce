from unicodedata import name
from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'shopApp'

urlpatterns = [
  path('', views.index, name='index'),
  path('<id>', views.detailView, name='detailView'),
  path('update/<id>', views.updateProduct, name='updateView')
]