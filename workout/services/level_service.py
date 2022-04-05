
def boy_youth_level_service(real_age, count, user): # 유소년 남자
    if real_age == 11: #11살이면
        if count >= 0 and count < 30: #횟수 30미만이면 3등급
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 30 <= count < 33:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif count >= 33:
            user.level = '1등급'
            user.save()
            return '1등급'

    else: #12살이면
        if 0 <= count < 29:  # 횟수 30미만이면 3등급
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 30 <= count < 32:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif count >= 32:
            user.level = '1등급'
            user.save()
            return '1등급'


def girl_youth_level_service(real_age, count, user):#유소년 여자
    if real_age == 11: #11살이면
        if 0 <= count < 30: #횟수 30미만이면 3등급
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 30 <= count < 32:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif count >= 33:
            user.level = '1등급'
            user.save()
            return '1등급'

    else: #12살이면
        if 0 <= count < 30:  # 횟수 30미만이면 3등급
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 30 <= count < 33:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif count >= 34:
            user.level = '1등급'
            user.save()
            return '1등급'

def man_senior_level_service(real_age, count, user):
    if 65 <= real_age < 70:#65~69세
        if 0 <= count < 21:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 21 <= count < 25:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif count >= 25:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif 70 <= real_age < 75:
        if 0 <= count < 20:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 20 <= count < 23:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif count >= 23:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif 75 <= real_age < 80:
        if 0 <= count < 17:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 17 <= count < 21:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif count >= 21:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif 80 <= real_age < 85:
        if 0 <= count < 15:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 15 <= count < 19:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif count >= 19:
            user.level = '1등급'
            user.save()
            return '1등급'

    else: # 85세 이상
        if 0 <= count < 13:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 13 <= count < 17:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif count >= 17:
            user.level = '1등급'
            user.save()
            return '1등급'

def woman_senior_level_service(real_age, count, user):
    if 65 <= real_age < 70:#65~69세
        if 0 <= count < 19:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 19 <= count < 22:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif count >= 22:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif 70 <= real_age < 75:
        if 0 <= count < 17:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 17 <= count < 20:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif count >= 20:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif 75 <= real_age < 80:
        if 0 <= count < 15:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 15 <= count < 18:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif count >= 18:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif 80 <= real_age < 85:
        if 0 <= count < 13:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 13 <= count < 15:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif count >= 15:
            user.level = '1등급'
            user.save()
            return '1등급'

    else: # 85세 이상
        if 0 <= count < 11:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 11 <= count < 14:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 14 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'


def boy_student_level_service(real_age, count, user):
    if real_age == 13:
        if 0 <= count < 49:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 49 <= count < 61:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 61 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif real_age == 14:
        if 0 <= count < 48:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 48 <= count < 60:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 60 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif real_age == 15:
        if 0 <= count < 39:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 39 <= count < 49:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 49 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif real_age == 16:
        if 0 <= count < 38:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 38 <= count < 49:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 49 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif real_age == 17:
        if 0 <= count < 36:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 36 <= count < 46:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 46 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif real_age == 18:
        if 0 <= count < 41:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 41 <= count < 53:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 53 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'



def girl_student_level_service(real_age, count, user):
    if real_age == 13:
        if 0 <= count < 37:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 37 <= count < 48:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 48 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif real_age == 14:
        if 0 <= count < 36:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 36 <= count < 47:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 47 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif real_age == 15:
        if 0 <= count < 36:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 36 <= count < 48:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 48 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif real_age == 16:
        if 0 <= count < 30:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 30 <= count < 41:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 41 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif real_age == 17 or real_age == 18:
        if 0 <= count < 29:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 30 <= count < 41:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 41 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'

def man_adult_level_service(real_age, count, user):
    if 19 <= real_age < 25:
        if 0<= count < 48:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 48 <= count < 55:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 55 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif 25 <= real_age < 30:
        if 0 <= count < 45:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 45 <= count < 51:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 51 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif 30 <= real_age < 35:
        if 0 <= count < 41:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 41 <= count < 47:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 47 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif 35 <= real_age < 40:
        if 0 <= count < 39:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 39 <= count < 45:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 45 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif 40 <= real_age < 45:
        if 0 <= count < 38:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 38 <= count < 44:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 44 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif 45 <= real_age < 50:
        if 0 <= count < 36:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 36 <= count < 41:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 41 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif 50 <= real_age < 55:
        if 0 <= count < 32:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 32 <= count < 38:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 38 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif 55 <= real_age < 60:
        if 0 <= count < 29:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 29 <= count < 35:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 35 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif 60 <= real_age < 65:
        if 0 <= count < 25:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 25 <= count < 31:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 31 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'


def woman_adult_level_service(real_age, count, user):
    if 19 <= real_age < 25:
        if 0<= count < 30:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 30 <= count < 36:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 36 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif 25 <= real_age < 30:
        if 0 <= count < 27:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 27 <= count < 33:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 33 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif 30 <= real_age < 35 or 35 <= real_age < 40:
        if 0 <= count < 25:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 25<= count < 31:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 31 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif 40 <= real_age < 45:
        if 0 <= count < 25:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 25<= count < 30:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 30 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif 45 <= real_age < 50:
        if 0 <= count < 22:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 22<= count < 24:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 34 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif 50 <= real_age < 55:
        if 0 <= count < 19:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif count == 19:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 20 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif 55 <= real_age < 60:
        if 0 <= count < 15:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 15 <= count < 20:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 20 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'

    elif 60 <= real_age < 65:
        if 0 <= count < 12:
            user.level = '3등급'
            user.save()
            return '3등급'
        elif 12<= count < 17:
            user.level = '2등급'
            user.save()
            return '2등급'
        elif 17 <= count:
            user.level = '1등급'
            user.save()
            return '1등급'