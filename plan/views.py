from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from plan.models import Plan
from second.models import User
import calendar


def plan_view(request):
    return render(request, 'plan.html')


@login_required(login_url='sign_in') # 유저에 맞는 todo불러올 수 있게 작업중
def plan_view2(request, id):
    # try:
    #     my_plan = Plan.objects.get(id=id)
    #     return render(request, 'plan.html', {'plan': my_plan})
    # except:
    return render(request, 'plan.html')


# def create_to_do(request):
#     if request.method == 'POST':
#         user = request.user
#         to_do = request.POST.get('to_do', '')
#         my_plan = Plan.objects.create(user=user,to_do=to_do)
#         my_plan.save()
#         return render(request, 'plan.html')
#
