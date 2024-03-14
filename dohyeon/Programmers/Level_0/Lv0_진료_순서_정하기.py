def solution(emergency):
    answer = []
    biggest_emergency = sorted(emergency, reverse = True)
    answer = [biggest_emergency.index(s) + 1 for s in emergency]
    return answer