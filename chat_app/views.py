from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Reached Index!!')


def login(request):
    return HttpResponse('Reached login!!')


def register(request):
    return HttpResponse('Reached register!!')
