from commu.models import Comment
from django.core.paginator import Paginator

def create_an_comment(article, user, comment):
    comment = Comment.objects.create(article=article,
                                     author=user,
                                     comment=comment)
    return comment

def update_an_comment(comment, edit_comment):
    comment.comment = edit_comment
    comment.save()
    return '댓글 수정 완료'

def delete_an_comment(id):
    return Comment.objects.filter(id=id).delete()

def get_comment_page(page: int, id):
    comment_list = Comment.objects.filter(article_id=id).order_by("-created_at").all()  # 생성시간 역순으로 모두불러오기
    paginator = Paginator(comment_list, 10)  # 댓글리스트를 한 페이지에 3개씩 불러오는 페이지네이터 정의
    comments = paginator.get_page(page)  # 현재 페이지에 표시될 댓글들을 넘겨줌
    return comments