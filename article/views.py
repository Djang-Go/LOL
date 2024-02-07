import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from article.models import Article

# Create your views here.
def create_article(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data['title']
        content = data['content']
        article = Article(title=title, content=content)
        article.save()
        return HttpResponse("생성 완료")
    return HttpResponse("생성 실패")

def hello_world(request):
    return HttpResponse("hello world!")