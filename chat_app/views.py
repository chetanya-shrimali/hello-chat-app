from django.shortcuts import render

from chat_app.models import Chat


def index(request):
    chats = Chat.objects.all()
    return render(request, 'index.html', {'chats':chats})


def login(request):
    return render(request, 'form_login.html')


def register(request):
    return render(request, 'form_register.html')
