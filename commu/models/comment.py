from django.db import models

from commu.models.article import Article
from second.models import User


class Comment(models.Model):
    class Meta:
        db_table = 'comment'

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)