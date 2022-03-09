from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_view, name='item'),
]