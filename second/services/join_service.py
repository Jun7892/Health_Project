from second.models import User

def create_user(username:str, password:str, nickname:str, email:str, gender:str, changed_age:str, age):
    if gender == "남자": #gender에 따라 기본 프로필 이미지 다르게 유저생성해주는것 추가
        new_user = User.objects.create_user(
                                    username= username,
                                    password= password,
                                    nickname= nickname,
                                    first_name=age,
                                    email= email,
                                    gender= gender,
                                    level= '',
                                    age= changed_age,
                                    profile_img= "https://tenten2.s3.ap-northeast-2.amazonaws.com/img/male.png")
        return new_user
    else:#여자라면
        new_user = User.objects.create_user(
                                    username= username,
                                    password= password,
                                    nickname= nickname,
                                    first_name=age,
                                    email=email,
                                    gender= gender,
                                    level='',
                                    age = changed_age,
                                    profile_img="https://tenten2.s3.ap-northeast-2.amazonaws.com/img/female.png")
        return new_user

def change_age(age):
    if int(age) < 13 and int(age) >= 11:
        age = '유소년'
        return age
    elif int(age) >= 13 and int(age) < 19:
        age = '청소년'
        return age
    elif int(age) >= 19 and int(age) < 65:
        age = '성인'
        return age
    elif int(age) >= 65 and int(age) < 100:
        age = '노인'
        return age
    elif int(age) >=0 and int(age) < 11:
        age = 'baby'
        return age
    else:
        age = 'error'
        return age