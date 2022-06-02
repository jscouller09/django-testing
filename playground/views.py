from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# note views in Django are actually actions, or request -> response handlers

def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
    x = calculate()
    # return render(request, template_name='hello.html') 
    return render(request, template_name='hello.html', context={'name': 'James'}) 