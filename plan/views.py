from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from plan.models import Plan

from second.models import User

def plan_view(request):
    return render(request, 'plan.html')

@login_required(login_url='sign_in') # 유저에 맞는 todo불러올 수 있게 작업중
def plan_view(request, id):
    user = User.objects.get(id=id)
    all_to_do= Plan.objects.filter(user=user) #통째로 던져도 되나요......?
    return render(request, 'plan.html', {'all_to_do':all_to_do})