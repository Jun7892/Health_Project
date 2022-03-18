from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from commu.models import Article
from commu.models import Comment
from commu.services.article_service import create_an_article, get_article_list
from commu.services.comment_service import create_an_comment, delete_an_comment, update_an_comment




# @login_required(login_url:'sign_in')
def commu_view(request):
    if request.method == 'GET':
       article = Article.objects.all().order_by('-id')
       return render(request, 'commu/commu.html', {'article': article})


# @login_required(login_url:'sign_in')
def write_comment(request, id): #해당게시글의 id
    if request.method == 'POST': #댓글작성 요청
        user = request.user # 지금 접속중인 user정보
        comment = request.POST['comment']
        article = Article.objects.get(id=id)
        comment = create_an_comment(article, user, comment)
        return redirect() #해당게시글 페이지로

      
# @login_required(login_url:'sign_in')
def update_comment(request, id): #해당댓글의 id
    if request.method == 'POST':
        comment = Comment.objects.filter(id=id).get() #쿼리셋
        edit_comment = request.POST['update_comment'] # 댓글모델에 바꿀 댓글내용
        if request.user == comment.author: #접속중인 유저가 댓글작성자라면
            # 댓글id와, 바꿀 해당쿼리셋객체, 수정할 댓글내용을 넘겨줌
            update_an_comment(comment, edit_comment) #댓글 수정함수 #메세지 넘길거면 return값 넘기기
            return redirect()#해당게시글 페이지로
        else:
            return JsonResponse({'msg':'잘못된 접근입니다.'})#어떤 방식으로 프론트에서 보여주냐에 따라 바뀔수 있음

          
# @login_required(login_url:'sign_in')
def delete_comment(request, id):# 해당댓글 id
    delete_an_comment(id)
    return redirect()#해당 게시글 페이지로


def delete_an_article(request, id): # 글 삭제
    my_article = Article.objects.get(id=id)
    my_article.delete()
    return redirect('/commu')


def article_detail(request, id):
    get_article = Article.objects.get(id=id)
    return render(request, 'commu/commu_detail.html', {'article': get_article})


def article_create(request):
    if request.method == 'GET':
        return render(request, 'commu/commu_create_article.html')
    elif request.method == 'POST':
        user = request.user
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        if content == '' or title == '':
            return render(request, 'commu/commu_create_article.html', {'error': '내용에 빈칸이 있습니다'})
        else:
            my_article = Article.objects.create(author=user, title=title, content=content)
            my_article.save()
            return redirect("/commu")
