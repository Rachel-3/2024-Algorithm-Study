def solution(id_pw, db):
    answer = ''
    db = dict(db)
    id, pw = id_pw[0], id_pw[1]
    if id not in db :
        answer = "fail"
    elif db[id] == pw :
        answer = "login"
    else :
        answer = "wrong pw"
    return answer
