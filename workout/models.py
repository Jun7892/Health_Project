from django.db import models
import json
import ast
from second.models import User
# Create your models here.


class Exercise(models.Model):
    class Meta:
        db_table = "exercise"

    gender = models.CharField(max_length=10)
    level = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    warm_up = models.TextField(blank=True)

    def set_warm_up(self, x):
        self.warm_up = json.dumps(x)# 객체를 json 문자열로 변환

    def get_warm_up(self):
        return ast.literal_eval(json.loads(self.warm_up)) # json 문자열을 객체로 변환 후 리스트형태로 변환

    main = models.TextField(blank=True)

    def set_main(self, x):
        self.main = json.dumps(x)

    def get_main(self):
        return ast.literal_eval(json.loads(self.main))