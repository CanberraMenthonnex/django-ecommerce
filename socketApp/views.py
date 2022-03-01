from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    if request.method == "POST":
        room_code = request.POST.get("room_code")
        char_choice = request.POST.get("character_choice")
        return redirect(
            'socketApp' 
            %(room_code, char_choice)
        )
    return render(request, "socketApp/index.html")
  

def chat(request, room_name):
    context = {
        "char_choice": choice, 
        "room_code": room_name
    }
    return render(request, "chat.html", context)