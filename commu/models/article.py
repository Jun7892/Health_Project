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

    def get_created_at(self):
        if self.created_at:
            result = ''.join(str(self.created_at)).split('.')
            day = result[0].split(' ')[0]
            time = result[0].split(' ')[1][:5]
            return day+' '+time
        else:
            None