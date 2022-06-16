from django.urls import path
from . import views

# URLConf
app_name = 'articles'
urlpatterns = [
    path('articles/', views.article_list_view, name='article-list'),
    path('articles/<int:id>/', views.article_detail_view, name='article-detail'),
]
