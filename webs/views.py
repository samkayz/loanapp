from django.contrib import messages
from webs.models import EmailConfig
from django.http import response
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.urls import resolvers
from django.conf import settings
from functions.authentication import Auth
from django.contrib.auth.decorators import permission_required
from functions.decorator import *
from django.template.loader import render_to_string
from functions.emailBackend import EmailBackEnd

auth = Auth()
email = EmailBackEnd()

# Create your views here.


def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        """Call the Authentication Class"""
        response = auth.userLogin(request, email, password, errorRedirectTo='/webs/', successRedirect='/webs/home/')
        return response
    else:
        return render(request, 'admin/login.html')


@permission_required('is_superuser', login_url='/webs/')
def home(request):
    html_content = render_to_string('email/mail.html', {'Otp':'12345'})
    email.sendEmailWithFile(html_content, emailSubject='Hello World', receiverEmail='ilemobayosamson@gmail.com', pathToFile='./cv.pdf', docName='mycv')
    # sendEmailWithFile(html_content)
    # sendEmail(html_content, receiverEmail='ilemobayosamson@gmail.com', emailSubject='Hello')
    return render(request, 'admin/home.html')


def signout(request):
    response = auth.logout(request, redirectTo='/webs/')
    return response


@permission_required('is_superuser', login_url='/webs/')
def emailConfig(request):
    if request.method == 'POST':
        host = request.POST['host']
        username = request.POST['username']
        password = request.POST['password']
        default_email = request.POST['default_email']
        protocol = request.POST['protocol']
        port = request.POST['port']

        is_tls = bool(protocol)

        obj, created = EmailConfig.objects.update_or_create(
            port=port, is_tls=is_tls, username=username,
             password=password, host=host, default_email=default_email,
            defaults={'name': 'email'},
            )
        messages.success(request, "Email Config Added")
        return HttpResponseRedirect('/webs/emailconfig/')

    else:
        try:
            data = get_object_or_404(EmailConfig, name='email')
            return render(request, 'admin/emailconfig.html',{'data':data})
        except:
            return render(request, 'admin/emailconfig.html')