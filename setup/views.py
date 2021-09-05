from django.shortcuts import render
from django.urls import resolve
from django.conf import settings


def index(request):
    return render(request, 'landing/landing.html')