from django import forms
from django.contrib.auth.models import User

from chat_app.models import Chat


class ChatForm(forms.ModelForm):
    """Provides form for Chat model"""

    class Meta:
        model = Chat
        # fields = '__all__'
        exclude = ['user', 'date']


class LoginForm(forms.Form):
    """Provides form for User model"""

    username = forms.CharField(label='username')
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterForm(forms.ModelForm):
    """Provides form for User model"""
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='confirm_password',
                                       widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']
