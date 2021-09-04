from django.shortcuts import render
from django.urls import resolve
from django.conf import settings


def login(request):
    return render(request, 'customer/login.html')


def signup(request):
    urlPath = request.META['HTTP_REFERER']
    current_url = resolve(request.path_info).url_name
    print("URL", urlPath)
    print(current_url)
    return render(request, 'customer/signup.html')