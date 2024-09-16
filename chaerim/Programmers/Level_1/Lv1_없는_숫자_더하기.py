def solution(numbers):
    answer = 0
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for num in numbers:
        if num in number:
            number.remove(num)

    for ex in number:
        answer += ex

    return answer