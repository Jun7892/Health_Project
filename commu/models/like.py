from django.db import models
from commu.models.article import Article
from second.models import User


class Like(models.Model):
    class Meta:
        db_table = 'like'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)