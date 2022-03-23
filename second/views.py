from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ValidationError
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from second.models import User
from django.contrib import auth
import json

from second.services.join_service import create_user
from second.services.login_service import login_check_blank
from second.services.profile_service import get_profile_img_src, profile_update
from django.contrib import messages
from django.contrib.auth import views as auth_views, authenticate
from plz import settings


def sign_up(request):
    select = json.loads(request.body.decode('utf-8'))
    print(select)
    if request.method == 'POST':
        username = select['username']
        password = str(select['password'])
        nickname = select['nickname']
        email = select['email']
        if username == '' or password =='' or nickname == '' or email == '' or not select['gender'] or not select['level']:
            return JsonResponse({'blank': True})
        else:
            gender = select['gender']
            level = select['level']
            print('빈칸통과!:', gender, level)
            founduser = User.objects.filter(username=username)
            existemail = User.objects.filter(email=email)
            if len(founduser) > 0:  # 같은아이디가 있을때.
                print('여기서 걸리니?:', 'founduser')
                return JsonResponse({'existid': True})
            elif existemail: #같은 이메일로 가입하면 에러메세지
                return JsonResponse({'existemail': True})
            else:  # 중복아이디/이메일이 아니면
                try:
                    print('?')
                    result =create_user(username=username, password=password, nickname=nickname, email=email, gender=gender,level=level)
                    result.full_clean() #얘가 이메일 유효성검사해줌
                    auth.login(request, result)
                    return JsonResponse({'works': True})

                except ValidationError: #이메일 유효성 검사 통과못했을때
                    print('갑자기?')
                    user=User.objects.get(username=username)
                    user.delete() #생성했던 유저 다시 삭제
                    return JsonResponse({'invalid_email': True})


def sign_in(request):
    if request.method == 'GET': #겟요청
        return render(request, 'second.html')  # second.html 렌더링해줌.
    else: # post로 들어왔을때
        select = json.loads(request.body.decode('utf-8'))
        username = select['username']
        password = select['password']
        msg = login_check_blank(username, password) # 빈칸체크함수
        if msg != '통과':
            return JsonResponse({'blank': True})
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return JsonResponse({'works': True})
            # if User.objects.filter(username=username).exists(): #로그인하고자하는 아이디를 가진 유저가 있다면
            #     user = User.objects.get(username=username)
            #     result = authenticate(request, username=username, password=password)
            #     # result = check_password_correct(password,user.password)#패스워드일치여부 판별
            #     if result == True:
            #         auth.login(request, user)
            #         return JsonResponse({'works':True})
            #     else:
            #         print(result)
            #         return JsonResponse({'wrong_pw': True})
            # else:#해당하는 유저정보없으면
            #     return JsonResponse({'no_user': True})


@login_required #로그인해야 로그아웃 가능
def logout(request):
    auth.logout(request)
    return redirect('sign_in')

def find_id(request):
    if request.method == 'GET':
        return render(request, 'login/find_id.html')
    if request.method == "POST":
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
            if user is not None:
                message = messages.info(request, f'당신의 아이디는 {user.username} 입니다.')
                return redirect('/second/find_id', messages=message)
        except User.DoesNotExist:
                print('여기')
                message = messages.warning(request, '해당 이메일로 가입한 아이디가 없습니다.')
                return redirect('/second/find_id', messages=message)

def send_email(request):
    from django.core.mail import EmailMessage
    email = EmailMessage()
    email.subject = 'test'
    email.body = 'test mail'
    email.from_email= settings.EMAIL_HOST_USER
    email.to = ['']
    email.send()

