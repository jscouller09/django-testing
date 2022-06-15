from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from playground.forms import ProductForm
from .models import Product
from django.contrib.auth.decorators import login_required
from .forms import ProductForm

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

# @login_required
# def product_detail_view(request):
#     obj = Product.objects.get(id=1)
#     context = {'object': obj}
#     return render(request, 'products/product_detail.html', context)

@login_required
def dynamic_lookup_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {'object': obj}
    return render(request, 'products/product_detail.html', context)

@login_required
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        # re-render empty form
        form = ProductForm()
    context = {'form': form}
    return render(request, 'products/product_create.html', context)

@login_required
def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        # confirming delete
        obj.delete()
        return redirect('../')
    context = {'object': obj}
    return render(request, 'products/product_delete.html', context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'products/product_list.html', context)