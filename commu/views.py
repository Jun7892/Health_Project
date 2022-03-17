from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models.article import Article


# @login_required(login_url:'sign_in')
def commu_view(request):
    if request.method == 'GET':
        article = Article.objects.all().order_by('-created_at')
        return render(request, 'commu/../templates/commu.html', {'article': article})
    if request.method == 'POST':
        author = request.user
        title = request.POST.get()
        content = request.POST.get()
        my_article = Article.objects.create(author=author, title=title, content=content)
        my_article.save()
        return render(request, 'commu/../templates/commu.html')


def delete_an_article(request, id): # 글 삭제
    pass