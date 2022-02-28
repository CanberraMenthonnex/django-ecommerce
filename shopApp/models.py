from django.db import models

# Create your models here.


class Product(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  price = models.IntegerField()
  quantity = models.IntegerField()
  image = models.CharField(max_length=300)