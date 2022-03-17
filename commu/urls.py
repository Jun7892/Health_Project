from django.urls import path
from . import views

urlpatterns = [
    path('', views.commu_view, name='commu'),
    path('/comment/<int:id>', views.write_comment, name='writecomment'),
    path('/comment/delete/<int:id>', views.delete_comment, name='deletecomment')
]