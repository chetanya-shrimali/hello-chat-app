from django.shortcuts import render
from django.views import View

from chat_app.forms import ChatForm, LoginForm, RegisterForm
from chat_app.models import Chat


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


class LoginFormView(View):
    form_class = LoginForm
    template_name = 'form_login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name,
                      {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = self.request.user
            post.save()
            return render(request, self.template_name,
                          {'form': form})
        else:
            return render(request, self.template_name, {'form': form})


class RegisterFormView(View):
    form_class = RegisterForm
    template_name = 'form_register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name,
                      {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = self.request.user
            post.save()
            return render(request, self.template_name,
                          {'form': form})
        else:
            return render(request, self.template_name, {'form': form})
