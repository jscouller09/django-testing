from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello/', views.say_hello),
    path('products/<int:id>/', views.dynamic_lookup_view, name='product'),
    path('create/', views.product_create_view, name='create'),
]
