from django.db import models


class FoodModel(models.Model):
    class Meta:
        db_table = "food"
