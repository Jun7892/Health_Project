from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.plan_view2, name='plan2'),
    path('', views.plan_view, name='plan')
]
