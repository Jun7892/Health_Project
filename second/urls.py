from django.urls import path
from . import views

urlpatterns = [
    path('', views.showlogin, name='login') #나중에 로그아웃 후 로그인페이지로 돌아올때 대비
    path('/sign_up', views.sign_up, name='sign_up'),
    path('/sign_in', views.sign_in, name='sign_in'),
]