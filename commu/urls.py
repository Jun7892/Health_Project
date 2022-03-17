from django.urls import path
from . import views

urlpatterns = [
    path('', views.commu_view, name='commu'),
]