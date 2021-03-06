import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from commu.models import Article
from commu.models import Comment
from commu.services.comment_service import create_an_comment, delete_an_comment, update_an_comment, get_comment_page
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator


@login_required(login_url='sign_in')
def commu_view(request):
    if request.method == 'GET':
       article = Article.objects.all().order_by('-id')
       page = request.GET.get('page')
       paginator = Paginator(article, '20')
       page_obj = paginator.get_page(page)
       article_created_at = str(Article.created_at)
       context = {
           'page': page_obj,
           'article_created_at':article_created_at
       }
       return render(request, 'commu/commu.html', context)


@login_required(login_url='sign_in')
def write_comment(request, id): #해당게시글의 id
    user = request.user  # 지금 접속중인 user정보
    comment = request.POST['comment']
    article = Article.objects.get(id=id)

    if request.method == 'POST': #댓글작성 요청
        if comment != "":#댓글 빈칸아니면
            create_an_comment(article, user, comment)
            return redirect('/commu/' + str(id)) #해당게시글 페이지로
        else: #빈칸이면
            messages.error(request, '내용을 입력하세요')
            return redirect(f'/commu/{id}')

@login_required(login_url='sign_in')
def update_comment(request, id): #해당댓글의 id
    comment = Comment.objects.filter(id=id).get()  # 쿼리셋
    article_id = comment.article_id
    if request.method == 'POST':
        edit_comment = request.POST['update_comment'] # 댓글모델에 바꿀 댓글내용
        print(edit_comment)
        if request.user == comment.author: #접속중인 유저가 댓글작성자라면
            if edit_comment != "":
                # 댓글id와, 바꿀 해당쿼리셋객체, 수정할 댓글내용을 넘겨줌
                update_an_comment(comment, edit_comment) #댓글 수정함수 #메세지 넘길거면 return값 넘기기
                return redirect('/commu/' + str(article_id))#해당게시글 페이지로
            else:#빈칸이면
                messages.info(request, '내용을 입력하세요.')
                return redirect('/commu/' + str(article_id))#해당게시글 페이지로
        else:#메세지 띄우기
            messages.info(request, '작성자만 수정할 수 있어요~.')
            return redirect('/commu/' + str(article_id))#해당게시글 페이지로
    else:
        messages.info(request, '잘못된 접근입니다.')
        return redirect('/commu/' + str(article_id))

          
@login_required(login_url='sign_in')
def delete_comment(request, id):# 해당댓글 id
    comment = Comment.objects.filter(id=id).get()
    article_id = comment.article_id
    if request.user == comment.author:
        delete_an_comment(id)
        return redirect('/commu/' + str(article_id))#해당 게시글 페이지로
    else:
        message = messages.warning(request, '잘못된 접근입니다.')
        return redirect('/commu/' + str(article_id),messages=message)


@login_required(login_url='sign_in')
def article_create(request):
    if request.method == 'GET':
        return render(request, 'commu/commu_create_article.html')
        # return render(request, 'commu/test.html')
    elif request.method == 'POST':
        user = request.user
        title = request.POST.get('title', '')
        content = request.POST['editordata']
        print(content)
        # content = request.POST.get('content', '')
        if content == '' or title == '':
            return render(request, 'commu/commu_create_article.html', {'error': '제목, 내용은 공백으로 작성 될 수 없습니다.'})
        else:
            my_article = Article.objects.create(author=user, title=title, content=content)
            my_article.save()
            return redirect("/commu")


@login_required(login_url='sign_in')
def article_detail(request, id):
    try:
        get_article = Article.objects.get(id=id)
        page = request.GET.get("page")
        comments = get_comment_page(page, id)
        return render(request, 'commu/commu_detail.html', {'article': get_article, 'comments': comments})
    except Article.DoesNotExist: #없는 게시물에 접근할때
        return redirect('/commu')


@login_required(login_url='sign_in')
def delete_an_article(request, id): # 글 삭제
    my_article = Article.objects.get(id=id)
    my_article.delete()
    return redirect('/commu')


@login_required(login_url='sign_in')
def article_update(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        article.title = request.POST['title']
        article.content = request.POST['editordata']
        print(article.content)
        # article.content = request.POST['content']
        if article.content == '' or article.title == '':
            return render(request, 'commu/commu_update_article.html', {'error': '내용에 빈칸이 있습니다'})
        else:
            article.save()
            return redirect('/commu', article.id)
    else:
        return render(request, 'commu/commu_update_article.html', {'article':article})


@login_required(login_url='sign_in')
def like(request, id):
    if request.method == 'POST':
        user = request.user
        article = Article.objects.get(id=id)
        if user in article.like_user.all():
            article.like_user.remove(user)
        else:
            article.like_user.add(user)
    return redirect(f'/commu/{id}')


@login_required(login_url='sign_in')
def search_article(request):
    article_list = Article.objects.all()
    search = request.GET.get('search_article', '')
    if search:
        search_list = article_list.filter(Q(title__icontains=search) | Q(content__icontains=search))
        page = request.GET.get('page')
        paginator = Paginator(search_list, '20')
        page_obj = paginator.get_page(page)
        context = {
            'page': page_obj,
        }
        return render(request, 'commu/commu_search.html', context)
    else:
        return redirect('/commu')