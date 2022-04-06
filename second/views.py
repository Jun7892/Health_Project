from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.exceptions import ValidationError
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from second.models import User
from django.contrib import auth
import json
from django.contrib import messages
from django.contrib.auth import authenticate
from plz import settings
from second.services import login_check_blank, create_user
from second.services.join_service import change_age


def sign_up(request):
    select = json.loads(request.body.decode('utf-8'))
    # print(select)
    if request.method == 'POST':
        try:
            username = select['username']
            password = str(select['password'])
            nickname = select['nickname']
            email = select['email']
            age = int(select['age'])
            print(age, type(age))
            if username == '' or password =='' or nickname == '' or email == '' or not select['gender'] or age == '':
                return JsonResponse({'blank': True})
            else:
                gender = select['gender']
                # print('빈칸통과!:', gender, age)
                founduser = User.objects.filter(username=username)
                existemail = User.objects.filter(email=email)
                if len(founduser) > 0:  # 같은아이디가 있을때.
                    # print('여기서 걸리니?:', 'founduser')
                    return JsonResponse({'existid': True})
                elif existemail: #같은 이메일로 가입하면 에러메세지
                    return JsonResponse({'existemail': True})
                else:  # 중복아이디/이메일이 아니면
                    try:
                        changed_age = change_age(age) # 나이 '유소년/청소년/성인/노인'으로 변환
                        if changed_age == 'error':
                            return JsonResponse({'noway':True})
                        elif changed_age == 'baby':
                            return JsonResponse({'baby': True})
                        else:
                            result =create_user(username, password, nickname, email, gender, changed_age, age)
                            result.full_clean() #얘가 이메일 유효성검사해줌
                            auth.login(request, result)
                            return JsonResponse({'works': True})
                    except ValidationError: #이메일 유효성 검사 통과못했을때
                        user=User.objects.get(username=username)
                        user.delete() #생성했던 유저 다시 삭제
                        return JsonResponse({'invalid_email': True})
        except ValueError:
            return JsonResponse({'str_age':True})


def sign_in(request):
    if request.method == 'GET': #겟요청
        return render(request, 'second.html')  # second.html 렌더링해줌.
    else: # post로 들어왔을때
        select = json.loads(request.body.decode('utf-8'))
        username = select['username']
        password = str(select['password'])
        msg = login_check_blank(username, password) # 빈칸체크함수
        if msg != '통과':
            return JsonResponse({'blank': True})
        else:
            try:
                founduser = User.objects.get(username=username)
                if founduser is not None:
                    user = authenticate(request, username=username, password=password)
                    if user is not None: #패스워드까지 맞으면
                        auth.login(request, user) #로그인하겠지
                        return JsonResponse({'works': True})
                    else: #패스워드가 틀리면
                        raise ValueError
            except User.DoesNotExist: # founduser가 없으면 이리로옴
                return JsonResponse({'no_user':True})
            except ValueError:
                return JsonResponse({'wrong_pw':True})


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
                messages.info(request, f'당신의 아이디는 {user.username} 입니다.')
                return redirect('/second/find_id')
        except User.DoesNotExist:
            messages.warning(request, '해당 이메일로 가입한 아이디가 없습니다.')
            return redirect('/second/find_id')

def send_email(request): #이메일 서비스 점검용
    from django.core.mail import EmailMessage
    email = EmailMessage()
    email.subject = 'test'
    email.body = 'test mail'
    email.from_email= settings.EMAIL_HOST_USER
    email.to = ['']
    email.send()

