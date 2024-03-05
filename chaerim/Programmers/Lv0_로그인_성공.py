def solution(id_pw, db):
    answer = 'fail'

    for user_id_pw in db:
        if user_id_pw[0] == id_pw[0]:
            if user_id_pw[1] == id_pw[1]:
                answer = "login"
            else:
                answer = "wrong pw"

    return answer