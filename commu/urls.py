from django.urls import path
from . import views

urlpatterns = [
    path('', views.commu_view, name='commu'),
    path('comment/<int:id>', views.write_comment, name='writecomment'),#여기서는 article.id
    path('delete/comment/<int:id>', views.delete_comment, name='deletecomment'),#comment의 id
    path('update/comment/<int:id>', views.update_comment, name='updatecomment'),#comment의 id
    path('<int:id>/', views.article_detail, name='article_detail'),
    path('create/', views.article_create, name='article_create'),
    path('delete/<int:id>/', views.delete_an_article, name="article_delete"),
    path('update/<int:id>/', views.article_update, name="article_update"),
    path('like/<int:id>', views.like, name='like'),
]