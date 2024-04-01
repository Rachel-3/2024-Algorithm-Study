def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)) :
        each_discount = discount[i:i + 10]
        count = 0
        for j in range(len(number)) :
            if each_discount.count(want[j]) == number[j] :
                count += 1
        if count == len(number) :
            answer += 1
    return answer