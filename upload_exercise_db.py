import os
import django
import csv

# 프로젝트 이름.settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "plz.settings")
django.setup()

from workout.models import *  # django.setup() 이후에 임포트해야 오류가 나지 않음

# csv파일 경로
CSV_PATH_PRODUCTS = 'workout_data.csv'
with open(CSV_PATH_PRODUCTS, encoding='euc-kr') as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)  # 출력시 함께 출력되는 맨첫줄을 제외하고 출력하기 위함
    for row in data_reader:
        exercise = Exercise()
        exercise.age = row[0]
        exercise.level = row[1]
        exercise.gender = row[2]
        exercise.set_warm_up(row[3])
        exercise.set_main(row[4])
        exercise.save()