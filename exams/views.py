from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Приложение exams работает!</h1>")