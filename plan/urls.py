from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.plan_view, name='plan'),
    path('', views.plan_view, name='plan')
]
