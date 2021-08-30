from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from app.models import UserModel


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def signup(request):
    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')


def loginV(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = UserModel()
        user.user = email
        user.password = password
        user.save(user)
        print("Email: "+email+" Password "+password, end="\n")

        return HttpResponse("Hello World")
