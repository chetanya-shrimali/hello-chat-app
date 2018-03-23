from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'form_login.html')


def register(request):
    return render(request, 'form_register.html')
