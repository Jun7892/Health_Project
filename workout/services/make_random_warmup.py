import random

from workout.models import Video_id


def make_youth_random_warmup(grade):
    if grade == '3':
        warm_up_list = []
        youth3_warmup_list = ['13pReCtwYgM', 'cjQJXqVguGY', 'cXQJEYiRnUM', 'ZmUj-E9A44E']
        random_index = random.randrange(1, len(youth3_warmup_list))
        warmup_video_id = youth3_warmup_list[random_index]
        warm_up_list.append(warmup_video_id)
        return warm_up_list
            #성인/노인/ 청소년은 준비운동 같음

    elif grade == '2':
        warm_up_list = []
        youth2_warmup_list = ['13pReCtwYgM','cjQJXqVguGY','cXQJEYiRnUM','J79-J2aQa0s','ZmUj-E9A44E']
        random_index = random.randrange(1, len(youth2_warmup_list))
        warmup_video_id = youth2_warmup_list[random_index]
        warm_up_list.append(warmup_video_id)
        return warm_up_list

    else: #1등급
        warm_up_list = []
        youth1_warmup_list = ['13pReCtwYgM','J79-J2aQa0s','ZmUj-E9A44E','ipB3TD0BpwA']
        random_index = random.randrange(1, len(youth1_warmup_list))
        warmup_video_id = youth1_warmup_list[random_index]
        warm_up_list.append(warmup_video_id)
        return warm_up_list


def make_random_others_warmup(age):
    if age == '청소년':
        warm_up_list = []
        student_warmup_list = ['dsKW-rdjPwA','99D1pWmpBeI','tauWsdpWqI4','ilGxwE4G4-E','0k32Xj_CKk4']
        random_index = random.randrange(1, len(student_warmup_list))
        warmup_video_id = student_warmup_list[random_index]
        warm_up_list.append(warmup_video_id)
        return warm_up_list
    elif age == '성인':
        warm_up_list = []
        adult_warmup_list = ['dsKW-rdjPwA','Tvw42auu5N4','UKQEojC4G9k','_bqes3Cw5ug','yyz_iOD_ZH0']
        random_index = random.randrange(1, len(adult_warmup_list))
        warmup_video_id = adult_warmup_list[random_index]
        warm_up_list.append(warmup_video_id)
        return warm_up_list
    else: #노인
        warm_up_list = []
        senior_warmup_list = ['HzAk4tYsLyU','lq1c54VERbo','Q57q79bL-90','B2OmkH0UNuc','Msubsqnqeo4']
        random_index = random.randrange(1, len(senior_warmup_list))
        warmup_video_id = senior_warmup_list[random_index]
        warm_up_list.append(warmup_video_id)
        return warm_up_list


def get_warm_up_video_id(warm_up_db_list,age):
    warm_up_list = []
    for i in range(len(warm_up_db_list)):  # 반복문돌리고
        result = Video_id.objects.filter(title__contains='['+age+']'+ warm_up_db_list[i])
        print(Video_id.objects.filter(title__contains='[' + age + ']' + warm_up_db_list[i]).exists())
        if Video_id.objects.filter(title__contains='[' + age + ']' + warm_up_db_list[i]).exists():
            warm_up_list.append(result[0].video_id.replace('"',''))
        else:
            pass
    return warm_up_list

def get_main_video_id(main_db_list, age):
    main_list = []
    for i in range(len(main_db_list)):  # 반복문돌리고
        result = Video_id.objects.filter(title__contains='['+age+']'+ main_db_list[i])
        if Video_id.objects.filter(title__contains='[' + age + ']' + main_db_list[i]).exists():
            main_list.append(result[0].video_id.replace('"',''))
        else:
            pass
    return main_list


