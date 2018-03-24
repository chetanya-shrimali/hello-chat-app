from django.urls import path

from chat_app import views

app_name = 'chat_app'
urlpatterns = [
    # Handles route to '/', home/index page
    # 'register/', register page
    # 'login/', login page
    # 'logout/' logout
    path('', views.ChatFormView.as_view(), name='index'),
    path('register/', views.RegisterFormView.as_view(), name='register'),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('logout/', views.signout, name='logout')
]