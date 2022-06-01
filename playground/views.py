from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# note views in Django are actually actions, or request -> response handlers



def say_hello(request):
    return render(request, template_name='hello.html') 
    # return render(request, template_name='hello.html', context={'name': 'James'}) 