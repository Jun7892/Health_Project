from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from commu.services.article_service import create_an_article, get_article_list


# @login_required(login_url:'sign_in')
def commu_view(request):
    if request.method == 'GET':
        #글들 좌라락 불러오기
        page = request.GET.get("page")
        comments = get_article_list(page)
        return render(request, 'commu/commu_test.html')
    else: #post요청이면
        user = request.user # 지금 접속해있는 user정보
        title=request.POST['title']
        content=request.POST['content']
        create_an_article(user, title, content) #게시글 생성함수
        return redirect()


def delete_an_article(request): # 글 삭제
    pass