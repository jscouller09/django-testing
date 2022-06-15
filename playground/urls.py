from django.urls import path
from . import views

# URLConf
app_name = 'products'
urlpatterns = [
    path('hello/', views.say_hello),
    path('products/', views.product_list_view, name='product-list'),
    path('products/<int:id>/', views.dynamic_lookup_view, name='product-detail'),
    path('products/<int:id>/delete', views.product_delete_view, name='product-delete'),
    path('create/', views.product_create_view, name='product-create'),
]
