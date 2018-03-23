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
        chats = Chat.objects.all().order_by('-date')
        return render(request, self.template_name,
                      {'form': form, 'chats': chats})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = self.request.user
            post.save()
            chats = Chat.objects.all().order_by('-date')
            return render(request, self.template_name,
                          {'form': form, 'chats': chats})
        else:
            return render(request, self.template_name, {'form': form})


def login(request):
    return render(request, 'form_login.html')


def register(request):
    return render(request, 'form_register.html')
