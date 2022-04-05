from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from workout.models import Exercise
from workout.services.level_service import boy_youth_level_service, girl_youth_level_service, man_senior_level_service, \
    woman_senior_level_service, boy_student_level_service, girl_student_level_service, man_adult_level_service, \
    woman_adult_level_service
from second.models import User
from workout.services.make_random_warmup import make_youth_random_warmup, make_random_main, get_main_video_id, \
    get_warm_up_video_id, make_random_others_warmup


@login_required(login_url='sign_in')
def workout_view(request):
    user = request.user
    who = User.objects.get(username=user.username)
    if request.method == 'GET':
        if who.level == "":
            return render(request, 'workout/nolevel.html')
        else:  # 유저 등급주어졌다면 운동페이지 보여줘야해
            user_match_exercise_list = Exercise.objects.filter(gender=who.gender, level=who.level, age=who.age)
            picked_exercise = user_match_exercise_list.order_by('?').first()
            # picked_exercise=Exercise.objects.get(id=2833)
            user_warm_up = picked_exercise.get_warm_up()  # get_warm_up으로 꺼내야 한글로나옴
            user_main = picked_exercise.get_main()
            warm_up_db_list = user_warm_up.split(',')
            main_db_list = user_main.split(',')
            grade = who.level.replace('등급', "")

            # print('어디서 오류나나보쟈',picked_exercise, warm_up_db_list,main_db_list)
            #데이터셋자체가 둘다없는 경우는 없음.
            #준비운동이 없을때
            if len(user_warm_up) == 0 :
                #준비운동 정해진 리스트에서 던져주고

                # 본운동은 데이터셋에 저장된 거 검색어로 불러오기
                if who.age == '유소년':
                    if who.level == '3등급':
                        warm_up_list = make_youth_random_warmup(grade)
                        main_list = get_main_video_id(main_db_list, who.age)
                        if len(main_list) == 0:
                            main_list = make_random_main(who.age, grade)
                        return render(request, 'workout.html', {'warm_up_list': warm_up_list, 'main_list': main_list})
                    elif who.level == '2등급':
                        warm_up_list = make_youth_random_warmup(grade)
                        main_list = get_main_video_id(main_db_list, who.age)
                        if len(main_list) == 0:
                            main_list = make_random_main(who.age, grade)
                        return render(request, 'workout.html', {'warm_up_list': warm_up_list, 'main_list': main_list})
                    else:  # 유소년 1등급
                        warm_up_list = make_youth_random_warmup(grade)
                        main_list = get_main_video_id(main_db_list, who.age)
                        if len(main_list) == 0:
                            main_list = make_random_main(who.age, grade)
                        return render(request, 'workout.html', {'warm_up_list': warm_up_list, 'main_list': main_list})
                else:  # 청소년/성인/노인
                    warm_up_list = make_random_others_warmup(who.age)
                    main_list = get_main_video_id(main_db_list, who.age)
                    if len(main_list) == 0:
                        main_list = make_random_main(who.age, grade)
                    return render(request, 'workout.html', {'warm_up_list': warm_up_list, 'main_list': main_list})
            # 본운동이 없을때
            elif len(user_main) == 0:
                # 준비운동은 DB에있는거 그대로 던져주고, 본운동은 기존 나이대/등급별 리스트 랜덤던져줌
                warm_up_list = get_warm_up_video_id(warm_up_db_list, who.age)
                main_list = make_random_main(who.age, grade)
                if len(warm_up_list) == 0:
                    if who.age == '유소년':
                        warm_up_list = make_youth_random_warmup(grade)
                    else:  # 청소년/성인/노인
                        warm_up_list = make_random_others_warmup(who.age)
                return render(request, 'workout.html', {'warm_up_list': warm_up_list, 'main_list': main_list})

            else:  # 준비운동 있고, 본운동 있고
                warm_up_list = get_warm_up_video_id(warm_up_db_list, who.age)
                main_list = get_main_video_id(main_db_list, who.age)
                if len(warm_up_list) == 0 and len(main_list) == 0:
                    if who.age == '유소년':
                        warm_up_list = make_youth_random_warmup(grade)
                        main_list = make_random_main(who.age, grade)
                    else:  # 청소년/성인/노인
                        warm_up_list = make_random_others_warmup(who.age)
                        main_list = make_random_main(who.age, grade)
                elif len(warm_up_list) == 0:
                    if who.age == '유소년':
                        warm_up_list = make_youth_random_warmup(grade)
                    else:  # 청소년/성인/노인
                        warm_up_list = make_random_others_warmup(who.age)
                elif len(main_list) == 0:
                    main_list = make_random_main(who.age, grade)
                print(warm_up_list, main_list, '준비운동길이', len(warm_up_list), '메인운동길이', len(main_list))
                return render(request, 'workout.html', {'warm_up_list': warm_up_list, 'main_list': main_list})


# 측정후에도 다시하고싶을수도 있으니까 나이대별 측정페이지 보여줄수 있음
@login_required(login_url='sign_in')
def age_different_show_page(request):
    user = request.user
    age_range = user.age
    if age_range == '유소년':
        return render(request, 'workout/youth_level_test.html')
    elif age_range == '노인':
        return render(request, 'workout/senior_level_test.html')
    else:
        return render(request, 'workout/student_and_adult_level_test.html')


@login_required(login_url='sign_in')
def level_confirm(request, id):
    login_user = request.user
    user = User.objects.get(id=id)
    age_range = user.age
    real_age = user.first_name
    if request.method == 'POST':
        try:
            count = request.POST['count']
            if login_user == user:
                if age_range == '유소년':
                    if user.gender == '남자':
                        grade = boy_youth_level_service(int(real_age), int(count), user)  # 등급여기서 나눠서 저장해줌
                        return render(request, 'workout/show_level.html', {'grade': grade, 'user': login_user})
                    elif user.gender == '여자':
                        grade = girl_youth_level_service(int(real_age), int(count), user)
                        return render(request, 'workout/show_level.html', {'grade': grade, 'user': login_user})
                elif age_range == '청소년':
                    if user.gender == '남자':
                        grade = boy_student_level_service(int(real_age), int(count), user)  # 등급여기서 나눠서 저장해줌
                        return render(request, 'workout/show_level.html', {'grade': grade, 'user': login_user})
                    elif user.gender == '여자':
                        grade = girl_student_level_service(int(real_age), int(count), user)
                        return render(request, 'workout/show_level.html', {'grade': grade, 'user': login_user})
                elif age_range == '성인':
                    if user.gender == '남자':
                        grade = man_adult_level_service(int(real_age), int(count), user)
                        return render(request, 'workout/show_level.html', {'grade': grade, 'user': login_user})
                    elif user.gender == '여자':
                        grade = woman_adult_level_service(int(real_age), int(count), user)
                        return render(request, 'workout/show_level.html', {'grade': grade, 'user': login_user})
                elif age_range == '노인':
                    if user.gender == '남자':
                        grade = man_senior_level_service(int(real_age), int(count), user)
                        return render(request, 'workout/show_level.html', {'grade': grade, 'user': login_user})
                    elif user.gender == '여자':
                        grade = woman_senior_level_service(int(real_age), int(count), user)
                        return render(request, 'workout/show_level.html', {'grade': grade, 'user': login_user})
            else:
                return redirect('age_different_show_page')
        except MultiValueDictKeyError(KeyError):  # 등급받고서 또 주소창에서 엔터치면
            return redirect('workout')
    else:
        return redirect('workout')
