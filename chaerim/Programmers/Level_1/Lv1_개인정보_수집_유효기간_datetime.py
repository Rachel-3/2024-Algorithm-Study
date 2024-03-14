import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []

    term_dict = {}
    for term in terms:
        key, value = term.split()
        term_dict[key] = int(value)

    today = datetime.datetime.strptime(today, "%Y.%m.%d")

    for idx, privacy in enumerate(privacies, start=1):
        date, term = privacy.split()
        date = datetime.datetime.strptime(date, "%Y.%m.%d")
        valid_months = term_dict[term]

        expire_date = date + relativedelta(months=valid_months)

        if today >= expire_date:
            answer.append(idx)

    return answer