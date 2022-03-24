from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('logout', views.logout, name='logout'),
    path('test/<int:id>', views.testmypage, name='test'),#프로필사진 변경확인용 임시 url
    path('test/update/follow/<int:id>', views.user_follow, name='user_follow'),#임시 url
    path('test/follow/<int:id>', views.show_follow, name='show_follow'), #임시 url
    path('find_id', views.find_id, name='find_id'),
    path('password_reset/', views.password_reset_mailing, name='password_reset_mailing'),
    path('password_reset/done/', views.email_send_success, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.reset_password,name='reset_password'),
]