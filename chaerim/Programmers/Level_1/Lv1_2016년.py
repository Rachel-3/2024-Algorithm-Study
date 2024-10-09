import datetime

def solution(a, b):
    answer = ''

    day_of_the_week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

    date = datetime.date(2016, a, b)

    answer += day_of_the_week[date.weekday()]

    return answer