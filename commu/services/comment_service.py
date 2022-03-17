from commu.models import Comment

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