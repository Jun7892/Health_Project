from django.urls import path
from . import views

urlpatterns = [
    path('', views.eat_view, name='eat'),
    # path('detail/<int:pk>', views.eat_detial, name='eat_detail')
]