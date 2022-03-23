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
    path('password_reset/', views.password_reset, name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='login/password_reset_email.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='login/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='login/password_reset_complete.html'),
         name='password_reset_complete'),
    # path('send', views.send_email, name='send_email'), #이메일 보내지는지 확인용 url
]