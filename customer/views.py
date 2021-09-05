from django.http import response
from django.shortcuts import render
import re
from functions.authentication import Auth
from functions.userManager import UserManager
from django.contrib.auth.decorators import login_required

user = UserManager()
auth = Auth()
# Create your views here.

# urlPath = request.META['HTTP_REFERER']
# print("URL", urlPath)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        """Call the Authentication Object"""
        response = auth.userLogin(request, email, password, errorRedirectTo='/customer/', successRedirect='/customer/home/')
        return response
    else:
        return render(request, 'customer/login.html')


def signup(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        mobile = request.POST['mobile']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        """Call the User creation Object"""
        response = user.userRegistration(request, fullname, email, mobile, password1, password2, redirectUrl='/customer/signup/')
        return response
    else:
        return render(request, 'customer/signup.html')


@login_required(login_url='/customer/')
def home(request):
    return render(request, 'customer/home.html')


def logout(request):
    response = auth.logout(request, redirectTo='/customer/')
    return response