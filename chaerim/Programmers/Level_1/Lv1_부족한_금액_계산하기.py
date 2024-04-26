def solution(price, money, count):
    answer = 0

    sum_money = 0
    current_price = price
    for i in range(count):
        sum_money += current_price
        current_price += price

    answer = sum_money - money if money < sum_money else 0

    return answer