from django.urls import path

from article import views

urlpatterns = {
    path('', views.create_article, name='create_article'),
    path('', views.hello_world, name='hello_world'),
}