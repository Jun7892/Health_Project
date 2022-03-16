from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from second.models import User
from django.contrib import auth
from second.services.join_service import create_user, check_blank
import json
from second.services.login_service import login_check_blank


@csrf_exempt
def sign_up(request):
    select = json.loads(request.body.decode('utf-8'))
    print(select)
    if request.method == 'POST':
        username = select['username']
        password = select['password']
        nickname = select['nickname']
        try:
            gender = select['gender']
            level = select['level']
            print('빈칸통과!:',gender,level)
            founduser= User.objects.filter(username=username)
            if len(founduser) > 0: #같은아이디가 있을때.
                print('여기서 걸리니?:','founduser')
                return JsonResponse({'existid': True})
            else: #중복아이디가 아니면
                result = create_user(username,password,nickname,gender,level) #유저생성함수
                auth.login(request, result)
                return JsonResponse({'works':True})
        except:
            gender = None
            level = None
            print('빈칸일걸?:', gender, level)
            msg = check_blank(username, password, nickname, gender, level)  # 빈칸확인함수
            if msg != '통과':
                print(msg)
                return JsonResponse({'blank': True})

@csrf_exempt
def sign_in(request):
    if request.method == 'GET': #겟요청
        return render(request, 'second.html')  # second.html 렌더링해줌.
    else: # post로 들어왔을때
        select = json.loads(request.body.decode('utf-8'))
        print(select, request)
        username = select['username']
        password = str(select['password'])
        print(username,password)
        msg = login_check_blank(username, password) # 빈칸체크함수
        if msg != '통과':
            return JsonResponse({'blank': True})
        else:#장고의 자격증명을 통과하면 founduser생성되고 통과하지 못하면 None반환
            founduser = auth.authenticate(request, username=username, password=password)
            print(founduser, username, password)
            if founduser is not None:
                auth.login(select, founduser)
                return JsonResponse({'works':True})
            else:#해당하는 유저정보없으면
                return JsonResponse({'no_user': True})


@login_required #로그인해야 로그아웃 가능
def logout(request):
    auth.logout(request)
    return redirect('sign_in')