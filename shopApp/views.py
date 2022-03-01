from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Product
from .form import ProductForm

# Create your views here.

def index(request):
  context ={}
  # add the dictionary during initialization
  context["dataset"] = Product.objects.filter(quantity__gte = 1)

  return render(request, "shopApp/index.html", context)


def detailView(request, id):
  context= {}
  context["data"] = Product.objects.get(id = id)

  return render(request, "shopApp/productDetail.html", context)


def updateProduct(request, id):

  obj = Product.objects.get(id = id)

  if(obj.quantity > 0):
    obj.quantity -= 1
    obj.save()

    if(obj.quantity == 0):
      return HttpResponseRedirect("../")
    else:
      return HttpResponseRedirect(("../" + str(id)))
  else:
    return HttpResponseRedirect("../")