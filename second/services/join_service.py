from second.models import User
import bcrypt

def create_user(username:str, password:str, nickname:str, email:str, gender:str, level:str):
    hashed_password = password_hashing(password)#저장시 패스워드 암호화

    if gender == "남자": #gender에 따라 기본 프로필 이미지 다르게 유저생성해주는것 추가
        new_user = User.objects.create(username= username,
                                    password= hashed_password,
                                    nickname= nickname,
                                    email= email,
                                    gender= gender,
                                    level= level,
                                    profile_img= '/static/img/male.png')
        return new_user
    else:#여자라면
        new_user = User.objects.create(username= username,
                                       password= hashed_password,
                                       nickname= nickname,
                                       email=email,
                                       gender= gender,
                                       level= level,
                                       profile_img='/static/img/female.png')
        return new_user


def password_hashing(password):
    # hashing과 salting을 해주기 위해 문자열에서 byte 타입으로 변환
    encoded_password = password.encode('utf-8')
    # bcrypt로 비밀번호 hashing 및 salting.
    # salting 하는 이유
        # hashing은 단방향 암호화 방식이다. 같은 값을 해싱하면 해싱값 또한 항상 같다.
        # 따라서 해싱값 데이터가 쌓이면 역으로 암호가 드러나는 위험성이 있다. 이 점을 보완하기 위해 salting 과정을 추가해서 더 복잡하게 암호화 한다.
    hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
    #DB저장위해 다시 str타입으로 decoding
        # DB에 비밀번호를 저장할 때 반드시 암호화한 형태를 저장해야 한다.
        # hased_password는 byte 타입으로 인코딩 되어있음,
        # DB에 저장할 때는 다시 string 타입으로 디코딩 해줘야 한다. 안하면....비교할때 엄청 힘들어져요...ㅎㅎㅎ
    decoded_hashed_password = hashed_password.decode('utf-8')
    return decoded_hashed_password