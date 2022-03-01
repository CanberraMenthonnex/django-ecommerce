from django.shortcuts import render
from .models import Product

# Create your views here.

def index(request):
  context ={}
  # add the dictionary during initialization
  context["dataset"] = Product.objects.all()
        
  return render(request, "shopApp/index.html", context)


def detailView(request, id):
  context= {}
  context["data"] = Product.objects.get(id = id)
         
  return render(request, "shopApp/productDetail.html", context)