def password_reset_mailing(request):
    if request.method == 'GET':
        return render(request, "login/check_ones_email.html")
    else:#post요청일때
        username = request.POST['username']
        email = request.POST['email']
        if username == '' or email == '':
            messages.warning(request, '빈칸을 입력했는지 확인하세요')
            return redirect('/second/password_reset/')
        else:#빈칸아닐때
            try:
                user = User.objects.get(username=username)
                if user.email == email:
                    print('여기일텐데....?')
                    title = '[비밀번호 재설정 요청] Longevity홈페이지에서 보낸 메일입니다.'
                    context = {
                                "email":user.email,
                                "domain": 'https://www.rookieno.com',
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
                        send_mail(title, template ,settings.EMAIL_HOST_USER, [user.email])
                        return redirect('/second/password_reset/done/')
                    except:
                        messages.debug(request, '잘못된 요청입니다.')
                        return redirect('/second/password_reset/')

                else: #id에 입력된 이메일과 입력한 이메일이 같지 않으면 ValueError일으킴
                    raise ValueError
            except User.DoesNotExist:
                messages.error(request, '해당 아이디로 가입한 유저가 존재하지 않습니다.')
                return redirect('/second/password_reset/')
            except ValueError:
                messages.info(request, '아이디의 이메일정보와 입력한 이메일이 일치하지 않습니다.')
                return redirect('/second/password_reset/')

def email_send_success(request):
    return render(request, 'login/success_mailing.html')

def reset_password(request, uidb64, token):
    if request.method =='GET':
        pk = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=pk)
        result = default_token_generator.check_token(user, token)
        print(pk,user)
        print(result)
        if result == True:
            return render(request, 'login/reset_password.html', {'ok':'ok'})
        else:
            messages.info(request, '비밀번호 재설정 유효시간이 지났네요!. 이 메일은 유효하지 않습니다')
            return render(request, 'login/reset_password.html')
    else:#post요청
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        print(password1,password2)
        if password1 and password2:
            if password1 != password2:
                messages.error(request, '입력한 비밀번호가 일치하지 않습니다.')
                return redirect(request.path)
            else:#패스워드 같다면
                try:
                    pk = force_str(urlsafe_base64_decode(uidb64))
                    user = User.objects.get(pk=pk)
                    result = default_token_generator.check_token(user, token)
                    print(result)
                    if result == True: #유효한 유저/토큰이면 True반환
                        user.password = make_password(password2) #create_user할때 장고자체에서 제공하는 패스워드 해시화함수
                        auth.logout(request) # 마이페이지에서도 비밀번호재설정 던져주니까 로그아웃시킴
                        user.save()
                        return render(request, 'login/password_reset_complete.html')
                    else: #유효하지 않으면
                        messages.info(request, '비밀번호변경이 완료되어 이 주소는 유효하지 않습니다.')
                        return render(request, 'login/reset_password.html')
                except:
                    message = messages.warning(request, '뭔가 잘못되었군요! situm26@gmail.com 여기로 메일을 보내주세요!')
                    return redirect(request.path, messages=message)
        else: #비밀번호 하나라도 빈칸이면
            messages.info(request, '빈칸을 입력했어요! 다시입력해주세요')
            return redirect(request.path)


@login_required(login_url='sign_in')
def user_delete(request, id):
    login_user = request.user
    if request.method == "GET":
        try:
            user = User.objects.get(id=id)
            if login_user == user:
                return render(request, 'login/user_delete.html')
            else:
                messages.error(request, '회원탈퇴는 본인만 가능합니다.')
                return redirect('mypage', login_user.id)
        except User.DoesNotExist:
            messages.error(request, '잘못된 접근입니다.')
            return redirect('mypage', login_user.id)
    else: #post요청
        password = str(request.POST['password'])
        if password == '':
            messages.info(request, '비밀번호를 입력해주세요')
            return redirect('user_delete', login_user.id)
        else:
            user = User.objects.get(id=id)
            result = authenticate(request, username=user.username, password=password)
            if result is None:
                messages.error(request, '비밀번호를 정확하게 입력했는지 확인하세요!')
                return redirect('user_delete', login_user.id)
            else:
                if result == login_user:
                    login_user.delete()
                    logout(request)
                    return redirect('first')
                else:
                    messages.error(request, '')
                    return redirect('user_delete', login_user.id)