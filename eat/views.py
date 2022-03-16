from django.shortcuts import render
from eat.models import FoodModel
import random


def eat_view(request):
    if request.method == 'GET':
        recipe = FoodModel.objects.all()
        recipe = random.sample(list(recipe), 12)
        return render(request, 'eat/eat.html', {'recipe': recipe})


def eat_detail(request, id):
    recipe = FoodModel.objects.fillter(id=id)

