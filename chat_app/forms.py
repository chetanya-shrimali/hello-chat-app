from django import forms
from django.contrib.auth.models import User

from chat_app.models import Chat


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        # fields = '__all__'
        exclude = ['user', 'date']


class LoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
