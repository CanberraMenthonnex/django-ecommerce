from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, response, Http404, HttpResponseRedirect
from .models import Question
from .form import QuestionForm

# Create your views here.


def index(request):
  return render(request, 'firstApp/index.html')

def formView(request):
  context = {}

  form = QuestionForm(request.POST or None)
  if form.is_valid():
    form.save()
  context['form']= form
  return render(request, 'firstApp/formView.html',)


def listView(request):
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Question.objects.all()
         
    return render(request, "firstApp/listView.html", context)

def updateView(request, id):

    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Question, id = id)
 
    # pass the object as instance in form
    form = QuestionForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("../listQuestion")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "firstApp/updateView.html", context)


def deleteView(request,id):

  context ={}

  obj = get_object_or_404(Question, id = id)

  if request.method =="POST":
    # delete object
    obj.delete()
    # after deleting redirect to
    # home page
    return HttpResponseRedirect("../listQuestion")

  return render(request, "firstApp/deleteView.html", context)