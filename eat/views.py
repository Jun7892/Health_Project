from django.shortcuts import render, redirect
from eat.models import FoodModel, ProductModel
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import random
import pandas as pd
from konlpy.tag import Mecab
from gensim.test.utils import common_texts
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import requests
import json
from django.db.models import Q
from second.models import *


def eat_view(request):
    if request.method == 'GET':
        recipe = FoodModel.objects.all().order_by('id')
        code = ['서울','부산','대구','인천','광주','대전','울산','수원','춘천','청주','전주','포항','제주','순천','안동','창원']
        seoul = ProductModel.objects.filter(country_name='서울')
        busan = ProductModel.objects.filter(country_name='부산')
        daegu = ProductModel.objects.filter(country_name='대구')
        incheon = ProductModel.objects.filter(country_name='인천')
        gwangju = ProductModel.objects.filter(country_name='광주')
        daejeon = ProductModel.objects.filter(country_name='대전')
        ulsan = ProductModel.objects.filter(country_name='울산')
        suwon = ProductModel.objects.filter(country_name='수원')
        chuncheon = ProductModel.objects.filter(country_name='춘천')
        chungju = ProductModel.objects.filter(country_name='청주')
        jeonju = ProductModel.objects.filter(country_name='전주')
        pohang = ProductModel.objects.filter(country_name='포항')
        jeju = ProductModel.objects.filter(country_name='제주')
        suncheon = ProductModel.objects.filter(country_name='순천')
        andong = ProductModel.objects.filter(country_name='안동')
        changwon = ProductModel.objects.filter(country_name='창원')

        page = request.GET.get('page')
        paginator = Paginator(recipe, '12')
        page_obj = paginator.get_page(page)
        context = {
            'page': page_obj,
            'seoul': seoul,
            'busan': busan,
            'daegu': daegu,
            'incheon':incheon,
            'gwangju': gwangju,
            'daejeon':daejeon,
            'ulsan':ulsan,
            'suwon':suwon,
            'chuncheon':chuncheon,
            'chungju':chungju,
            'jeonju':jeonju,
            'pohang':pohang,
            'jeju':jeju,
            'suncheon':suncheon,
            'andong':andong,
            'changwon':changwon,
            'code':code
        }
        return render(request, 'eat/eat.html', context)


def eat_detail(request, id):
    recipe = FoodModel.objects.get(id=id)
    print(recipe)
    recipe.ingredients = recipe.get_ingredients()
    recipe.step = recipe.get_step()
    # --------------------추천시스템--------------------------------
    # 형태소 분석을 위한 객체를 만들고,
    mecab = Mecab(dicpath=r"C:/mecab/mecab-ko-dic")
    # 명사 단위로 레시피 제목을 나누고,
    tmp = mecab.nouns(recipe.title)
    # print(tmp)
    #학습된 모델 불러와서
    model = Doc2Vec.load('vmodel.model')
    # print(model)
    #현재페이지의 제목과 학습된 모델을 이용하여 유사도를 구하고 
    inferred_doc_vec = model.infer_vector(tmp)
    # 유사도구한 것들을 문서화 시키는과정 
    most_similar_docs = model.docvecs.most_similar([inferred_doc_vec], topn=8)
    # print(most_similar_docs)
    recommend=[]
    # index와 그 유사도를 함께 보여줍니다.
    for index, similarity in most_similar_docs:
        recommend_image = FoodModel.objects.filter(id=index)
        recommend.append(recommend_image)

    return render(request, 'eat/eat_detail.html', {'recipe': recipe, 'recommend': recommend})


def bookmark(request,id):
    if request.method == 'POST':
        user = request.user
        recipe = FoodModel.objects.get(id=id)
        if user in recipe.bookmark.all():
            recipe.bookmark.remove(user)
        else:
            recipe.bookmark.add(user)
    return redirect(f'/eat/detail/{id}')


def eat_search(request):
    if request.method == 'GET':
        recipe = FoodModel.objects.all().order_by('id')
        search_recipe = request.GET.get('search_recipe', ' ')
        code = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '수원', '춘천', '청주', '전주', '포항', '제주', '순천', '안동', '창원']
        seoul = ProductModel.objects.filter(country_name='서울')
        busan = ProductModel.objects.filter(country_name='부산')
        daegu = ProductModel.objects.filter(country_name='대구')
        incheon = ProductModel.objects.filter(country_name='인천')
        gwangju = ProductModel.objects.filter(country_name='광주')
        daejeon = ProductModel.objects.filter(country_name='대전')
        ulsan = ProductModel.objects.filter(country_name='울산')
        suwon = ProductModel.objects.filter(country_name='수원')
        chuncheon = ProductModel.objects.filter(country_name='춘천')
        chungju = ProductModel.objects.filter(country_name='청주')
        jeonju = ProductModel.objects.filter(country_name='전주')
        pohang = ProductModel.objects.filter(country_name='포항')
        jeju = ProductModel.objects.filter(country_name='제주')
        suncheon = ProductModel.objects.filter(country_name='순천')
        andong = ProductModel.objects.filter(country_name='안동')
        changwon = ProductModel.objects.filter(country_name='창원')

        if search_recipe:
            search_list = recipe.filter(Q(title__icontains=search_recipe) | Q(ingredients__icontains=search_recipe))
            page = request.GET.get('page')
            paginator = Paginator(search_list, '12')
            page_obj = paginator.get_page(page)
            context = {
                'page': page_obj,
                'search':search_recipe,
                'seoul': seoul,
                'busan': busan,
                'daegu': daegu,
                'incheon': incheon,
                'gwangju': gwangju,
                'daejeon': daejeon,
                'ulsan': ulsan,
                'suwon': suwon,
                'chuncheon': chuncheon,
                'chungju': chungju,
                'jeonju': jeonju,
                'pohang': pohang,
                'jeju': jeju,
                'suncheon': suncheon,
                'andong': andong,
                'changwon': changwon,
                'code': code

            }
            return render(request, 'eat/eat_search.html', context)
        else:
            return redirect('/eat')


def item_view(request):
    return render(request, 'item.html')
