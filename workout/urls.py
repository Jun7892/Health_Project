from django.urls import path
from . import views

urlpatterns = [
    path('', views.workout_view, name='workout'),
    path('get/level_test', views.age_different_show_page, name='age_different_show_page'),
    path('update/level/<int:id>', views.youth_and_old_level_confirm, name='youth_and_old_level_confirm'),
]