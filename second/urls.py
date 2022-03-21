from django.urls import path
from . import views

urlpatterns = [
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('logout', views.logout, name='logout'),
    path('test/<int:id>', views.testmypage, name='test'),#프로필사진 변경확인용 임시 url
    path('test/follow/<int:id>', views.user_follow, name='user_follow'),#임시 url
    path('test/follow', views.show_follow, name='show_follow'), #임시 url
]