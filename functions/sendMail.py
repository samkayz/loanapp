from re import template
from django.template.loader import render_to_string
from .emailBackend import EmailBackEnd

send = EmailBackEnd()


class Email:


    def registrationEmail(self, fullname, email, userId):
        template = render_to_string('email/register.html', {'fullname': fullname, 'userid':userId})

        send.sendEmail(template, email, emailSubject='Welcome to Loan App')
        pass