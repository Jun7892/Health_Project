from django.urls import path
from . import views

urlpatterns = [
    path('', views.workout_view, name='workout'),
]