def solution(people, limit):
    answer = 0

    people.sort()

    light_people = 0
    heavy_people = len(people)-1
    while light_people <= heavy_people:
        if people[light_people] + people[heavy_people] <= limit:
            light_people += 1
            heavy_people -= 1
            answer += 1
        else:
            heavy_people -= 1
            answer += 1

    return answer