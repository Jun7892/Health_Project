import os, json
from googleapiclient.discovery import build
from plz.settings import BASE_DIR

with open(os.path.join(BASE_DIR, 'plz/secret.json')) as f:
    secrets = json.loads(f.read())

id_list = []

def build_youtube_search(): #유튜브 api와함께 검색주소 만들어줌
    developer_key = secrets["YOUTUBE"]['Api_key']
    youtube_api_service_name ="youtube"
    youtube_api_version="v3"
    return build(youtube_api_service_name,youtube_api_version,developerKey=developer_key)


def get_search_response(youtube,query): # 검색결과를 리스트로저장
    search_response = youtube.search().list(q=query, order='relevance', part='id').execute()
    return search_response


def get_video_info(search_response): # 검색결과중 앞에 하나만 가져옴
    result = search_response['items'][0]['id']['videoId']
    return result


def get_video_list(query):# 불러오기
    youtube = build_youtube_search()
    query=query
    search_response = get_search_response(youtube, query)
    result = get_video_info(search_response)
    return result