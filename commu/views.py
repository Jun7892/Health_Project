from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models.article import Article


# @login_required(login_url:'sign_in')
def commu_view(request):
    if request.method == 'GET':
        article = Article.objects.all().order_by('-created_at')
        return render(request, 'commu/commu.html', {'article': article})


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
        author = request.user
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        my_article = Article.objects.create(author=author, title=title, content=content)
        my_article.save()
        return redirect("/commu")
