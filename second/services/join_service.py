from second.models import User


def create_user(username:str, password:str, nickname:str, gender:str, level:str):
     new_user = User.objects.create(username=username,
                                    password=password,
                                    nickname=nickname,
                                    gender=gender,
                                    level=level)
     return new_user


def check_blank(username, password, nickname, gender, level):
     if username == "" or password == "" or nickname == "" or gender == None or level == None:
          msg = '빈칸인 항목이 있는지 확인하세요'
          return msg
     else:
          msg = '통과'
          return msg