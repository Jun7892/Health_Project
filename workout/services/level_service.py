
def boy_youth_level_service(real_age, count, user): # 유소년 남자
    if int(real_age) == 11: #11살이면
        if count >= 0 and count < 30: #횟수 30미만이면 3등급
            user.level = '3등급'
            user.save()
        elif count >= 30 and count < 33:
            user.level = '2등급'
            user.save()
        elif count >= 33:
            user.level = '1등급'
            user.save()

    else: #12살이면
        if count >= 0 and count < 29:  # 횟수 30미만이면 3등급
            user.level = '3등급'
            user.save()
        elif count >= 30 and count < 32:
            user.level = '2등급'
            user.save()
        elif count >= 32:
            user.level = '1등급'
            user.save()


def girl_youth_level_service(real_age, count, user):#유소년 여자
    if int(real_age) == 11: #11살이면
        if count >= 0 and count < 30: #횟수 30미만이면 3등급
            user.level = '3등급'
            user.save()
        elif count >= 30 and count < 32:
            user.level = '2등급'
            user.save()
        elif count >= 33:
            user.level = '1등급'
            user.save()

    else: #12살이면
        if count >= 0 and count < 30:  # 횟수 30미만이면 3등급
            user.level = '3등급'
            user.save()
        elif count >= 30 and count < 33:
            user.level = '2등급'
            user.save()
        elif count >= 34:
            user.level = '1등급'
            user.save()


def man_senior_level_service(real_age, count, user):
    if int(real_age) >= 65 and int(real_age) < 70:#65~69세
        if count>=0 and count < 21:
            user.level = '3등급'
            user.save()
        elif count>=21 and count < 25:
            user.level = '2등급'
            user.save()
        elif count >= 25:
            user.level = '1등급'
            user.save()

    elif int(real_age) >= 70 and int(real_age) < 75:
        if count >= 0 and count < 20:
            user.level = '3등급'
            user.save()
        elif count >= 20 and count < 23:
            user.level = '2등급'
            user.save()
        elif count >= 23:
            user.level = '1등급'
            user.save()

    elif int(real_age) >= 75 and int(real_age) < 80:
        if count >= 0 and count < 17:
            user.level = '3등급'
            user.save()
        elif count >= 17 and count < 21:
            user.level = '2등급'
            user.save()
        elif count >= 21:
            user.level = '1등급'
            user.save()

    elif int(real_age) >= 80 and int(real_age) < 85:
        if count >= 0 and count < 15:
            user.level = '3등급'
            user.save()
        elif count >= 15 and count < 19:
            user.level = '2등급'
            user.save()
        elif count >= 19:
            user.level = '1등급'
            user.save()

    else: # 85세 이상
        if count >= 0 and count < 13:
            user.level = '3등급'
            user.save()
        elif count >= 13 and count < 17:
            user.level = '2등급'
            user.save()
        elif count >= 17:
            user.level = '1등급'
            user.save()

def woman_senior_level_service(real_age, count, user):
    if int(real_age) >= 65 and int(real_age) < 70:#65~69세
        if count>=0 and count < 19:
            user.level = '3등급'
            user.save()
        elif count>=19 and count < 22:
            user.level = '2등급'
            user.save()
        elif count >= 22:
            user.level = '1등급'
            user.save()

    elif int(real_age) >= 70 and int(real_age) < 75:
        if count >= 0 and count < 17:
            user.level = '3등급'
            user.save()
        elif count >= 17 and count < 20:
            user.level = '2등급'
            user.save()
        elif count >= 20:
            user.level = '1등급'
            user.save()

    elif int(real_age) >= 75 and int(real_age) < 80:
        if count >= 0 and count < 15:
            user.level = '3등급'
            user.save()
        elif count >= 15 and count < 18:
            user.level = '2등급'
            user.save()
        elif count >= 18:
            user.level = '1등급'
            user.save()

    elif int(real_age) >= 80 and int(real_age) < 85:
        if count >= 0 and count < 13:
            user.level = '3등급'
            user.save()
        elif count >= 13 and count < 15:
            user.level = '2등급'
            user.save()
        elif count >= 15:
            user.level = '1등급'
            user.save()

    else: # 85세 이상
        if count >= 0 and count < 11:
            user.level = '3등급'
            user.save()
        elif count >= 11 and count < 14:
            user.level = '2등급'
            user.save()
        elif count >= 14:
            user.level = '1등급'
            user.save()