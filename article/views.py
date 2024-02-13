import json
from django.shortcuts import render, redirect, get_object_or_404

from article.models import Article

# Create your views here.
from django.shortcuts import render, redirect


def create_article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        if title == "" or content == "":
            return render(request, 'create_article.html')

        article = Article(title=title, content=content)
        article.save()
        return redirect('view_article', articleId=article.id)

    return render(request, 'create_article.html')


def update_article(request, articleId):
    article = get_object_or_404(Article, id=articleId)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        if title is None or content is None:
            error_message = "제목과 내용을 모두 입력해주세요."
            return render(request, 'error.html', {'error_message': error_message})

        article.title = title
        article.content = content
        article.save()
        return redirect('view_article', articleId=article.id)
    return render(request, 'update_article.html', {'article': article})

def delete_article(request, articleId):
    article = get_object_or_404(Article, id=articleId)
    if request.method == 'POST':
        article.delete()
        return redirect('list_article')
    return render(request, 'delete_article.html', {'article': article})

def list_article(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        return render(request, 'list_article.html', {'articles': articles})
    return render(request, 'error.html')

def view_article(request, articleId):
    if request.method == 'GET':
        article = get_object_or_404(Article, id=articleId)
        return render(request, 'veiw_article.html', {'article': article})
    return render(request, 'error.html')
