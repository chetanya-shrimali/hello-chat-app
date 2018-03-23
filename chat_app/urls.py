from django.urls import path
from chat_app import views
from django.urls import path

from chat_app import views

app_name = 'chat_app'
urlpatterns = [
    path('', views.ChatFormView.as_view(), name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]