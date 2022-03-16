from django.db import models
import json
import ast


class FoodModel(models.Model):
    class Meta:
        db_table = "food"

    image = models.URLField()
    title = models.CharField(max_length=256)

    ingredients = models.CharField(max_length=256)

    def set_ingredients(self, x):
        self.ingredients = json.dumps(x)

    def get_ingredients(self):
        return ast.literal_eval(json.loads(self.ingredients))

    step = models.CharField(max_length=256)

    def set_step(self, x):
        self.step = json.dumps(x)

    def get_step(self):
        return ast.literal_eval(json.loads(self.step))
