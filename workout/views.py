from django.shortcuts import render

def workout_view(request):
    return render(request, 'workout.html')
