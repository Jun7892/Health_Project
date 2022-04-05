import os
import django
import csv

# 프로젝트 이름.settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "plz.settings")
django.setup()

from workout.models import *  # django.setup() 이후에 임포트해야 오류가 나지 않음

# csv파일 경로
CSV_PATH_PRODUCTS = 'video_id_.csv'
with open(CSV_PATH_PRODUCTS, encoding='utf-8') as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)  # 출력시 함께 출력되는 맨첫줄을 제외하고 출력하기 위함
    for row in data_reader:
        video = Video_id()
        video.video_id = row[0]
        video.title = row[1]
        video.save()