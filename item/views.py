from django.shortcuts import render

def item_view(request):
    return render(request, 'item.html')