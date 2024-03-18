def solution(progresses, speeds):
    answer = []
    deadline = []

    for progress, speed in zip(progresses, speeds):
        remaining_progress = 100 - progress
        day = remaining_progress // speed
        if remaining_progress%speed != 0:
            day += 1
        deadline.append(day)

    count = 1
    prev_day = deadline[0]
    for day in deadline[1:]:
        if day <= prev_day:
            count += 1
        else:
            answer.append(count)
            count = 1
            prev_day = day
    answer.append(count)

    return answer