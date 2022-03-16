import bcrypt


def login_check_blank(username, password):
    if username == '' or password == '':
        msg = '빈칸있음'
        return msg
    else:
        msg = '통과'
        return msg

def check_password_correct(inputpassword,dbpassword):
    #비밀번호 일치하는지 확인할때는 인코딩필수.
    #bcrypt의 checkpw가 입력받은 패스워드와 db의 패스워드 알아서 비교해줌! 일치하면 True반환
    result = bcrypt.checkpw(inputpassword.encode('utf-8'), dbpassword.encode('utf-8'))
    return result