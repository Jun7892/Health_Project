

def login_check_blank(username, password):
    if username == '' or password == '':
        msg = '빈칸있음'
        return msg
    else:
        msg = '통과'
        return msg