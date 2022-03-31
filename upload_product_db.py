import os
import django
import csv

# 프로젝트 이름.settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "plz.settings")
django.setup()

from eat.models import *  # django.setup() 이후에 임포트해야 오류가 나지 않음

# csv파일 경로
CSV_PATH_PRODUCTS = 'city_product_price.csv'
with open(CSV_PATH_PRODUCTS, encoding='UTF8') as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)  # 출력시 함께 출력되는 맨첫줄을 제외하고 출력하기 위함
    for row in data_reader:
        prodectModel = ProductModel()
        prodectModel.country_name = row[0]
        prodectModel.item_name = row[1]
        prodectModel.day1 = row[2]
        prodectModel.dpr1 = row[3]
        prodectModel.day2 = row[4]
        prodectModel.dpr2 = row[5]
        prodectModel.value = row[6]
        prodectModel.unit = row[7]
        prodectModel.save()
