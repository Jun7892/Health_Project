from django.urls import path
from . import views

urlpatterns = [
    path('', views.eat_view, name='eat'),
    path('detail/<int:id>/', views.eat_detail, name='eat_detail')
]