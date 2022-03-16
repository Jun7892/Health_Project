from django.shortcuts import render

def commu_view(request):
    return render(request, 'commu.html')