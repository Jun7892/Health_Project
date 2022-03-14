from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from second.models import User
from django.contrib import auth

from second.services.join_service import create_user, check_blank


def showloginpage(request):
    if request.method == 'GET': #로그아웃 같은상황으로 이쪽으로 던저주게 되면
        return render(request, 'second.html') #second.html 렌더링해줌.

@csrf_exempt
def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = str(request.POST['password'])
        nickname = request.POST['nickname']
        gender = request.POST.get('gender') #체크박스를 아무것도 선택하지 않았을때 값이없기때문에 에러가남.
        level = request.POST.get('level') # request.POST.get('키값')으로 받아오면 none값이 뜸
        print(gender, level)

        msg = check_blank(username,password,nickname,gender,level) #빈칸확인함수
        if msg != '통과':
            print(msg)
            return JsonResponse({'error': msg})
        else:#빈칸이 아니면
            founduser= User.objects.filter(username=username)
            if len(founduser) > 0: #같은아이디가 있을때.
                return JsonResponse({'error': '해당아이디는 이미 존재합니다.'}) #이거 표시할 곳 필요
            else: #중복아이디가 아니면
                result = create_user(username,password,nickname,gender,level)
                auth.login(request, result) #ajax가 응답을 기다릴까봐 걱정.....
                return redirect('main')


def sign_in(request):
    #장고의 자격증명을 통과하면 founduser생성되고 통과하지 못하면 None반환
    founduser = auth.authenticate(request,
                                  username=request.POST['username'],
                                  password=request.POST['password'])
    if founduser is not None:
        auth.login(request, founduser)
        redirect('main')
    else:#해당하는 유저정보없으면
        return render(request, 'second.html', {'error':'id, pw를 확인하세요'})#이것도 표시할 곳 필요할듯
    if request.method == 'POST':
        #장고의 자격증명을 통과하면 founduser생성되고 통과하지 못하면 None반환
        founduser = auth.authenticate(request,
                                      username=request.POST['username'],
                                      password=request.POST['password'])
        if founduser is not None:
            auth.login(request, founduser)
            return redirect('main')
        else:#해당하는 유저정보없으면
            return render(request, 'second.html', {'error':'id, pw를 확인하세요'})#이것도 표시할 곳 필요할듯

@login_required #로그인해야 로그아웃 가능
def logout(request):
    auth.logout(request)
    return redirect('showloginpage')