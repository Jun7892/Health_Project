from django.db import models
from second.models import User


# Create your models here.
class Plan(models.Model):
    class Meta:
        db_table = 'plan'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    to_do = models.CharField(max_length=60)
    meal = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

