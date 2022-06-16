from django.shortcuts import render, get_object_or_404
from .models import Article

# Create your views here.
def article_list_view(request):
    queryset = Article.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'article_list.html', context)

def article_detail_view(request, id):
    obj = get_object_or_404(Article, id=id)
    context = {'object': obj}
    return render(request, 'article_detail.html', context)