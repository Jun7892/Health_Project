from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from plan.models import Plan
from second.models import User
import calendar

def plan_view(request):
    return render(request, 'plan.html')

@login_required(login_url='sign_in') # 유저에 맞는 todo불러올 수 있게 작업중
def plan_view2(request, id):
    # if request.method == 'GET':
    #
    # #해당달의 마지막 일자 알 수 있음
    # #ajax에서 해당달력의 년월 정보 던져주면
    # # year = request.POST[]
    # # month = request.POST[]
    # # last_day = calendar.monthrange(year, month)[1] #해당월의 마지막 날짜 구할 수 있음
    #
    # user = User.objects.get(id=id)
    # Plan.objects.filter(user)
    #
    #
    #
    # all_to_do= Plan.objects.filter(user=user) #통째로 던져도 되나요......?
    return render(request, 'plan.html')