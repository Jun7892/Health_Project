from django.urls import path
from . import views

urlpatterns = [
    # path('', views.item_view, name='item'),
    path('<int:id>', views.mypage, name='mypage'),  # 마이페이지로 이동
    path('update/profile/<int:id>', views.editprofile, name='edit_profile'),  # 프로필변경용 url
    path('update/email/<int:id>', views.reset_email, name='reset_email'),
    path('update/follow/<int:id>', views.user_follow, name='user_follow'),  # 팔로우/팔로우취소
    path('get/follow/<int:id>', views.show_follow, name='show_follow'),  # 팔로우목록 보기
    path('search/users', views.user_search, name='user_search'),#유저 검색
]