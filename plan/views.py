from django.shortcuts import render

def plan_view(request):
    return render(request, 'plan.html')
