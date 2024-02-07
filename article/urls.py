from django.urls import path

from article import views

urlpatterns = [
    path('create/', views.create_article, name='create_article'),
    path('<int:articleId>/', views.view_article, name='view_article'),
    path('update/<int:articleId>/', views.update_article, name='update_article'),
    path('delete/<int:articleId>', views.delete_article, name='delete_article'),
    path('list/', views.list_article, name='list_article')

]