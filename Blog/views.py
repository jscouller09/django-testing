from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .models import Article
from .forms import ArticleModelForm

# Create your views here.
class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()   
    success_url = '..' # go back to list of articles instead of detail view for new article

    def form_valid(self, form):
        # print(form.cleaned_data)
        return super().form_valid(form)

class ArticleListView(ListView):
    # override default expected template location of <app_name>/<model_name>_list.html
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()   

class ArticleDetailView(DetailView):
    # override default expected template location of <app_name>/<model_name>_detail.html
    template_name = 'articles/article_detail.html'
    queryset = Article.objects.all()
    # or filter ids to be everything > 1
    # queryset = Article.objects.filter(id__gt=1)

class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()   
    success_url = '../..' # go back to list of articles instead of detail view for new article

    def form_valid(self, form):
        # print(form.cleaned_data)
        return super().form_valid(form)

class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    queryset = Article.objects.all()   
    
    def get_success_url(self):
        return reverse('articles:article-list')
    