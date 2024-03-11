def solution(number):
    answer = sum(map(int, str(number))) % 9
    return answer