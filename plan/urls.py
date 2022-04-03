from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.add_Event, name='addEvent'),
    path('', views.plan_view, name='plan'),
    # path('create/', views.create_to_do, name='create_to_do'),
]
