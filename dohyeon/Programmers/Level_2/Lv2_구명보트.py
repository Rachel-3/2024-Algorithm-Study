def solution(people, limit):
    answer = 1
    people.sort(reverse = True)
    print(people)
    current_weight = people[0]
    m = 1
    while m < len(people) :
        if current_weight + people[m] <= limit :
            current_weight += people[m]
            m += 1
        else :
            answer += 1
            current_weight = 0
        # break
    return answer

print(solution([70, 50, 80, 50],100)) # 3
print(solution([70, 80, 50], 100)) # 3