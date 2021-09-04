from django.contrib.auth import get_user_model, authenticate, login as signin, logout as signout
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from webs.models import *
from django.conf import settings

allInstallApp = settings.INSTALLED_APPS


class Auth:

    def userLogin(self, request, email, password, errorRedirectTo, successRedirect):
        """ Get the Application Name"""
        appName = __package__

        if '@' not in email:
            messages.error(request, "Invalid Email format")
            return HttpResponseRedirect(errorRedirectTo)
        else:
            try:
                u = get_object_or_404(User, email=email)

                """Check if the Login Application is Webs"""

                """Call the Authentication class"""
                user = authenticate(email=email, password=password)

                """Test if the User is super user"""
                if u.is_superuser == True and appName == 'webs':

                    """ Test if the Suplied information is True"""
                    if user is not None:
                        """Call the Sign class"""
                        signin(request, user)
                        messages.success(request, f'Welcome {u.fullname}')
                        return HttpResponseRedirect(successRedirect)
                    else:
                        messages.error(request, "Permission Denied")
                        return HttpResponseRedirect(errorRedirectTo)
                
                    """ Test if the user is customer """
                elif u.is_customer == True and appName == 'customer':
                    if user is not None:
                        """Call the Sign class"""
                        signin(request, user)
                        messages.success(request, f'Welcome {u.fullname}')
                        return HttpResponseRedirect(successRedirect)
                    else:
                        messages.error(request, "Permission Denied")
                        return HttpResponseRedirect(errorRedirectTo)
                
                    """ Test if the user is Agent """
                elif u.is_agent == True and appName == 'agent':
                    if user is not None:
                        """Call the Sign class"""
                        signin(request, user)
                        messages.success(request, f'Welcome {u.fullname}')
                        return HttpResponseRedirect(successRedirect)
                    else:
                        messages.error(request, "Permission Denied")
                        return HttpResponseRedirect(errorRedirectTo)
                
                    """ Test if the user is manager """
                elif u.is_manager == True and appName == 'manager':
                    if user is not None:
                        """Call the Sign class"""
                        signin(request, user)
                        messages.success(request, f'Welcome {u.fullname}')
                        return HttpResponseRedirect(successRedirect)
                    else:
                        messages.error(request, "Permission Denied")
                        return HttpResponseRedirect(errorRedirectTo)
                
                    """ Test if the user is Accountant """
                else:
                    if user is not None:
                        """Call the Sign class"""
                        signin(request, user)
                        messages.success(request, f'Welcome {u.fullname}')
                        return HttpResponseRedirect(successRedirect)
                    else:
                        
                        messages.error(request, "Permission Denied")
                        return HttpResponseRedirect(errorRedirectTo)

                """If User doesn't exist within the system"""
            except:
                messages.error(request, "User is not a register member")
                return HttpResponseRedirect(errorRedirectTo)
    

    def logout(self, request, redirectTo):
        signout(request)
        messages.success(request, "Goodbye")
        return HttpResponseRedirect(redirectTo)