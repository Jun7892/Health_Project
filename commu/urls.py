from django.urls import path
from . import views

urlpatterns = [
    path('', views.commu_view, name='commu'),
    path('/comment/<int:id>', views.write_comment, name='writecomment'),
    path('/comment/delete/<int:id>', views.delete_comment, name='deletecomment'),
    path('<int:id>/', views.article_detail, name='article_detail'),
    path('create/', views.article_create, name='article_create'),
    path('delete/<int:id>', views.delete_an_article, name="article_delete"),
]