
from commu.models.article import Article
from django.core.paginator import Paginator

def get_article_list(page:int):
    article_list = Article.objects.order_by('-created_at').all() #작성된 게시글 모두불러와서
    paginator = Paginator(article_list, 10) #한페이지에 10개씩 보여주기
    articles = paginator.get_page(page)
    return articles

def create_an_article(user:str,title:str ,content:str): #author는 username임
    article = Article.objects.create(author=user, title=str(title), content=str(content))
    return article