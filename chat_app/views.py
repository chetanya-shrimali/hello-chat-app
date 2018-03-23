from django.shortcuts import render
from django.views import View

from chat_app.forms import ChatForm
from chat_app.models import Chat


def index(request):
    chats = Chat.objects.all()
    return render(request, 'index.html', {'chats': chats})


class ChatFormView(View):
    form_class = ChatForm
    template_name = 'index.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        pass


def login(request):
    return render(request, 'form_login.html')


def register(request):
    return render(request, 'form_register.html')
