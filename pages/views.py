from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def home_view(request, *args, **kwargs):
    data = {}
    data['view_name'] = 'home'
    data['user_name'] = request.user
    data['path'] = reverse(data['view_name'])
    return render(request, '{}.html'.format(data['view_name']), data)

def contact_view(request, *args, **kwargs):
    data = {}
    data['view_name'] = 'contact'
    data['user_name'] = request.user
    data['path'] = reverse(data['view_name'])
    return render(request, '{}.html'.format(data['view_name']), data)

def about_view(request, *args, **kwargs):
    data = {}
    data['view_name'] = 'about'
    data['user_name'] = request.user
    data['path'] = reverse(data['view_name'])
    return render(request, '{}.html'.format(data['view_name']), data)

def social_view(request, *args, **kwargs):
    data = {}
    data['view_name'] = 'social'
    data['user_name'] = request.user
    data['path'] = reverse(data['view_name'])
    return render(request, '{}.html'.format(data['view_name']), data)