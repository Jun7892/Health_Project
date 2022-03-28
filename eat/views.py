from django.shortcuts import render
from eat.models import FoodModel
from django.core.paginator import Paginator
import random
import pandas as pd
from konlpy.tag import Mecab
from gensim.test.utils import common_texts
from gensim.models.doc2vec import Doc2Vec, TaggedDocument



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
    print(recipe)
    recipe.ingredients = recipe.get_ingredients()
    recipe.step = recipe.get_step()
    
    # --------------------추천시스템--------------------------------
 
    print(recipe.title)
    # 형태소 분석을 위한 객체를 만들고,
    mecab = Mecab(dicpath=r"C:/mecab/mecab-ko-dic")
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
    print(recommend)
    
    return render(request, 'eat/eat_detail.html', {'recipe': recipe, 'recommend': recommend})

