from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def home_view(request, *args, **kwargs):
    data = {}
    data['view_name'] = 'home'
    data['user_name'] = request.user
    data['list_data'] = ['something', 123, 456]
    data['path'] = reverse(data['view_name'])
    return render(request, '{}.html'.format(data['view_name']), context=data)

def contact_view(request, *args, **kwargs):
    data = {}
    data['view_name'] = 'contact'
    data['user_name'] = request.user
    data['path'] = reverse(data['view_name'])
    return render(request, '{}.html'.format(data['view_name']), context=data)

def about_view(request, *args, **kwargs):
    data = {}
    data['view_name'] = 'about'
    data['user_name'] = request.user
    data['path'] = reverse(data['view_name'])
    return render(request, '{}.html'.format(data['view_name']), context=data)

def social_view(request, *args, **kwargs):
    data = {}
    data['view_name'] = 'social'
    data['user_name'] = request.user
    data['path'] = reverse(data['view_name'])
    return render(request, '{}.html'.format(data['view_name']), context=data)