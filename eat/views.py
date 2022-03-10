from django.shortcuts import render

def eat_view(request):
    return render(request, 'eat.html')
