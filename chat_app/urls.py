from django.conf.urls import url
from django.urls import path
from chat_app import views


app_name = 'chat_app'
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'register/', views.register, name='register'),
    path(r'login/', views.login, name='login'),
]
