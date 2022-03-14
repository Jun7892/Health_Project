from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from second.models import User
from django.contrib import auth


def showloginpage(request):
    if request.method == 'GET': #로그아웃 같은상황으로 이쪽으로 던저주게 되면
        return render(request, 'second.html') #second.html 렌더링해줌.

def sign_up(request):
    if request.method == 'POST':
        founduser= User.objects.filter(username=request.POST['username'])
        if len(founduser) > 0: #같은아이디가 있을때.
            return render(request, 'second.html', {'error':'해당아이디는 이미 존재합니다.'}) #이거 표시할 곳 필요할듯
        else:
            print(request.POST)
            new_user = User.objects.create(#authmodel에서 id는 pk값으로 쓰기때문에 username을 아이디 저장하는 곳으로 사용.
                                            username=request.POST['username'],
                                            password=str(request.POST['password']),
                                            nickname= request.POST['nickname'],
                                            gender= request.POST['gender'],
                                            level= request.POST['level']
                        ) # 유저생성하고 바로 로그인시켜버렷
            auth.login(request, new_user)
            return redirect('main')
    #만약 get요청으로 들어오면 해당url은 모달창과 연결할 수 있나?

@csrf_exempt
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

@login_required #로그인해야 로그아웃 가능
def logout(request):
    auth.logout(request)
    return redirect('showloginpage')