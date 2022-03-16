from django.db import models


class FoodModel(models.Model):
    class Meta:
        db_table = "food"

    image = models.URLField()
    title = models.CharField(max_length=256)
    ingredients = models.TextField()
    step = models.TextField()