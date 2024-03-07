def solution(money):
    coffee = money//5500
    ex_money = money - coffee*5500
    
    answer = [coffee, ex_money]

    return answer