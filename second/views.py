from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from second.models import User
from django.contrib import auth
from second.services.join_service import create_user, check_blank
import json
from second.services.login_service import login_check_blank, check_password_correct
# from second.services.profile_service import get_profile_img_src, profile_update


@csrf_exempt
def sign_up(request):
    select = json.loads(request.body.decode('utf-8'))
    print(select)
    if request.method == 'POST':
        username = select['username']
        password = str(select['password'])
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
        else:
            if User.objects.filter(username=username).exists(): #로그인하고자하는 아이디를 가진 유저가 있다면
                user = User.objects.get(username=username)
                result = check_password_correct(password,user.password)#패스워드일치여부 판별
                if result == True:
                    auth.login(request, user)
                    return JsonResponse({'works':True})
                else:
                    print(result)
                    return JsonResponse({'wrong_pw': True})
            else:#해당하는 유저정보없으면
                return JsonResponse({'no_user': True})


@login_required #로그인해야 로그아웃 가능
def logout(request):
    auth.logout(request)
    return redirect('sign_in')

# @login_required(login_url:'sign_in')
def testmypage(request):
    login_user = request.user  # 접속한 유저의 정보들고있음
    print(login_user)
    if request.method == 'GET':
        user_list = User.objects.all().exclude(username=login_user.username) #로그인한 사용자 제외한 유저리스트
        return render(request, 'commu/testmypage.html', {'login_user':login_user, 'user_list':user_list})
    else:
        nickname= request.POST['nickname']
        img_file = request.FILES['file']
        print(nickname, img_file)
        #닉네임만 변경시 혹은 프로필사진만 변경시를 따로 나눠줘야함 - 아직작업안함
        try:
            filepath = get_profile_img_src(login_user, img_file)
            profile_update(login_user, nickname, filepath)
            return redirect('test')#마이페이지로
        except:
            print('오류?')#메세지
            return redirect('test') #나중에 마이페이지에 해당하는것으로 변경하기

# @login_required(login_url:'sign_in')
def user_follow(request, id):
    login_user = request.user#지금 접속한 사용자
    click_user = User.objects.get(id=id) #클릭한 유저
    if login_user in click_user.followee.all(): #접속한 유저가 클릭한 유저를 팔로우 하고있었다면
        click_user.followee.remove(login_user)#클릭한 유저의 followee에서 login_user 제거
    else: #팔로우하고 있지 않았다면
        click_user.followee.add(login_user)#클릭한 유저의 followee에 login_user추가~!
    return redirect('test')

def show_follow(request):
    user = request.user
    follow_list = User.objects.get(id=user.id).follow.all()
    followee_list = User.objects.get(id=user.id).followee.all()
    return render(request, 'commu/follow_detail.html', {'follow_list':follow_list, 'followee_list':followee_list})