def make_random_main(age,grade):
    if grade == '3':
        if age == '유소년':
            main_list = []
            youth3_main_list = ['0k32Xj_CKk4','uLnYKa-d-Os','JmPP5cMPlGg','uLnYKa-d-Os','ZzZNhpNcaHQ']
            random_index = random.randrange(1, len(youth3_main_list))
            main_video_id = youth3_main_list[random_index]
            main_list.append(main_video_id)
            return main_list
        elif age == '청소년':
            main_list = []
            student3_main_list = ['0k32Xj_CKk4','hCaIw9L_Pp8','o6ARYhR-gw8','CRMpWponGIc','P968Pd37-NQ']
            random_index = random.randrange(1, len(student3_main_list))
            main_video_id = student3_main_list[random_index]
            main_list.append(main_video_id)
            return main_list
        elif age == '성인':
            main_list = []
            adult3_main_list = ['7Bickpeymew', '-O1lweMLj4E', '-O1lweMLj4E', 'c5kNdIk9jgc', 'sw_4b6GKfnI', 'DT5d9GrbLyg']
            random_index = random.randrange(1, len(adult3_main_list))
            main_video_id = adult3_main_list[random_index]
            main_list.append(main_video_id)
            return main_list
        else:#노인3등급
            main_list = []
            senior3_main_list = ['_0D9iMzntJI','OiXEJ29IVPU','6ws5Ze7ootE','clifZdPnX9E','SuJKMztDB58','6ulvd_mw_uo']
            random_index = random.randrange(1, len(senior3_main_list))
            main_video_id = senior3_main_list[random_index]
            main_list.append(main_video_id)
            return main_list

    elif grade == '2':
        if age == '유소년':
            main_list = []
            youth2_main_list = ['0k32Xj_CKk4','uLnYKa-d-Os','oz9TL60Amb4','0V2O2VnxdCg','JmPP5cMPlGg']
            random_index = random.randrange(1, len(youth2_main_list))
            main_video_id = youth2_main_list[random_index]
            main_list.append(main_video_id)
            return main_list
        elif age == '청소년':
            main_list = []
            student2_main_list = ['hCaIw9L_Pp8','L6o5qmuoxl4','o6ARYhR-gw8','NwcxlUkJems','CRMpWponGIc']
            random_index = random.randrange(1, len(student2_main_list))
            main_video_id = student2_main_list[random_index]
            main_list.append(main_video_id)
            return main_list
        elif age == '성인':
            main_list = []
            adult2_main_list = ['jRK9h4VGECI','-O1lweMLj4E','-O1lweMLj4E','hCJgzZIo7cI','sw_4b6GKfnI','DT5d9GrbLyg','L6o5qmuoxl4']
            random_index = random.randrange(1, len(adult2_main_list))
            main_video_id = adult2_main_list[random_index]
            main_list.append(main_video_id)
            return main_list
        else: #노인2등급
            main_list = []
            senior2_main_list = ['ll_eGqz-yH4','_0D9iMzntJI','6ws5Ze7ootE','clifZdPnX9E','SuJKMztDB58','6ulvd_mw_uo']
            random_index = random.randrange(1, len(senior2_main_list))
            main_video_id = senior2_main_list[random_index]
            main_list.append(main_video_id)
            return main_list

    else: #1등급
        if age == '유소년':
            main_list = []
            youth1_main_list = ['_SPkfAVwR0I','oz9TL60Amb4','0V2O2VnxdCg','JmPP5cMPlGg','3h5HD6IEjqE']
            random_index = random.randrange(1, len(youth1_main_list))
            main_video_id = youth1_main_list[random_index]
            main_list.append(main_video_id)
            return main_list
        elif age == '청소년':
            main_list = []
            student1_main_list = ['hCaIw9L_Pp8','Wz-JIKxiPXk','o6ARYhR-gw8','NwcxlUkJems','CRMpWponGIc']
            random_index = random.randrange(1, len(student1_main_list))
            main_video_id = student1_main_list[random_index]
            main_list.append(main_video_id)
            return main_list
        elif age == '성인':
            main_list = []
            adult1_main_list = ['f-X9yBbSNao', 'C7REZandz0g', 'owKBuruZh6o', 'DuSIEmcodeU', 'Gw73tXd_Wow']
            random_index = random.randrange(1, len(adult1_main_list))
            main_video_id = adult1_main_list[random_index]
            main_list.append(main_video_id)
            return main_list
        else:  # 노인1등급
            main_list = []
            senior1_main_list = ['ll_eGqz-yH4','_0D9iMzntJI','nDxtByfXnzs','ahOYqLVAxwI','fbRvjzl_RIE','6ulvd_mw_uo','clifZdPnX9E']
            random_index = random.randrange(1, len(senior1_main_list))
            main_video_id = senior1_main_list[random_index]
            main_list.append(main_video_id)
            return main_list