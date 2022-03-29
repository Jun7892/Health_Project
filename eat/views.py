from django.shortcuts import render, redirect
from eat.models import FoodModel
from django.core.paginator import Paginator
import random
import pandas as pd
from konlpy.tag import Mecab
from gensim.test.utils import common_texts
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import requests
import json


def eat_view(request):
    if request.method == 'GET':
        recipe = FoodModel.objects.all().order_by('id')
        page = request.GET.get('page')
        paginator = Paginator(recipe, '12')
        page_obj = paginator.get_page(page)
        context = {
            'page': page_obj,
        }
        product = get_city_product_price()
        return render(request, 'eat/eat.html', {'context':context,'product':product})

def eat_detail(request, id):
    recipe = FoodModel.objects.get(id=id)
    print(recipe)
    recipe.ingredients = recipe.get_ingredients()
    recipe.step = recipe.get_step()
    # --------------------추천시스템--------------------------------
    # 형태소 분석을 위한 객체를 만들고,
    mecab = Mecab()
    # 명사 단위로 뉴스 본문을 나누고,
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


def city_select():
    code = {
          '서울':'1101',
          '부산':'2100',
          '대구':'2200',
          '인천':'2300',
          '광주':'2401',
          '대전':'2501',
          '울산':'2601',
          '수원':'3111',
          '춘천':'3211',
          '청주':'3311',
          '전주':'3511',
          '포항':'3711',
          '제주':'3911',
          '순천':'3613',
          '안동':'3714',
          '창원':'3814'
          }
    params = []
    for i,j in code.items():
        a = {"p_cert_key":"50ae0e04-be51-4bf2-a7a1-ee6ac5062542", "p_cert_id":"2371", "p_returntype":"json", "p_countycode":f"{j}"}
        params.append(a)

    return params


def get_city_product_price():
    params_list = city_select()
    city_product_price = []
    for params in params_list:
      url = 'http://www.kamis.or.kr/service/price/xml.do?action=dailyCountyList'
      response = requests.get(url, params=params)
      df = response.json()
      target = df['price']

      for idx in range(len(target)):
        product_price = [target[idx]['county_name'], target[idx]['item_name'], target[idx]['day1'], target[idx]['dpr1'], target[idx]['day2'], target[idx]['dpr2'], target[idx]['value'], target[idx]['unit']]
        city_product_price.append(product_price)

    return city_product_price


