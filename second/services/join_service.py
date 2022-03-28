from second.models import User

def create_user(username:str, password:str, nickname:str, email:str, gender:str, level:str):
    if gender == "남자": #gender에 따라 기본 프로필 이미지 다르게 유저생성해주는것 추가
        new_user = User.objects.create_user(username= username,
                                    password= password,
                                    nickname= nickname,
                                    email= email,
                                    gender= gender,
                                    level= level,
                                    profile_img= '/static/img/male.png')
        return new_user
    else:#여자라면
        new_user = User.objects.create_user(username= username,
                                       password= password,
                                       nickname= nickname,
                                       email=email,
                                       gender= gender,
                                       level= level,
                                       profile_img='/static/img/female.png')
        return new_user