from second.models import User

def create_user(username:str, password:str, nickname:str, gender:str, level:str):
    if gender == "남자": #gender에 따라 기본 프로필 이미지 다르게 유저생성해주는것 추가
        new_user = User.objects.create(username=username,
                                    password=password,
                                    nickname=nickname,
                                    gender=gender,
                                    level=level,
                                    profile_img='/static/img/male.png')
        return new_user
    else:#여자라면
        new_user = User.objects.create(username=username,
                                       password=password,
                                       nickname=nickname,
                                       gender=gender,
                                       level=level,
                                       profile_img='/static/img/female.png')
        return new_user

def check_blank(username, password, nickname, gender, level):
    if username == "" or password == "" or nickname == "" or gender == None or level == None:
        msg = '빈칸인 항목이 있는지 확인하세요'
        return msg
    else:
        msg = '통과'
        return msg