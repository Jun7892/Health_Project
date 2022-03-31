from django.urls import path
from . import views

urlpatterns = [
    path('', views.eat_view, name='eat'),
    path('detail/<int:id>/', views.eat_detail, name='eat_detail'),
    path('detail/<int:id>/bookmark/', views.bookmark, name='bookmark'),
    path('search/', views.eat_search, name='eat_search'),
    path('item/', views.item_view, name='item'),
]