from django.shortcuts import render, redirect

from workout.models import Exercise
from workout.services.get_youtube_video_id import get_video_list
from workout.services.level_service import boy_youth_level_service, girl_youth_level_service, man_senior_level_service, \
    woman_senior_level_service, boy_student_level_service, girl_student_level_service, man_adult_level_service, \
    woman_adult_level_service
from second.models import User

def workout_view(request):
    user = request.user
    who = User.objects.get(username=user.username)
    if request.method == 'GET':
        if who.level == "":
            return render(request, 'workout/nolevel.html')
        else: #유저 등급주어졌다면 운동페이지 보여줘야해
            user_match_exercise_list= Exercise.objects.filter(gender=who.gender, level=who.level,age=who.age)
            # picked_exercise =user_match_exercise_list.order_by('?').first()
            picked_exercise = user_match_exercise_list[300] #준비운동 없는 친구
            user_warm_up = picked_exercise.get_warm_up() #get_warm_up으로 꺼내야 한글로나옴
            user_main = picked_exercise.get_main()
            print(user_main)
            if len(user_warm_up) == 0: #나중에 연령대별로 나누든지...
                result = get_video_list('안동국민체력센터 '+'운동전 스트레칭') #이래야 얘가나오네
                video_id_list=[]
                video_id_list.append(result)
                # print('이게결과:',result, '얘는리스트:',video_id_list)

                return render(request, 'workout.html', {'warm_up_list':video_id_list})







            else: # 준비운동 있으면
                split_warm_up = user_warm_up.split(',')
                video_id_list=[]
                for i in range(len(split_warm_up)):
                    result = get_video_list('국민체력100_운동처방전 '+who.age+" "+split_warm_up[i])
                    video_id_list.append(result)
                return render(request, 'workout.html', {'warm_up_list': video_id_list})

            # picked_exercise= user_match_exercise_list[50] #여러개 있는 친구
            # picked_exercise1 = user_match_exercise_list[0] #한개만 있는 친구
            # picked_zero = user_match_exercise_list[300] #준비운동 없는 친구
            # print(picked_zero.get_warm_up(), '갯수:',len(picked_zero.get_warm_up())) # 없는건 len 0으로 나옴



            # print(picked_exercise1.get_warm_up().split(',')) #,으로 나눠서
            # print('len으로세기:',len(picked_exercise1.get_warm_up().split(','))) #len으로세면 걷기만있을때 1개로나옴

            # picked_exercise.get_warm_up().split(',')
            # print(picked_exercise, 'id값은:', picked_exercise.get_warm_up())
            # print(picked_exercise.get_warm_up().split(','))
            # exercise = Exercise.objects.get(id=1)
            # exercise.warm_up = exercise.get_warm_up()
            # split_warm_up = exercise.warm_up.split(',')


            #없으면 len()처리했을때 0임 준비운동없을때 보여줄 동영상 주소 하나 던져주자

            # print(exercise.warm_up, '길이는:',len(exercise.warm_up))
            # print(split_warm_up, '길이는:', len(split_warm_up))
            return render(request, 'workout.html')

#측정후에도 다시하고싶을수도 있으니까 나이대별 측정페이지 보여줄수 있음
def age_different_show_page(request):
    user = request.user
    age_range= user.age
    if age_range == '유소년':
        return render(request, 'workout/youth_level_test.html')
    elif age_range == '노인':
        return render(request, 'workout/senior_level_test.html')
    else:
        return render(request, 'workout/student_and_adult_level_test.html')


def level_confirm(request, id):
    login_user = request.user
    user = User.objects.get(id=id)
    age_range = user.age
    real_age = user.first_name
    count = request.POST['count']
    if request.method == 'POST':
        if login_user == user:
            if age_range == '유소년':
                if user.gender == '남자':
                    boy_youth_level_service(int(real_age), int(count), user) # 등급여기서 나눠서 저장해줌
                    return render(request, 'workout/show_level.html', {'user': login_user})
                elif user.gender == '여자':
                    girl_youth_level_service(int(real_age), int(count), user)
                    return render(request, 'workout/show_level.html', {'user': login_user})
            elif age_range == '청소년':
                if user.gender == '남자':
                    boy_student_level_service(int(real_age), int(count), user)  # 등급여기서 나눠서 저장해줌
                    return render(request, 'workout/show_level.html', {'user': login_user})
                elif user.gender == '여자':
                    girl_student_level_service(int(real_age), int(count), user)
                    return render(request, 'workout/show_level.html', {'user': login_user})
            elif age_range == '성인':
                if user.gender == '남자':
                    man_adult_level_service(int(real_age), int(count), user)
                    return render(request, 'workout/show_level.html', {'user': login_user})
                elif user.gender == '여자':
                    woman_adult_level_service(int(real_age), int(count), user)
                    return render(request, 'workout/show_level.html', {'user': login_user})
            elif age_range == '노인':
                if user.gender == '남자':
                    man_senior_level_service(int(real_age), int(count), user)
                    return render(request, 'workout/show_level.html', {'user': login_user})
                elif user.gender == '여자':
                    woman_senior_level_service(int(real_age), int(count), user)
                    return render(request, 'workout/show_level.html', {'user': login_user})
        else:
            return redirect('age_different_show_page')
    else:
        return redirect('age_different_show_page')
