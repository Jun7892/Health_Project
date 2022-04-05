from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from plan.models import Plan
from second.models import User
import calendar

#달력 보여줄수 있게
def plan_view(request):
    all_plan = Plan.objects.all()
    context = {
        "events":all_plan,
    }
    return render(request, 'plan.html',context)


def all_events(request):
    all_plan = Plan.objects.all()
    out = []
    for event in all_plan:
        out.append({
            'title': event.name,
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),
        })

    return JsonResponse(out, safe=False)


@login_required(login_url='sign_in') # 유저에 맞는 Event불러올 수 있게 작업중
def add_event(request, id):
    try:
        start = request.GET.get("start", None)
        end = request.GET.get("end", None)
        title = request.GET.get("title", None)
        event = Plan(name=str(title), start=start, end=end)
        event.save()
        data = {}
        return JsonResponse(data)
    except:
        return render(request, 'plan.html')

@login_required(login_url='sign_in')
def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Plan.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)

@login_required(login_url='sign_in')
def remove(request):
    event = Plan.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)
