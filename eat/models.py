from django.db import models


class FoodModel(models.Model):
    class Meta:
        db_table = "food"

    title = models.CharField(max_length=256)
    ingredients = models.TextField()
    image = models.URLField()
    step = models.TextField()