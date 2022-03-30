from django.contrib.auth.decorators import login_required
from django.db.models import Q, QuerySet
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.contrib import messages
from commu.models import Article
from mypage.services.profile_service import get_profile_img_src, profile_update
from second.models import User
from django.core.paginator import Paginator


def item_view(request):
    return render(request, 'item.html')


# @login_required(login_url='sign_in')
def mypage(request, id):
    login_user = request.user  # 접속한 유저의 정보들고있음
    user = User.objects.get(id=id)  # 마이페이지의 유저
    user_list = User.objects.filter(is_superuser=0).all().exclude(username=user.username)  # 로그인한 사용자와 admin계정 제외한 유저리스트
    follow_list = User.objects.get(id=user.id).follow.all()
    another_user_list = user_list.difference(follow_list)  # 나와, 내가 팔로우한 사람을 제외한 모든사람의 리스트

    page = request.GET.get("page")
    article_list = Article.objects.filter(author_id=user.id).order_by("-created_at")  # 생성시간 역순으로 모두불러오기
    paginator = Paginator(article_list, 10)  # 게시글리스트를 한 페이지에 10개씩 불러오는 페이지네이터 정의
    articles = paginator.get_page(page)  # 현재 페이지에 표시될 댓글들을 넘겨줌
    print(articles, article_list)
    doc = {
        'user': user,
        'login_user': login_user,
        'another_user_list': another_user_list,
        'follow': follow_list,
        'articles':articles,
        'article_list':article_list
    }
    if request.method == 'GET':
        return render(request, 'mypage/mypage.html', doc)
    else:
        return redirect('mypage', login_user.id)


# @login_required(login_url='sign_in')
def editprofile(request, id):
    if request.method == 'POST':
        login_user = request.user  # 접속한 유저의 정보들고있음
        user = User.objects.get(id=id)  # 프로필변경페이지 유저
        if login_user.id == user.id:  # 프로필변경하기
            try:
                nickname = request.POST['nickname']
                level = request.POST['level']  # 얘는 다행히 선택 안할 수가 없다.
                print(level)
                if nickname == '':
                    messages.info(request, '닉네임은 빈칸으로 입력할 수 없어요')
                    return redirect('mypage', login_user.id)
                elif nickname != '':
                    user.nickname = nickname
                    user.level = level
                    user.save()
                    img_file = request.FILES['file']
                    filepath = get_profile_img_src(login_user, img_file)
                    profile_update(login_user, filepath)
                    return redirect('mypage', login_user.id)  # 마이페이지로
            except:  # 사진도 선택안했으면 그냥 유지
                print('여기아닐껄?')
                return redirect('mypage', login_user.id)
        else:  # 응 돌아가
            print('여기?')
            return redirect('mypage', login_user.id)
    else:  # 겟요청이면 그냥 메인으로 돌려보냄
        return redirect('/main/')


# @login_required(login_url='sign_in')
def reset_email(request, id):
    login_user = request.user
    try:
        user = User.objects.get(id=id)  # 마이페이지의 유저
    except User.DoesNotExist:
        return redirect('reset_email', login_user.id)
    doc = {
        'login_user': login_user,
        'user': user,
    }
    if request.method == "GET":
        if login_user != user:  # 다른사람 pk값입력해서 들어가면 본인 이메일 변경페이지로 던져줌
            messages.error(request, '잘못된 요청입니다.')
            return redirect('reset_email', login_user.id)
        else:
            return render(request, 'mypage/reset_email.html', doc)

    else:  # post요청
        if login_user != user:  # 자기이메일은 자기만 바꿀수 있어야함
            messages.error(request, '잘못된 요청입니다.')
            return redirect('reset_email', login_user.id)
        else:
            try:
                email = request.POST['email']
                if email == "":
                    messages.error(request, '이메일을 입력해주세요.')
                    return redirect('reset_email', login_user.id)
                else:
                    login_user.email = email
                    login_user.full_clean()  # 여기서 한번더 검사? 통과못하면 except로 빠짐
                    # 중복되지 않은 이메일인지도 확인해야해!!
                    same_email_user = User.objects.filter(email=email).exclude(username=login_user.username)
                    if len(same_email_user) == 0:
                        login_user.save()
                        return redirect('mypage', login_user.id)
                    else:
                        messages.error(request, '이미 해당이메일로 가입한 유저가있습니다. 다른이메일로 입력해주세요.')
                        return redirect('reset_email', login_user.id)
            except ValidationError:
                messages.error(request, '유효한 이메일형식으로 입력해주세요.')
                return redirect('reset_email', login_user.id)


# @login_required(login_url='sign_in')
def user_follow(request, id):  # 팔로우할 사람의 id
    user = request.user  # 지금 접속한 사용자
    click_user = User.objects.get(id=id)  # 클릭한 유저
    if user != click_user:  # 내가 나를 팔로우하지 않도록
        url = request.META['HTTP_REFERER']  # 와 이거 대박
        print(url)
        if user in click_user.followee.all():  # 접속한 유저가 클릭한 유저를 팔로우 하고있었다면
            click_user.followee.remove(user)  # 클릭한 유저의 followee에서 user 제거
        else:  # 팔로우하고 있지 않았다면
            click_user.followee.add(user)  # 클릭한 유저의 followee에 user추가~!
        return redirect(url)


# @login_required(login_url='sign_in')
def show_follow(request, id):
    login_user = request.user  # 접속한 유저
    user = User.objects.get(id=id)  # 마이페이지의 유저
    follow_list = User.objects.get(id=user.id).follow.all()
    followee_list = User.objects.get(id=user.id).followee.all()
    user_list = User.objects.filter(is_superuser=0).all().exclude(username=user.username)  # 로그인한 사용자와 admin계정 제외한 유저리스트
    another_user_list = user_list.difference(follow_list)  # 나와, 내가 팔로우한 사람을 제외한 모든사람의 리스트
    doc = {
        'user': user,
        'login_user': login_user,
        'follow_list': follow_list,
        'followee_list': followee_list,
        'another_user_list': another_user_list,
    }
    return render(request, 'mypage/follow_detail.html', doc)


def user_search(request):
    if request.method == 'POST':
        login_user = request.user
        user_list = User.objects.order_by("nickname").all()
        try:
            keyword = request.POST['user_search']
            search_result_list = user_list.filter(Q(username__icontains=keyword) | Q(nickname__icontains=keyword))
            if keyword == "":
                messages.error(request, '검색어를 입력하세요')
                return render(request, 'mypage/user_search_result.html')
            elif search_result_list.exists():
                paginator = Paginator(search_result_list, 10)  # 유저 한 페이지에 10명씩 불러오는 페이지네이터 정의
                page = request.GET.get('page')
                members = paginator.get_page(page)
                doc = {
                    'login_user': login_user,
                    'members': members
                }
                return render(request, 'mypage/user_search_result.html', doc)
            else: #키워드 없을때
                raise ValueError
        except ValueError:
            messages.info(request, '일치하는 유저가 없습니다.')
            return render(request, 'mypage/user_search_result.html')
    else:
        return redirect('mypage')