def password_reset(request):
    if request.method == 'GET':
        return render(request, 'login/reset_pw.html')
    else:#post요청일때
        username = request.POST['username']
        email = request.POST['email']
        if username == '' or email == '':
            message = messages.warning(request, '빈칸을 입력했는지 확인하세요')
            return redirect('/second/password_reset/', messages=message)
        else:#빈칸아닐때
            try:
                user = User.objects.get(username=username)
                if user.email == email:
                    print('여기일텐데....?')
                    title = '[비밀번호 재설정 요청] Longevity홈페이지에서 보낸 메일입니다.'
                    context = {
                                "email":user.email,
                                "domain": '127.0.0.1:8000',#도메인 이름으로 나중에 변경 settings.HOSTNAME,
                                "site_name": '10장생 프로젝트',
                                # MTE4 토큰보내줄거면
                                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                                "user": user,
                                # Return a token that can be used once to do a password reset for the given user.
                                'token': default_token_generator.make_token(user),
                                "protocol": 'http', #"로컬": 'http', #도메인: https
                    }
                    template = render_to_string('login/email.html', context)
                    try:
                        print('오긴왔니?')
                        send_mail(title, template ,settings.EMAIL_HOST_USER, [user.email])
                        print('잘됐니?')
                        message = messages.info(request, 'ok')
                        return redirect('/second/password_reset/done/')
                    except:
                        print('안됐니?')
                        message = messages.debug(request, '잘못된 요청입니다.')
                        return redirect('/second/password_reset/', messages=message)

                else: #id에 입력된 이메일과 입력한 이메일이 같지 않으면 ValueError일으킴
                    raise ValueError
            except User.DoesNotExist:
                print('어디있니?')
                message = messages.error(request, '해당 아이디로 가입한 유저가 존재하지 않습니다.')
                return redirect('/second/password_reset/', messages=message)
            except ValueError:
                print('여기니?')
                message = messages.info(request, '아이디의 이메일정보와 입력한 이메일이 일치하지 않습니다.')
                return redirect('/second/password_reset/', messages=message)

def email_send_success(request):
    return render(request, 'login/password_reset_email.html')


# @login_required(login_url:'sign_in')
def testmypage(request,id):
    login_user = request.user  # 접속한 유저의 정보들고있음
    user = User.objects.get(id=id) #마이페이지의 유저
    user_list = User.objects.filter(is_superuser=0).all().exclude(username=user.username)  # 로그인한 사용자와 admin계정 제외한 유저리스트
    follow_list = User.objects.get(id=user.id).follow.all()
    another_user_list = user_list.difference(follow_list)  # 나와, 내가 팔로우한 사람을 제외한 모든사람의 리스트
    if request.method == 'GET':
        return render(request, 'commu/testmypage.html', {'user':user, 'login_user':login_user ,'another_user_list':another_user_list})
    else:# 프로필 변경요청
        nickname= request.POST['nickname']
        if nickname == "" or MultiValueDictKeyError(KeyError): #닉네임 공백이면
            try:#사진 선택한걸로 바꿔주거나
                img_file = request.FILES['file']
                filepath = get_profile_img_src(login_user, img_file)
                profile_update(login_user, nickname, filepath)
                return redirect('test', login_user.id)#마이페이지로
            except: #사진도 선택안했으면 그냥 유지
                return redirect('test', login_user.id) #나중에 마이페이지에 해당하는것으로 변경하기


# @login_required(login_url:'sign_in')
def user_follow(request, id):
    user = request.user#지금 접속한 사용자
    click_user = User.objects.get(id=id) #클릭한 유저
    if user in click_user.followee.all(): #접속한 유저가 클릭한 유저를 팔로우 하고있었다면
        click_user.followee.remove(user)#클릭한 유저의 followee에서 user 제거
    else: #팔로우하고 있지 않았다면
        click_user.followee.add(user)#클릭한 유저의 followee에 user추가~!
    return redirect('test', user.id)


# @login_required(login_url:'sign_in')
def show_follow(request, id):
    login_user = request.user
    user = User.objects.get(id=id)
    follow_list = User.objects.get(id=user.id).follow.all()
    followee_list = User.objects.get(id=user.id).followee.all()
    return render(request, 'commu/follow_detail.html', {'user':user,'follow_list':follow_list, 'followee_list':followee_list, 'login_user':login_user})