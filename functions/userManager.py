from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from webs.models import *
from django.db.models import Q
import string
import random
from .sendMail import Email
from .validator import Validator


send = Email()
validate = Validator()

class UserManager:

    def userRegistration(self, request, fullname, email, mobile, password1, password2, redirectUrl):
        T = 5
        res = ''.join(random.choices(string.digits, k=T))
        user_no = f'MNO{str(res)}'
        """Test if Email or Mobile Number has been used already within the system"""
        if User.objects.filter(Q(email=email) | Q(mobile=mobile)).exists():
            messages.error(request, "Email or Mobile Number has been used")
            return HttpResponseRedirect(redirectUrl)

            """Test if the password 1 is the same as password 2"""
        elif password1 != password2:
            messages.error(request, "Password did not match")
            return HttpResponseRedirect(redirectUrl)

        elif validate.passwordValidator(password1) == False:
            messages.error(request, "Password must be between 8-15 and contain Uppercase and special character like @!*")
            return HttpResponseRedirect(redirectUrl)
        
        else:
            """Create User"""
            user = User.objects.create_user(fullname=fullname, email=email, mobile=mobile, password=password1, is_customer=True)
            acct = AccountInfo(user=user, user_no=user_no)
            user.save()
            acct.save()

            """Send registration Email"""
            send.registrationEmail(fullname, email, user_no)
            messages.success(request, "Account Created Successfully")
            return HttpResponseRedirect(redirectUrl)