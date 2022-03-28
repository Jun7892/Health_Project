from django.urls import path
from . import views

urlpatterns = [
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('logout', views.logout, name='logout'),
    path('find_id', views.find_id, name='find_id'),
    path('password_reset/', views.password_reset_mailing, name='password_reset_mailing'),
    path('password_reset/done/', views.email_send_success, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.reset_password, name='reset_password'),
    path('delete/<int:id>', views.user_delete, name='user_delete'),
]