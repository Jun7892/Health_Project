from django.urls import path
from . import views

urlpatterns = [
    path('', views.eat_view, name='eat'),
]