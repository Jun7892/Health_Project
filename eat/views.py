from django.shortcuts import render, redirect
from eat.models import FoodModel
from django.core.paginator import Paginator
import random


def eat_view(request):
    if request.method == 'GET':
        recipe = FoodModel.objects.all()
        page = request.GET.get('page')
        paginator = Paginator(recipe, '12')
        page_obj = paginator.get_page(page)
        context = {
            'page': page_obj,
        }
        return render(request, 'eat/eat.html', context)


def eat_detail(request, id):
    recipe = FoodModel.objects.get(id=id)
    recipe.ingredients = recipe.get_ingredients()
    recipe.step = recipe.get_step()
    return render(request, 'eat/eat_detail.html', {'recipe': recipe})


def bookmark(request,id):
    if request.method == 'POST':
        user = request.user
        recipe = FoodModel.objects.get(id=id)
        if user in recipe.bookmark.all():
            recipe.bookmark.remove(user)
        else:
            recipe.bookmark.add(user)
    return redirect(f'/eat/detail/{id}')

