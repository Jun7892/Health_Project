from django.db import models
from second.models import User


class Article(models.Model):
    class Meta:
        db_table = 'article'

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    like_user = models.ManyToManyField(User, related_name="like", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
