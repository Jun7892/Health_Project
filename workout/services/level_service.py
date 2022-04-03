
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
