from django.urls import path
from . import views

urlpatterns = [
    path('', views.commu_view, name='commu'),
    path('<int:id>/', views.article_detail, name='article_detail'),
]