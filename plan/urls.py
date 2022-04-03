from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.add_event, name='addEvent'),
    path('', views.plan_view, name='plan'),
    path('', views.all_events, name='allEvent'),
    path('', views.update, name='update'),
    path('<int:id>/', views.remove, name='remove'),
    # path('create/', views.create_to_do, name='create_to_do'),
]
#