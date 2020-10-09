"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import Form
import random


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    context = {'year': datetime.now().year }

    if request.method == "POST":
        name_surname = request.POST.get('nameSurname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        form = Form(name_surname=name_surname, email=email, phone=phone, message=message)
        form.save()
        context.update({'success':"Dziękujemy, skotaktujemy się z tobą!"})

    return render( request, 'app/index.html', context)

def compensation(request):
    context = {'year': datetime.now().year }
    value = random.randint(0,50) * 5
    context.update({'money': value})

    return render(request, 'app/compensation.html', context) 


def docs(request):

    

    context = {'year': datetime.now().year}




    return render(request, 'app/docs.html', context) 

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
