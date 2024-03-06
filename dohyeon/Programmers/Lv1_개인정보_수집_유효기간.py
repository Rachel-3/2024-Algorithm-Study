import datetime
from dateutil.relativedelta import relativedelta

def str_to_time(string) :
    return datetime.datetime.strptime(string, "%Y.%m.%d")

def add_months(date, month) :
    return date + relativedelta(months = month) + relativedelta(days = -1)

def solution(today, terms, privacies):
    answer = []
    privacy_type = {}
    for i in terms :
        privacy_type[i.split(" ")[0]] = int(i.split(" ")[1])
    today = str_to_time(today)
    for i in range(len(privacies)) :
        stored_date, types = privacies[i].split(" ")
        
        stored_date = str_to_time(stored_date)
        month = privacy_type[types]
        validation_date = add_months(stored_date, month)
        if today > validation_date :
            answer.append(i + 1)


    return answer

# print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
# print(solution("2020.01.01", ["Z 3", "D 5"],["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))