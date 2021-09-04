
from functools import wraps

from django.shortcuts import render
# from django.shortcuts import HttpResponseRedirect,



def add_footer(function):
    footer = 'hello World'
    @wraps(function)
    def footers(request, template_name, *args, **kwargs):
        return render(request, template_name)
    return footers