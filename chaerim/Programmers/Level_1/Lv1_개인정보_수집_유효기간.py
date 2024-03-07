def solution(today, terms, privacies):
    answer = []

    term_dict = {}
    for term in terms:
        key, value = term.split()
        term_dict[key] = int(value)

    today_y, today_m, today_d = map(int, today.split("."))

    for idx, privacy in enumerate(privacies, start=1):
        date, term = privacy.split()
        date_y, date_m, date_d = map(int, date.split("."))
        valid_months = term_dict[term]

        expire_y, expire_m, expire_d = date_y, date_m + valid_months, date_d - 1
        
        if expire_m > 12:
            expire_y += (expire_m - 1) // 12
            expire_m = (expire_m - 1) % 12 + 1
        
        if expire_d == 0:
            expire_m -= 1 
            if expire_m == 0:
                expire_m = 12
                expire_y -= 1
            expire_d = 28

        if today_y > expire_y or (today_y == expire_y and today_m > expire_m) or (today_y == expire_y and today_m == expire_m and today_d > expire_d):
            answer.append(idx)

    return answer