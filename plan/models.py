from django.db import models
from second.models import User


# Create your models here.
class Plan(models.Model):
    class Meta:
        db_table = 'plan'
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

