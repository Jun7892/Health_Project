from django.shortcuts import render, redirect
from workout.services.level_service import boy_youth_level_service, girl_youth_level_service, man_senior_level_service, \
    woman_senior_level_service
from second.models import User

def workout_view(request):
    user = request.user
    if request.method == 'GET':
        if user.level == "":
            return render(request, 'workout/nolevel.html')
        else: #유저 등급주어졌다면 운동페이지 보여줘야해
            return render(request, 'workout.html')


def age_different_show_page(request):
    user = request.user
    age_range= user.age
    if age_range == '유소년':
        return render(request, 'workout/youth_level_test.html')
    elif age_range == '노인':
        return render(request, 'workout/senior_level_test.html')
    elif age_range == '청소년':
        return render(request, 'workout/senior_level_test.html')


def youth_and_old_level_confirm(request, id):
    login_user = request.user
    user = User.objects.get(id=id)
    age_range = user.age
    real_age = user.first_name
    count = request.POST['count']
    if request.method == 'POST':
        if login_user == user:
            if age_range == '유소년':
                if user.gender == '남자':
                    boy_youth_level_service(real_age, int(count), user) # 등급여기서 나눠서 저장해줌
                    return render(request, 'workout/show_level.html', {'user': login_user})
                elif user.gender == '여자':
                    girl_youth_level_service(real_age, int(count), user)
                    return render(request, 'workout/show_level.html', {'user': login_user})
            elif age_range == '노인':
                if user.gender == '남자':
                    man_senior_level_service(real_age, int(count), user)
                    return render(request, 'workout/show_level.html', {'user': login_user})
                elif user.gender == '여자':
                    woman_senior_level_service(real_age, int(count), user)
                    return render(request, 'workout/show_level.html', {'user': login_user})
        else:
            return redirect('age_different_show_page')


