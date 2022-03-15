import requests
import pandas as pd
import re
from bs4 import BeautifulSoup


def make_urllist(page_num):
    urllist = []

    for i in range(1, page_num + 1):
        url = f'https://www.10000recipe.com/recipe/list.html?order=reco&page={i}'

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
        }

        food = requests.get(url, headers=headers)

        html = food.text

        soup = BeautifulSoup(html, 'html.parser')

        ul = soup.select_one('ul.rcp_m_list2')  # ul 태그 찾기

        a = ul.select('li > div > a')  # ul 태그안의 a태그

        for line in a:
            urllist.append("https://www.10000recipe.com/" + line["href"])  # href 안의 url 찾기

    return urllist


def make_food_data(urllist):
    image_list = []
    title_list = []
    ingredients_list = []
    step_list = []
    num = 0
    for url in urllist:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        html = response.text

        try:  # 레시피가 삭제되어서 클릭하면 존재하지 않는 레시피인 경우 존재
            soup = BeautifulSoup(html, 'html.parser')
            img = soup.select('#main_thumbs')[0]  # img 태그 가져오기 리스트 제거)
            src = img.get('src')  # src 가져오기
        except:
            continue

        print(f'{num}: {src}')
        num += 1

        title = soup.select('#contents_area > div.view2_summary.st3 > h3')[0]  # h3 태그 가져오기 리스트제거
        title = re.sub('[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]', '', title.get_text())  # 텍스트만 추출

        li_list = soup.select('#divConfirmedMaterialArea > ul > a > li')  # li 태그 리스트로 만들어주기
        if li_list == []:
            continue
        ingredients = []
        for li in li_list:
            ingredients.append(li.get_text().replace('\n', '').replace(' ', ''))  # 재료와 용량 추출, \n, 띄어쓰기 삭제

        try:
            view_step = soup.select_one('div.view_step')  # view_step 첫번째꺼 가져오기
            sequence_list = view_step.select('div.view_step_cont > .media-body')  # 조리순서 가져오기
            if sequence_list == []:
                continue
        except:
            continue
        step = []
        for i in sequence_list:
            step.append(re.sub('[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]', '',
                               i.get_text().replace('\n', ' ')))  # 텍스트만 특수문자 제거

        image_list.append(src)
        title_list.append(title)
        step_list.append(step)
        ingredients_list.append(ingredients)

    df = pd.DataFrame({'img': image_list, 'tltle': title_list, 'ingredients': ingredients_list, 'step': step_list})

    return df


df = make_food_data(make_urllist(200))
df.to_csv('recipe_data.csv', index=False)
