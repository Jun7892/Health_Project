from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser): #models폴더로 따로 빼고싶었지만 settings.py에서 auth_user_model 경로지정하는법 찾고서 옮길 수 있을듯.
    class Meta:
        db_table = 'user'
    gender = models.TextField() # 남/여 로만 입력받도록 제한
    level = models.TextField()
    nickname = models.CharField(max_length=10) #닉네임 너무길까봐
    profile_img = models.TextField()


