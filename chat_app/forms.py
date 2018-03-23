from django import forms

from chat_app.models import Chat


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = '__all__'
        # exclude = ['user', 'date']
